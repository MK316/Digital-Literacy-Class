import csv
import html
import io
import random
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import streamlit as st
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
# DATA FILE
#
# repository/
# └── pages/
#     ├── 🌀_DL_flashcards.py
#     └── data/
#         └── terms_data.csv
# ============================================================

APP_DIR = Path(__file__).resolve().parent
DATA_FILE = APP_DIR / "data" / "terms_data.csv"

if not DATA_FILE.is_file():
    st.error("terms_data.csv was not found.")
    st.write("Current app file:")
    st.code(str(Path(__file__).resolve()))
    st.write("Expected CSV file:")
    st.code(str(DATA_FILE))
    st.stop()


# ============================================================
# LOAD CSV DATA
# ============================================================

@st.cache_data
def load_terms_from_csv(path_str):
    """Load vocabulary data from a UTF-8 CSV file."""
    terms = []

    with Path(path_str).open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as f:
        reader = csv.DictReader(f)

        required_columns = {
            "number",
            "set",
            "set_name",
            "keyword",
            "explanation",
            "quiz_prompt",
            "accepted_answers",
        }

        actual_columns = set(reader.fieldnames or [])
        missing_columns = required_columns - actual_columns

        if missing_columns:
            raise ValueError(
                "Missing CSV column(s): "
                + ", ".join(sorted(missing_columns))
            )

        for row in reader:
            aliases_raw = (row.get("accepted_answers") or "").strip()
            aliases = [
                x.strip()
                for x in aliases_raw.split(";")
                if x.strip()
            ]

            terms.append(
                {
                    "number": int(row["number"]),
                    "set": int(row["set"]),
                    "set_name": row["set_name"].strip(),
                    "keyword": row["keyword"].strip(),
                    "explanation": row["explanation"].strip(),
                    "question": row["quiz_prompt"].strip(),
                    "aliases": aliases,
                }
            )

    terms.sort(key=lambda x: x["number"])
    return terms


try:
    TERMS = load_terms_from_csv(str(DATA_FILE))
except Exception as e:
    st.error("The CSV file was found, but it could not be read.")
    st.code(str(e))
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
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


def clear_dynamic_widgets():
    for key in list(st.session_state.keys()):
        if key.startswith("unknown_") or key.startswith("quiz_answer_"):
            del st.session_state[key]


def reset_learning_state(new_set=None):
    clear_dynamic_widgets()

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



# ============================================================
# BROWSER TEXT-TO-SPEECH
# ============================================================

def explanation_audio_button(text, language="en-US", rate=0.92):
    """
    Add a browser-based audio button for the explanation.

    This uses the browser's built-in Web Speech API, so no audio files
    or external TTS service are required.
    """

    safe_text = html.escape(text, quote=True)

    component_html = f"""
    <div style="display:flex; gap:8px; align-items:center; margin:2px 0 8px 0;">
        <button
            id="playButton"
            onclick="playExplanation()"
            style="
                border:1px solid #d0d0d0;
                border-radius:8px;
                background:white;
                padding:7px 12px;
                font-size:14px;
                cursor:pointer;
            "
        >
            🔊 Play explanation
        </button>

        <button
            id="stopButton"
            onclick="stopExplanation()"
            style="
                border:1px solid #d0d0d0;
                border-radius:8px;
                background:white;
                padding:7px 12px;
                font-size:14px;
                cursor:pointer;
            "
        >
            ■ Stop
        </button>
    </div>

    <script>
        const explanationText = `{safe_text}`;

        function chooseEnglishVoice() {{
            const voices = window.speechSynthesis.getVoices();

            const preferred = voices.find(v =>
                v.lang === "{language}" &&
                /Samantha|Google US English|Microsoft|English/i.test(v.name)
            );

            if (preferred) return preferred;

            return voices.find(v => v.lang === "{language}")
                || voices.find(v => v.lang.startsWith("en"))
                || null;
        }}

        function playExplanation() {{
            window.speechSynthesis.cancel();

            const utterance = new SpeechSynthesisUtterance(explanationText);
            utterance.lang = "{language}";
            utterance.rate = {rate};
            utterance.pitch = 1.0;

            const voice = chooseEnglishVoice();
            if (voice) {{
                utterance.voice = voice;
            }}

            window.speechSynthesis.speak(utterance);
        }}

        function stopExplanation() {{
            window.speechSynthesis.cancel();
        }}

        window.speechSynthesis.getVoices();
        if (window.speechSynthesis.onvoiceschanged !== undefined) {{
            window.speechSynthesis.onvoiceschanged = () => {{
                window.speechSynthesis.getVoices();
            }};
        }}
    </script>
    """

    st.components.v1.html(
        component_html,
        height=52,
        scrolling=False,
    )


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

tab_list, tab_practice, tab_quiz, tab_result = st.tabs(
    ["1. Word List", "2. Practice", "3. Quiz", "4. Result"]
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
        data=DATA_FILE.read_bytes(),
        file_name="terms_data.csv",
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

        st.caption(f"Card {idx + 1} of {len(selected_items)}")

        with st.expander("Show explanation"):
            st.write(item["explanation"])

            explanation_audio_button(
                item["explanation"],
                language="en-US",
                rate=0.92,
            )

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
# TAB 3 — QUIZ
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
# TAB 4 — RESULT
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
