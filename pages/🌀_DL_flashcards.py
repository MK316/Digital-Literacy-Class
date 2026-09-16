import io
import random
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas


st.set_page_config(
    page_title="Digital Literacy Flashcards",
    page_icon="💻",
    layout="wide",
)

SET_SIZE = 20
TZ = ZoneInfo("Asia/Seoul")


def find_data_file():
    """Find terms_data.md whether this app is in the repo root or in pages/."""
    app_dir = Path(__file__).resolve().parent
    candidates = [
        app_dir / "terms_data.md",
        app_dir.parent / "data"/"terms_data.md",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


@st.cache_data
def load_terms_from_markdown(path_str):
    """Read the human-readable Markdown vocabulary file as app data."""
    text = Path(path_str).read_text(encoding="utf-8")

    pattern = re.compile(
        r"^###\s+\d+\.\s+(?P<keyword>.+?)\s*$"
        r"\n\s*\n\*\*Explanation:\*\*\s*(?P<explanation>.*?)"
        r"\n\s*\n\*\*Quiz prompt:\*\*\s*(?P<question>.*?)"
        r"\n\s*\n\*\*Accepted answers:\*\*\s*(?P<aliases>.*?)"
        r"(?=\n\s*\n---)",
        re.MULTILINE | re.DOTALL,
    )

    terms = []
    for match in pattern.finditer(text):
        aliases_raw = match.group("aliases").strip()
        aliases = [] if aliases_raw in {"", "—", "-", "None"} else [
            x.strip() for x in aliases_raw.split(";") if x.strip()
        ]
        terms.append((
            match.group("keyword").strip(),
            re.sub(r"\s+", " ", match.group("explanation").strip()),
            re.sub(r"\s+", " ", match.group("question").strip()),
            aliases,
        ))

    return terms


DATA_FILE = find_data_file()
if DATA_FILE is None:
    st.error("terms_data.md was not found. Put it beside this app file or in the repository root.")
    st.stop()

TERMS = load_terms_from_markdown(str(DATA_FILE))
if len(TERMS) != 100:
    st.error(f"Expected 100 vocabulary entries in terms_data.md, but found {len(TERMS)}.")
    st.stop()

SET_LABELS = {
    1: "Set 1 · Digital Foundations",
    2: "Set 2 · Data & Coding Basics",
    3: "Set 3 · App Development & Git",
    4: "Set 4 · Platforms & AI Basics",
    5: "Set 5 · AI, Deployment & APIs",
}


def now_kst():
    return datetime.now(TZ)


def fmt_time(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S") if dt else ""


def normalize_answer(text):
    """Case-insensitive grading; ignores spaces, hyphens, underscores, and punctuation."""
    return re.sub(r"[^a-z0-9]", "", (text or "").lower())


def answer_is_correct(user_answer, item):
    accepted = [item[0], *item[3]]
    target_set = {normalize_answer(x) for x in accepted}
    return normalize_answer(user_answer) in target_set


def valid_english_name(name):
    # English alphabet plus ordinary punctuation used in names.
    return bool(re.fullmatch(r"[A-Za-z][A-Za-z .'-]*", (name or "").strip()))


def get_set_items(set_no):
    start = (set_no - 1) * SET_SIZE
    end = start + SET_SIZE
    return TERMS[start:end]


def reset_learning_state(new_set=None):
    # Clear prior quiz-entry widgets so a retake starts with blank answers.
    for key in list(st.session_state.keys()):
        if key.startswith("quiz_") and key not in {
            "quiz_started", "quiz_submitted", "quiz_order", "quiz_start",
            "quiz_end", "quiz_results"
        }:
            del st.session_state[key]

    if new_set is not None:
        st.session_state.active_set = new_set
    st.session_state.selected_unknown = []
    st.session_state.card_index = 0
    st.session_state.practice_ready = False
    st.session_state.quiz_started = False
    st.session_state.quiz_submitted = False
    st.session_state.quiz_order = []
    st.session_state.quiz_start = None
    st.session_state.quiz_end = None
    st.session_state.student_name = ""
    st.session_state.quiz_results = []


if "active_set" not in st.session_state:
    st.session_state.active_set = 1
    reset_learning_state(1)


# ---------------- PDF ----------------
def build_pdf_report(name, set_no, start_time, end_time, results):
    """Create a one-page landscape A4 result report."""
    buffer = io.BytesIO()
    page_size = landscape(A4)
    width, height = page_size
    c = canvas.Canvas(buffer, pagesize=page_size)

    left = 28
    top = height - 28

    c.setFont("Helvetica-Bold", 15)
    c.drawString(left, top, "Digital Literacy Quiz Report")

    c.setFont("Helvetica", 8.7)
    meta_y = top - 22
    c.drawString(left, meta_y, f"Name: {name}")
    c.drawString(left + 240, meta_y, f"Set: {set_no}")
    c.drawString(left + 330, meta_y, f"Start: {fmt_time(start_time)}")
    c.drawString(left + 555, meta_y, f"End: {fmt_time(end_time)}")

    score = sum(1 for r in results if r["correct"])
    pct = score / len(results) * 100 if results else 0

    table_data = [["No.", "Your answer", "Correct answer", "Result"]]
    for r in results:
        table_data.append([
            str(r["no"]),
            r["user_answer"] or "—",
            r["correct_answer"],
            "Correct" if r["correct"] else "Incorrect",
        ])

    table = Table(
        table_data,
        colWidths=[42, 280, 280, 90],
        rowHeights=[18] + [17] * len(results),
    )
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EEEEEE")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.7),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (-1, 1), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.45, colors.HexColor("#BBBBBB")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))

    tw, th = table.wrapOn(c, width - 2 * left, height)
    table_y = meta_y - 12 - th
    table.drawOn(c, left, table_y)

    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(left, table_y - 22, f"Total Score: {score}/{len(results)} ({pct:.0f}%)")

    c.setFont("Helvetica-Oblique", 7.5)
    note = "Answers are graded case-insensitively; spaces and punctuation are ignored. Common accepted aliases may also receive credit."
    # keep note on one line if possible
    if stringWidth(note, "Helvetica-Oblique", 7.5) < width - 2 * left:
        c.drawString(left + 270, table_y - 22, note)

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.getvalue()


# ---------------- Styling ----------------
st.markdown(
    """
    <style>
    .flashcard {
        border: 1px solid #d9d9d9;
        border-radius: 14px;
        padding: 32px 28px;
        min-height: 175px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        background: #fafafa;
        margin: 8px 0 14px 0;
    }
    .flashcard-term {
        font-size: 2rem;
        font-weight: 700;
        letter-spacing: 0.2px;
    }
    .set-note {
        font-size: 0.92rem;
        color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Digital Literacy & App Development Flashcards")
st.caption("100 core terms · 5 non-overlapping sets · 20 terms per set")

# Keep set fixed while a quiz is active.
set_no = st.selectbox(
    "Choose a 20-word set",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: SET_LABELS[x],
    index=st.session_state.active_set - 1,
    disabled=st.session_state.quiz_started,
)

if set_no != st.session_state.active_set:
    reset_learning_state(set_no)

items = get_set_items(st.session_state.active_set)

tab_list, tab_practice, tab_quiz, tab_result = st.tabs(
    ["1. Word List", "2. Practice", "3. Quiz", "4. Result"]
)

# ============================================================
# TAB 1 — WORD LIST
# ============================================================
with tab_list:
    st.subheader(SET_LABELS[st.session_state.active_set])
    st.write("Review the 20 keywords before practice. The five sets never overlap.")

    rows = []
    global_start = (st.session_state.active_set - 1) * SET_SIZE
    for i, item in enumerate(items, start=1):
        rows.append({"No.": global_start + i, "Keyword": item[0]})
    st.dataframe(rows, hide_index=True, use_container_width=True)

    with st.expander("Show all 100 keywords"):
        for s in range(1, 6):
            st.markdown(f"**{SET_LABELS[s]}**")
            words = [x[0] for x in get_set_items(s)]
            st.write(" · ".join(words))

    st.download_button(
        "Download vocabulary data (.md)",
        data=DATA_FILE.read_bytes(),
        file_name="terms_data.md",
        mime="text/markdown",
    )

    with st.expander("View vocabulary data source"):
        st.markdown(DATA_FILE.read_text(encoding="utf-8"))

# ============================================================
# TAB 2 — PRACTICE
# ============================================================
with tab_practice:
    st.subheader("Select what you do not know")
    st.write(
        "Check only the terms you do **not** know yet. Your flashcard practice will use only those terms."
    )

    with st.form(f"unknown_form_{st.session_state.active_set}"):
        c1, c2 = st.columns(2)
        selected_terms = []
        for i, item in enumerate(items):
            target_col = c1 if i < 10 else c2
            with target_col:
                checked = st.checkbox(
                    item[0],
                    key=f"unknown_{st.session_state.active_set}_{i}",
                )
                if checked:
                    selected_terms.append(item[0])

        apply_selection = st.form_submit_button("Study selected words", use_container_width=True)

    if apply_selection:
        st.session_state.selected_unknown = selected_terms
        st.session_state.card_index = 0
        st.session_state.practice_ready = False
        st.session_state.quiz_started = False
        st.session_state.quiz_submitted = False
        st.session_state.quiz_results = []

    selected_items = [x for x in items if x[0] in st.session_state.selected_unknown]

    if st.session_state.selected_unknown:
        st.divider()
        st.markdown(f"**Selected for practice: {len(selected_items)} word(s)**")

        idx = min(st.session_state.card_index, len(selected_items) - 1)
        item = selected_items[idx]
        st.session_state.card_index = idx

        st.markdown(
            f'<div class="flashcard"><div class="flashcard-term">{item[0]}</div></div>',
            unsafe_allow_html=True,
        )
        st.caption(f"Card {idx + 1} of {len(selected_items)}")

        with st.expander("Show explanation"):
            st.write(item[1])
            if item[3]:
                st.caption("Also used: " + ", ".join(item[3]))

        prev_col, next_col, ready_col = st.columns([1, 1, 2])
        with prev_col:
            if st.button("← Previous", disabled=idx == 0, use_container_width=True):
                st.session_state.card_index -= 1
                st.rerun()
        with next_col:
            if st.button("Next →", disabled=idx == len(selected_items) - 1, use_container_width=True):
                st.session_state.card_index += 1
                st.rerun()
        with ready_col:
            if st.button("I’m ready for the quiz", type="primary", use_container_width=True):
                st.session_state.practice_ready = True
                st.success("Quiz unlocked. Open the Quiz tab.")

    else:
        st.info("No unknown terms are currently selected. If you already know all 20, you may go directly to the quiz.")
        if st.button("I know all 20 · Unlock quiz", type="primary"):
            st.session_state.practice_ready = True
            st.success("Quiz unlocked. Open the Quiz tab.")

# ============================================================
# TAB 3 — QUIZ
# ============================================================
with tab_quiz:
    st.subheader("Final Quiz · 20 items")
    st.write(
        "Each of the 20 terms in this set appears exactly once. Read the description and type the keyword."
    )

    if not st.session_state.practice_ready and not st.session_state.quiz_started and not st.session_state.quiz_submitted:
        st.warning("Complete the Practice step first to unlock the quiz.")

    elif not st.session_state.quiz_started and not st.session_state.quiz_submitted:
        name = st.text_input(
            "Name (English only)",
            value=st.session_state.student_name,
            placeholder="e.g., Minji Kim",
        )
        st.caption("Use English letters only. Spaces, hyphens, apostrophes, and periods are allowed.")

        if st.button("Start Quiz", type="primary"):
            if not valid_english_name(name):
                st.error("Please enter your name using English letters only.")
            else:
                st.session_state.student_name = name.strip()
                order = list(range(SET_SIZE))
                random.shuffle(order)
                st.session_state.quiz_order = order
                st.session_state.quiz_start = now_kst()
                st.session_state.quiz_started = True
                st.session_state.quiz_results = []
                st.rerun()

    elif st.session_state.quiz_started:
        st.caption(
            f"Name: {st.session_state.student_name}  ·  Started: {fmt_time(st.session_state.quiz_start)}"
        )

        with st.form(f"quiz_form_{st.session_state.active_set}"):
            current_answers = []
            for q_no, item_idx in enumerate(st.session_state.quiz_order, start=1):
                item = items[item_idx]
                st.markdown(f"**{q_no}. {item[2]}**")
                answer = st.text_input(
                    "Your answer",
                    key=f"quiz_{st.session_state.active_set}_{item_idx}",
                    max_chars=40,
                    label_visibility="collapsed",
                    placeholder="Type one keyword",
                )
                current_answers.append((q_no, item_idx, answer))

            submitted = st.form_submit_button("Submit Quiz", type="primary", use_container_width=True)

        if submitted:
            blanks = [q for q, _, ans in current_answers if not ans.strip()]
            if blanks:
                st.error("Please answer all 20 questions before submitting.")
            else:
                results = []
                for q_no, item_idx, answer in current_answers:
                    item = items[item_idx]
                    results.append({
                        "no": q_no,
                        "user_answer": answer.strip(),
                        "correct_answer": item[0],
                        "correct": answer_is_correct(answer, item),
                    })

                st.session_state.quiz_results = results
                st.session_state.quiz_end = now_kst()
                st.session_state.quiz_started = False
                st.session_state.quiz_submitted = True
                st.rerun()

    else:
        score = sum(1 for r in st.session_state.quiz_results if r["correct"])
        st.success(f"Quiz completed: {score}/20")
        st.write("Open the **Result** tab to review your answers and download the PDF report.")

# ============================================================
# TAB 4 — RESULT
# ============================================================
with tab_result:
    st.subheader("Quiz Result")

    if not st.session_state.quiz_submitted:
        st.info("Complete the quiz to see your result.")
    else:
        results = st.session_state.quiz_results
        score = sum(1 for r in results if r["correct"])
        pct = score / len(results) * 100

        m1, m2, m3 = st.columns(3)
        m1.metric("Score", f"{score}/20")
        m2.metric("Percentage", f"{pct:.0f}%")
        m3.metric("Set", str(st.session_state.active_set))

        st.write(f"**Name:** {st.session_state.student_name}")
        st.write(f"**Start:** {fmt_time(st.session_state.quiz_start)}")
        st.write(f"**End:** {fmt_time(st.session_state.quiz_end)}")

        result_rows = []
        for r in results:
            result_rows.append({
                "No.": r["no"],
                "Your answer": r["user_answer"],
                "Correct answer": r["correct_answer"],
                "Result": "✓" if r["correct"] else "✗",
            })
        st.dataframe(result_rows, hide_index=True, use_container_width=True)

        pdf_bytes = build_pdf_report(
            st.session_state.student_name,
            st.session_state.active_set,
            st.session_state.quiz_start,
            st.session_state.quiz_end,
            results,
        )

        safe_name = re.sub(r"[^A-Za-z0-9_-]", "_", st.session_state.student_name.strip())
        st.download_button(
            "Download one-page PDF report",
            data=pdf_bytes,
            file_name=f"digital_literacy_quiz_{safe_name}_set{st.session_state.active_set}.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True,
        )

        if st.button("Start another set"):
            reset_learning_state(st.session_state.active_set)
            st.rerun()
