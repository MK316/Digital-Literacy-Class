import csv
import io
import random
import html
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import streamlit as st
import requests
from gtts import gTTS
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Digital Literacy Flashcards",
    page_icon="💻",
    layout="wide",
)

SET_SIZE = 20
TOTAL_TERMS = 100
TZ = ZoneInfo("Asia/Seoul")


# ============================================================
# DATA SOURCE (GitHub raw CSV)
# ============================================================

DATA_URL = (
    "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/"
    "refs/heads/main/pages/data/terms_data_with_context.csv"
)


@st.cache_data(ttl=3600, show_spinner=False)
def fetch_csv_bytes(url):
    """Fetch the latest published CSV; cache for one hour."""
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.content


@st.cache_data(show_spinner=False)
def parse_terms(csv_bytes):
    """Read the CSV including the new context_paragraph field."""
    terms = []
    content = csv_bytes.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(content))
    required_columns = {
        "number", "set", "set_name", "keyword", "explanation",
        "quiz_prompt", "accepted_answers", "context_paragraph",
    }
    missing = required_columns - set(reader.fieldnames or [])
    if missing:
        raise ValueError("Missing CSV column(s): " + ", ".join(sorted(missing)))

    for row in reader:
        aliases = [
            value.strip()
            for value in (row.get("accepted_answers") or "").split(";")
            if value.strip()
        ]
        terms.append({
            "number": int(row["number"]),
            "set": int(row["set"]),
            "set_name": row["set_name"].strip(),
            "keyword": row["keyword"].strip(),
            "explanation": row["explanation"].strip(),
            "question": row["quiz_prompt"].strip(),
            "aliases": aliases,
            "context": (row.get("context_paragraph") or "").strip(),
        })
    terms.sort(key=lambda item: item["number"])
    return terms


try:
    CSV_BYTES = fetch_csv_bytes(DATA_URL)
    TERMS = parse_terms(CSV_BYTES)
except Exception as exc:
    st.error("Unable to load the vocabulary CSV from GitHub.")
    st.code(str(exc))
    st.markdown(f"[Open CSV directly]({DATA_URL})")
    if st.button("Retry loading CSV"):
        fetch_csv_bytes.clear()
        st.rerun()
    st.stop()


# ============================================================
# DATA VALIDATION
# ============================================================

if len(TERMS) != TOTAL_TERMS:
    st.error(
        f"Expected {TOTAL_TERMS} vocabulary entries, "
        f"but found {len(TERMS)}."
    )
    st.stop()

numbers = [item["number"] for item in TERMS]
if numbers != list(range(1, TOTAL_TERMS + 1)):
    st.error("The number column must run continuously from 1 to 100.")
    st.stop()

for set_no in range(1, 6):
    count = sum(1 for item in TERMS if item["set"] == set_no)
    if count != SET_SIZE:
        st.error(
            f"Set {set_no} contains {count} terms. "
            f"Each set must contain exactly {SET_SIZE}."
        )
        st.stop()


SET_LABELS = {
    set_no: f"Set {set_no} · {next(item['set_name'] for item in TERMS if item['set'] == set_no)}"
    for set_no in range(1, 6)
}


def get_set_items(set_no):
    return [item for item in TERMS if item["set"] == set_no]


# ============================================================
# HELPERS
# ============================================================

def now_kst():
    return datetime.now(TZ)


def fmt_time(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S") if dt else ""


def normalize_answer(text):
    """Ignore case, spaces, hyphens, underscores, and punctuation."""
    return re.sub(r"[^a-z0-9]", "", (text or "").lower())


def answer_is_correct(user_answer, item):
    accepted = [item["keyword"], *item["aliases"]]
    accepted_normalized = {normalize_answer(x) for x in accepted}
    return normalize_answer(user_answer) in accepted_normalized


def valid_english_name(name):
    name = (name or "").strip()
    return bool(re.fullmatch(r"[A-Za-z][A-Za-z .'-]*", name))


# ============================================================
# SESSION STATE
# ============================================================

DEFAULT_STATE = {
    "active_set": 1,
    "selected_unknown": [],
    "card_index": 0,
    "practice_ready": False,
    "quiz_started": False,
    "quiz_submitted": False,
    "quiz_order": [],
    "quiz_start": None,
    "quiz_end": None,
    "student_name": "",
    "quiz_results": [],
    "reading_index": 0,
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


def clear_dynamic_widgets():
    for key in list(st.session_state.keys()):
        if key.startswith("unknown_") or key.startswith("quiz_answer_"):
            del st.session_state[key]


def select_all_practice_words(set_no):
    """Select all 20 practice checkboxes for the current set."""
    for i in range(SET_SIZE):
        st.session_state[f"unknown_{set_no}_{i}"] = True


def clear_all_practice_words(set_no):
    """Clear all 20 practice checkboxes for the current set."""
    for i in range(SET_SIZE):
        st.session_state[f"unknown_{set_no}_{i}"] = False


def reset_learning_state(new_set=None):
    clear_dynamic_widgets()

    if new_set is not None:
        st.session_state.active_set = new_set

    st.session_state.selected_unknown = []
    st.session_state.card_index = 0
    st.session_state.reading_index = 0
    st.session_state.practice_ready = False
    st.session_state.quiz_started = False
    st.session_state.quiz_submitted = False
    st.session_state.quiz_order = []
    st.session_state.quiz_start = None
    st.session_state.quiz_end = None
    st.session_state.student_name = ""
    st.session_state.quiz_results = []



# ============================================================
# GTTS AUDIO
# ============================================================

@st.cache_data(show_spinner=False)
def make_gtts_audio(keyword, explanation):
    """
    Create one MP3 clip with gTTS.
    The keyword is spoken first, followed by the explanation.
    """

    text_to_speak = f"{keyword}. {explanation}"

    audio_buffer = io.BytesIO()

    tts = gTTS(
        text=text_to_speak,
        lang="en",
        tld="com",
        slow=False,
    )

    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    return audio_buffer.getvalue()


# ============================================================
# PDF REPORT
# ============================================================

def shorten_text(text, max_length=38):
    text = str(text)
    if len(text) <= max_length:
        return text
    return text[: max_length - 1] + "…"


def build_pdf_report(name, set_no, start_time, end_time, results):
    """Create a one-page landscape A4 quiz report."""
    buffer = io.BytesIO()
    page_size = landscape(A4)
    width, height = page_size
    c = canvas.Canvas(buffer, pagesize=page_size)

    left = 26
    top = height - 26

    c.setFont("Helvetica-Bold", 14)
    c.drawString(left, top, "Digital Literacy Quiz Report")

    meta_y = top - 20
    c.setFont("Helvetica", 8)
    c.drawString(left, meta_y, f"Name: {name}")
    c.drawString(left + 180, meta_y, f"Set: {set_no}")
    c.drawString(left + 245, meta_y, f"Start: {fmt_time(start_time)}")
    c.drawString(left + 465, meta_y, f"End: {fmt_time(end_time)}")

    score = sum(1 for r in results if r["correct"])
    percentage = score / len(results) * 100 if results else 0

    table_data = [["No.", "Your Answer", "Correct Answer", "Result"]]

    for r in results:
        table_data.append(
            [
                str(r["no"]),
                shorten_text(r["user_answer"] or "—", 40),
                shorten_text(r["correct_answer"], 32),
                "Correct" if r["correct"] else "Incorrect",
            ]
        )

    table = Table(
        table_data,
        colWidths=[38, 310, 250, 92],
        rowHeights=[17] + [16] * len(results),
    )

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EEEEEE")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 7.4),
                ("ALIGN", (0, 0), (0, -1), "CENTER"),
                ("ALIGN", (-1, 1), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BBBBBB")),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )

    _, table_height = table.wrap(width - 2 * left, height)
    table_y = meta_y - 10 - table_height
    table.drawOn(c, left, table_y)

    c.setFont("Helvetica-Bold", 10)
    c.drawString(
        left,
        table_y - 20,
        f"Total Score: {score}/{len(results)} ({percentage:.0f}%)",
    )

    c.setFont("Helvetica-Oblique", 7)
    c.drawString(
        left + 240,
        table_y - 20,
        "Capitalization, spaces, hyphens, and punctuation are ignored in grading.",
    )

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.getvalue()


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
    <style>
    .flashcard {
        border: 1px solid #d8d8d8;
        border-radius: 16px;
        padding: 35px 30px;
        min-height: 180px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        background: #fafafa;
        margin-top: 10px;
        margin-bottom: 16px;
    }

    .flashcard-term {
        font-size: 2rem;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.title("Digital Literacy & App Development Flashcards")
st.caption("100 core terms · 5 sets · 20 terms per set")


# ============================================================
# SET SELECTION
# ============================================================

selected_set = st.selectbox(
    "Choose a 20-word set",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: SET_LABELS[x],
    index=st.session_state.active_set - 1,
    disabled=st.session_state.quiz_started,
)

if selected_set != st.session_state.active_set:
    reset_learning_state(selected_set)
    st.rerun()

items = get_set_items(st.session_state.active_set)


# ============================================================
# TABS
# ============================================================

tab_list, tab_practice, tab_reading, tab_quiz, tab_result = st.tabs(
    ["1. Word List", "2. Practice", "3. Reading with the keyword", "4. Quiz", "5. Result"]
)


# ============================================================
# TAB 1 — WORD LIST
# ============================================================

with tab_list:
    st.subheader(SET_LABELS[st.session_state.active_set])
    st.write("Review the 20 keywords before starting your practice.")

    rows = [
        {
            "No.": item["number"],
            "Keyword": item["keyword"],
        }
        for item in items
    ]

    st.dataframe(
        rows,
        hide_index=True,
        use_container_width=True,
    )

    with st.expander("View all 100 keywords"):
        for s in range(1, 6):
            st.markdown(f"**{SET_LABELS[s]}**")
            words = [x["keyword"] for x in get_set_items(s)]
            st.write(" · ".join(words))

    st.download_button(
        "Download vocabulary data (.csv)",
        data=CSV_BYTES,
        file_name="terms_data_with_context.csv",
        mime="text/csv",
    )


# ============================================================
# TAB 2 — PRACTICE
# ============================================================

with tab_practice:
    st.subheader("Select what you do not know")
    st.write(
        "Choose only the words you do not know well. "
        "You will practice those words before taking the final quiz."
    )

    select_col, clear_col = st.columns(2)

    with select_col:
        st.button(
            "Select all 20",
            on_click=select_all_practice_words,
            args=(st.session_state.active_set,),
            use_container_width=True,
        )

    with clear_col:
        st.button(
            "Clear all",
            on_click=clear_all_practice_words,
            args=(st.session_state.active_set,),
            use_container_width=True,
        )

    with st.form(f"unknown_form_{st.session_state.active_set}"):
        col1, col2 = st.columns(2)
        selected_terms = []

        for i, item in enumerate(items):
            column = col1 if i < 10 else col2

            with column:
                checked = st.checkbox(
                    item["keyword"],
                    key=f"unknown_{st.session_state.active_set}_{i}",
                )

                if checked:
                    selected_terms.append(item["keyword"])

        apply_selection = st.form_submit_button(
            "Study selected words",
            use_container_width=True,
        )

    if apply_selection:
        st.session_state.selected_unknown = selected_terms
        st.session_state.card_index = 0
        st.session_state.practice_ready = False
        st.session_state.quiz_started = False
        st.session_state.quiz_submitted = False
        st.session_state.quiz_results = []

    selected_items = [
        item
        for item in items
        if item["keyword"] in st.session_state.selected_unknown
    ]

    if selected_items:
        st.divider()
        st.write(f"Selected for practice: **{len(selected_items)} word(s)**")

        idx = min(st.session_state.card_index, len(selected_items) - 1)
        st.session_state.card_index = idx
        item = selected_items[idx]

        st.markdown(
            f"""
            <div class="flashcard">
                <div class="flashcard-term">{item['keyword']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        try:
            audio_bytes = make_gtts_audio(
                item["keyword"],
                item["explanation"],
            )

            st.audio(
                audio_bytes,
                format="audio/mp3",
            )

        except Exception as e:
            st.warning("Audio is temporarily unavailable.")
            st.caption(str(e))

        st.caption(f"Card {idx + 1} of {len(selected_items)}")

        with st.expander("Show explanation"):
            st.write(item["explanation"])

            if item["aliases"]:
                st.caption("Also called / accepted: " + ", ".join(item["aliases"]))

        previous_col, next_col = st.columns(2)

        with previous_col:
            if st.button(
                "← Previous",
                disabled=(idx == 0),
                use_container_width=True,
            ):
                st.session_state.card_index -= 1
                st.rerun()

        with next_col:
            if st.button(
                "Next →",
                disabled=(idx == len(selected_items) - 1),
                use_container_width=True,
            ):
                st.session_state.card_index += 1
                st.rerun()

        st.write("")

        if st.button(
            "I’m ready for the quiz",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.practice_ready = True
            st.success("Quiz unlocked. Open the Quiz tab.")

    else:
        st.info(
            "No words are currently selected. "
            "If you already know all 20 words, you can proceed directly to the quiz."
        )

        if st.button("I know all 20 · Unlock quiz", type="primary"):
            st.session_state.practice_ready = True
            st.success("Quiz unlocked. Open the Quiz tab.")


# ============================================================
# TAB 3 — READING WITH THE KEYWORD
# ============================================================


def render_reading_context(passage, keyword, highlight=False):
    """Keep the passage readable; optionally highlight the actual keyword."""
    safe_passage = html.escape(passage)
    if highlight and keyword:
        # Match the term as a whole word or phrase (case insensitive).
        pattern = re.compile(r"(?<!\w)" + re.escape(keyword) + r"(?!\w)", re.I)
        safe_passage = pattern.sub(
            lambda match: "<mark>" + match.group(0) + "</mark>",
            safe_passage,
        )
    safe_passage = safe_passage.replace("\n", "<br>")
    st.markdown(
        '<div style="line-height:1.85;font-size:1.13rem;max-width:900px;'
        'padding:20px;border:1px solid #ddd;border-radius:12px;">'
        + safe_passage + "</div>",
        unsafe_allow_html=True,
    )


with tab_reading:
    st.subheader("Reading with the keyword")
    st.write(
        "Read each passage and use the surrounding context to infer the "
        "meaning of the keyword. You can highlight the word or reveal "
        "its explanation after reading."
    )
    if not items:
        st.info("No reading passages are available for this set.")
    else:
        reading_options = list(range(len(items)))
        reading_index = st.selectbox(
            "Select a passage",
            options=reading_options,
            index=min(st.session_state.reading_index, len(items) - 1),
            format_func=lambda idx: f"{items[idx]['number']}. {items[idx]['keyword']}",
            key=f"reading_choice_{st.session_state.active_set}",
        )
        st.session_state.reading_index = reading_index
        selected_reading = items[reading_index]
        st.caption(f"Passage {reading_index + 1} of {len(items)} · "
                   f"{SET_LABELS[st.session_state.active_set]}")

        highlight = st.checkbox(
            "Highlight the keyword",
            value=False,
            key=f"reading_highlight_{st.session_state.active_set}",
        )
        if selected_reading["context"]:
            render_reading_context(
                selected_reading["context"], selected_reading["keyword"], highlight
            )
        else:
            st.warning("No context paragraph was provided for this keyword.")

        with st.expander("Show meaning / explanation", expanded=False):
            st.write(selected_reading["explanation"])
            if selected_reading["aliases"]:
                st.caption("Also accepted: " + ", ".join(selected_reading["aliases"]))

        # The selector above also supports direct movement to any passage.
        st.caption("Choose another keyword above to read the next passage.")


# ============================================================
# TAB 4 — QUIZ
# ============================================================

with tab_quiz:
    st.subheader("Final Quiz · 20 Questions")
    st.write(
        "Read each description and type the correct keyword. "
        "Each word appears exactly once."
    )

    if (
        not st.session_state.practice_ready
        and not st.session_state.quiz_started
        and not st.session_state.quiz_submitted
    ):
        st.warning("Complete the Practice section before starting the quiz.")

    elif (
        not st.session_state.quiz_started
        and not st.session_state.quiz_submitted
    ):
        name = st.text_input(
            "Name (English only)",
            value=st.session_state.student_name,
            placeholder="e.g., Minji Kim",
        )

        st.caption(
            "Use English letters only. Spaces, hyphens, apostrophes, and periods are allowed."
        )

        if st.button("Start Quiz", type="primary"):
            if not valid_english_name(name):
                st.error("Please enter your name using English letters only.")
            else:
                st.session_state.student_name = name.strip()

                order = list(range(len(items)))
                random.shuffle(order)
                st.session_state.quiz_order = order

                st.session_state.quiz_start = now_kst()
                st.session_state.quiz_end = None
                st.session_state.quiz_started = True
                st.session_state.quiz_submitted = False
                st.session_state.quiz_results = []

                for key in list(st.session_state.keys()):
                    if key.startswith("quiz_answer_"):
                        del st.session_state[key]

                st.rerun()

    elif st.session_state.quiz_started:
        st.caption(
            f"Name: {st.session_state.student_name} · "
            f"Started: {fmt_time(st.session_state.quiz_start)}"
        )

        with st.form(f"quiz_form_{st.session_state.active_set}"):
            current_answers = []

            for q_no, item_idx in enumerate(
                st.session_state.quiz_order,
                start=1,
            ):
                item = items[item_idx]

                st.markdown(f"**{q_no}. {item['question']}**")

                answer = st.text_input(
                    "Your answer",
                    key=f"quiz_answer_{st.session_state.active_set}_{item_idx}",
                    max_chars=60,
                    placeholder="Type the keyword",
                    label_visibility="collapsed",
                )

                current_answers.append((q_no, item_idx, answer))

            submitted = st.form_submit_button(
                "Submit Quiz",
                type="primary",
                use_container_width=True,
            )

        if submitted:
            blank_questions = [
                q_no
                for q_no, _, answer in current_answers
                if not answer.strip()
            ]

            if blank_questions:
                st.error("Please answer all 20 questions before submitting.")
            else:
                results = []

                for q_no, item_idx, answer in current_answers:
                    item = items[item_idx]

                    results.append(
                        {
                            "no": q_no,
                            "user_answer": answer.strip(),
                            "correct_answer": item["keyword"],
                            "correct": answer_is_correct(answer, item),
                        }
                    )

                st.session_state.quiz_results = results
                st.session_state.quiz_end = now_kst()
                st.session_state.quiz_started = False
                st.session_state.quiz_submitted = True
                st.rerun()

    else:
        score = sum(
            1
            for r in st.session_state.quiz_results
            if r["correct"]
        )

        st.success(f"Quiz completed: {score}/{SET_SIZE}")
        st.write(
            "Open the **Result** tab to review your answers "
            "and download your PDF report."
        )


# ============================================================
# TAB 5 — RESULT
# ============================================================

with tab_result:
    st.subheader("Quiz Result")

    if not st.session_state.quiz_submitted:
        st.info("Complete the quiz to see your result.")
    else:
        results = st.session_state.quiz_results
        score = sum(1 for r in results if r["correct"])
        percentage = score / len(results) * 100

        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Score", f"{score}/{SET_SIZE}")
        metric2.metric("Percentage", f"{percentage:.0f}%")
        metric3.metric("Set", str(st.session_state.active_set))

        st.write(f"**Name:** {st.session_state.student_name}")
        st.write(f"**Start:** {fmt_time(st.session_state.quiz_start)}")
        st.write(f"**End:** {fmt_time(st.session_state.quiz_end)}")

        result_rows = []

        for r in results:
            result_rows.append(
                {
                    "No.": r["no"],
                    "Your answer": r["user_answer"],
                    "Correct answer": r["correct_answer"],
                    "Result": "✓" if r["correct"] else "✗",
                }
            )

        st.dataframe(
            result_rows,
            hide_index=True,
            use_container_width=True,
        )

        pdf_bytes = build_pdf_report(
            st.session_state.student_name,
            st.session_state.active_set,
            st.session_state.quiz_start,
            st.session_state.quiz_end,
            results,
        )

        safe_name = re.sub(
            r"[^A-Za-z0-9_-]",
            "_",
            st.session_state.student_name.strip(),
        )

        st.download_button(
            "Download one-page PDF report",
            data=pdf_bytes,
            file_name=(
                f"digital_literacy_quiz_{safe_name}_"
                f"set{st.session_state.active_set}.pdf"
            ),
            mime="application/pdf",
            type="primary",
            use_container_width=True,
        )

        st.write("")

        if st.button("Reset this set"):
            reset_learning_state(st.session_state.active_set)
            st.rerun()
