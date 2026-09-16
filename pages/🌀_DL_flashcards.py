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
# pages/
# ├── 🌀_DL_flashcards.py
# └── terms_data.md
# ============================================================

APP_DIR = Path(__file__).resolve().parent
DATA_FILE = APP_DIR / "terms_data.md"


if not DATA_FILE.is_file():

    st.error("terms_data.md was not found.")

    st.write("Current app file:")
    st.code(str(Path(__file__).resolve()))

    st.write("Expected data file:")
    st.code(str(DATA_FILE))

    st.write("Files visible in this directory:")

    try:
        filenames = sorted(
            p.name for p in APP_DIR.iterdir()
        )
        st.code("\n".join(filenames))

    except Exception as e:
        st.code(str(e))

    st.stop()


# ============================================================
# LOAD MARKDOWN DATA
# ============================================================

@st.cache_data
def load_terms_from_markdown(path_str):

    text = Path(path_str).read_text(
        encoding="utf-8"
    )

    # Normalize Windows / Mac line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")


    # --------------------------------------------------------
    # Each entry begins with:
    #
    # ### 001. Hardware
    #
    # and ends immediately before the next ### heading.
    # --------------------------------------------------------

    entry_pattern = re.compile(
        r"^###\s*(\d+)\.\s*(.+?)\s*$"
        r"(.*?)"
        r"(?=^###\s*\d+\.|\Z)",
        re.MULTILINE | re.DOTALL,
    )


    terms = []


    for entry in entry_pattern.finditer(text):

        number = int(entry.group(1))
        keyword = entry.group(2).strip()

        body = entry.group(3)


        # ----------------------------------------------------
        # Explanation
        # ----------------------------------------------------

        explanation_match = re.search(
            r"\*\*Explanation:\*\*\s*"
            r"(.*?)"
            r"(?=\n\s*\*\*Quiz prompt:\*\*)",
            body,
            re.DOTALL,
        )


        # ----------------------------------------------------
        # Quiz prompt
        # ----------------------------------------------------

        question_match = re.search(
            r"\*\*Quiz prompt:\*\*\s*"
            r"(.*?)"
            r"(?=\n\s*\*\*Accepted answers:\*\*)",
            body,
            re.DOTALL,
        )


        # ----------------------------------------------------
        # Accepted answers
        # ----------------------------------------------------

        aliases_match = re.search(
            r"\*\*Accepted answers:\*\*\s*"
            r"(.*?)"
            r"(?=\n\s*---|\Z)",
            body,
            re.DOTALL,
        )


        if not explanation_match:
            continue

        if not question_match:
            continue


        explanation = re.sub(
            r"\s+",
            " ",
            explanation_match.group(1).strip(),
        )


        question = re.sub(
            r"\s+",
            " ",
            question_match.group(1).strip(),
        )


        aliases = []


        if aliases_match:

            aliases_raw = aliases_match.group(1).strip()

            if aliases_raw not in {
                "",
                "-",
                "—",
                "None",
                "none",
                "N/A",
                "n/a",
            }:

                aliases = [
                    x.strip()
                    for x in aliases_raw.split(";")
                    if x.strip()
                ]


        terms.append(
            {
                "number": number,
                "keyword": keyword,
                "explanation": explanation,
                "question": question,
                "aliases": aliases,
            }
        )


    terms.sort(
        key=lambda x: x["number"]
    )

    return terms


TERMS = load_terms_from_markdown(
    str(DATA_FILE)
)


# ============================================================
# DATA CHECK
# ============================================================

if len(TERMS) != TOTAL_TERMS:

    st.error(
        f"terms_data.md was found, but "
        f"{len(TERMS)} entries were loaded. "
        f"Expected {TOTAL_TERMS}."
    )

    if TERMS:

        st.write("Entries successfully loaded:")

        for item in TERMS:
            st.write(
                f'{item["number"]}. '
                f'{item["keyword"]}'
            )

    st.stop()


# ============================================================
# SETS
# ============================================================

SET_LABELS = {
    1: "Set 1 · Digital Foundations",
    2: "Set 2 · Data & Coding Basics",
    3: "Set 3 · App Development & Git",
    4: "Set 4 · Platforms & AI Basics",
    5: "Set 5 · AI, Deployment & APIs",
}


def get_set_items(set_no):

    start = (
        set_no - 1
    ) * SET_SIZE

    end = start + SET_SIZE

    return TERMS[start:end]


# ============================================================
# TIME
# ============================================================

def now_kst():
    return datetime.now(TZ)


def fmt_time(dt):

    if dt is None:
        return ""

    return dt.strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# ============================================================
# ANSWER CHECKING
# ============================================================

def normalize_answer(text):

    """
    Ignore:
    - capitalization
    - spaces
    - hyphens
    - underscores
    - punctuation

    Example:
    Hugging Face == huggingface
    """

    return re.sub(
        r"[^a-z0-9]",
        "",
        (text or "").lower(),
    )


def answer_is_correct(
    user_answer,
    item,
):

    accepted = [
        item["keyword"],
        *item["aliases"],
    ]

    accepted_normalized = {
        normalize_answer(x)
        for x in accepted
    }

    return (
        normalize_answer(user_answer)
        in accepted_normalized
    )


# ============================================================
# NAME CHECK
# ============================================================

def valid_english_name(name):

    name = (
        name or ""
    ).strip()

    return bool(
        re.fullmatch(
            r"[A-Za-z][A-Za-z .'-]*",
            name,
        )
    )


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

    for key in list(
        st.session_state.keys()
    ):

        if (
            key.startswith("unknown_")
            or key.startswith("quiz_answer_")
        ):
            del st.session_state[key]


def reset_learning_state(
    new_set=None,
):

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
# PDF REPORT
# ============================================================

def shorten_text(
    text,
    max_length=38,
):

    text = str(text)

    if len(text) <= max_length:
        return text

    return (
        text[: max_length - 1]
        + "…"
    )


def build_pdf_report(
    name,
    set_no,
    start_time,
    end_time,
    results,
):

    buffer = io.BytesIO()

    page_size = landscape(A4)

    width, height = page_size

    c = canvas.Canvas(
        buffer,
        pagesize=page_size,
    )


    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    left = 26
    top = height - 26


    c.setFont(
        "Helvetica-Bold",
        14,
    )

    c.drawString(
        left,
        top,
        "Digital Literacy Quiz Report",
    )


    # --------------------------------------------------------
    # Student information
    # --------------------------------------------------------

    meta_y = top - 20

    c.setFont(
        "Helvetica",
        8,
    )

    c.drawString(
        left,
        meta_y,
        f"Name: {name}",
    )

    c.drawString(
        left + 180,
        meta_y,
        f"Set: {set_no}",
    )

    c.drawString(
        left + 245,
        meta_y,
        f"Start: {fmt_time(start_time)}",
    )

    c.drawString(
        left + 465,
        meta_y,
        f"End: {fmt_time(end_time)}",
    )


    # --------------------------------------------------------
    # Score
    # --------------------------------------------------------

    score = sum(
        1
        for r in results
        if r["correct"]
    )

    percentage = (
        score
        / len(results)
        * 100
    )


    # --------------------------------------------------------
    # Table
    # --------------------------------------------------------

    table_data = [
        [
            "No.",
            "Your Answer",
            "Correct Answer",
            "Result",
        ]
    ]


    for r in results:

        table_data.append(
            [
                str(r["no"]),

                shorten_text(
                    r["user_answer"]
                    or "—",
                    40,
                ),

                shorten_text(
                    r["correct_answer"],
                    32,
                ),

                (
                    "Correct"
                    if r["correct"]
                    else "Incorrect"
                ),
            ]
        )


    table = Table(
        table_data,

        colWidths=[
            38,
            310,
            250,
            92,
        ],

        rowHeights=[
            17
        ]
        + [
            16
        ] * len(results),
    )


    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        "#EEEEEE"
                    ),
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),

                (
                    "FONTNAME",
                    (0, 1),
                    (-1, -1),
                    "Helvetica",
                ),

                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    7.4,
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (0, -1),
                    "CENTER",
                ),

                (
                    "ALIGN",
                    (-1, 1),
                    (-1, -1),
                    "CENTER",
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    colors.HexColor(
                        "#BBBBBB"
                    ),
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
            ]
        )
    )


    _, table_height = table.wrap(
        width - 2 * left,
        height,
    )


    table_y = (
        meta_y
        - 10
        - table_height
    )


    table.drawOn(
        c,
        left,
        table_y,
    )


    # --------------------------------------------------------
    # Final score
    # --------------------------------------------------------

    c.setFont(
        "Helvetica-Bold",
        10,
    )

    c.drawString(
        left,
        table_y - 20,
        (
            f"Total Score: "
            f"{score}/{len(results)} "
            f"({percentage:.0f}%)"
        ),
    )


    c.setFont(
        "Helvetica-Oblique",
        7,
    )

    c.drawString(
        left + 240,
        table_y - 20,
        (
            "Capitalization, spaces, "
            "hyphens, and punctuation "
            "are ignored in grading."
        ),
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
# TITLE
# ============================================================

st.title(
    "Digital Literacy & App Development Flashcards"
)

st.caption(
    "100 core terms · "
    "5 sets · "
    "20 terms per set"
)


# ============================================================
# SET SELECTION
# ============================================================

selected_set = st.selectbox(
    "Choose a 20-word set",
    options=[
        1,
        2,
        3,
        4,
        5,
    ],

    format_func=lambda x: (
        SET_LABELS[x]
    ),

    index=(
        st.session_state.active_set
        - 1
    ),

    disabled=(
        st.session_state.quiz_started
    ),
)


if (
    selected_set
    != st.session_state.active_set
):

    reset_learning_state(
        selected_set
    )

    st.rerun()


items = get_set_items(
    st.session_state.active_set
)


# ============================================================
# TABS
# ============================================================

tab_list, tab_practice, tab_quiz, tab_result = st.tabs(
    [
        "1. Word List",
        "2. Practice",
        "3. Quiz",
        "4. Result",
    ]
)


# ============================================================
# TAB 1
# WORD LIST
# ============================================================

with tab_list:

    st.subheader(
        SET_LABELS[
            st.session_state.active_set
        ]
    )

    st.write(
        "Review the 20 keywords "
        "before starting your practice."
    )


    rows = []

    for item in items:

        rows.append(
            {
                "No.": item["number"],
                "Keyword": item["keyword"],
            }
        )


    st.dataframe(
        rows,
        hide_index=True,
        use_container_width=True,
    )


    # --------------------------------------------------------
    # All 100 words
    # --------------------------------------------------------

    with st.expander(
        "View all 100 keywords"
    ):

        for s in range(
            1,
            6,
        ):

            st.markdown(
                f"**{SET_LABELS[s]}**"
            )

            words = [
                x["keyword"]
                for x
                in get_set_items(s)
            ]

            st.write(
                " · ".join(words)
            )


    # --------------------------------------------------------
    # Markdown source
    # --------------------------------------------------------

    with st.expander(
        "View vocabulary descriptions"
    ):

        st.markdown(
            DATA_FILE.read_text(
                encoding="utf-8"
            )
        )


# ============================================================
# TAB 2
# PRACTICE
# ============================================================

with tab_practice:

    st.subheader(
        "Select what you do not know"
    )

    st.write(
        "Choose only the words "
        "you do not know well. "
        "You will practice those words "
        "before taking the final quiz."
    )


    # --------------------------------------------------------
    # Select unknown words
    # --------------------------------------------------------

    with st.form(
        f"unknown_form_"
        f"{st.session_state.active_set}"
    ):

        col1, col2 = st.columns(2)

        selected_terms = []


        for i, item in enumerate(items):

            column = (
                col1
                if i < 10
                else col2
            )


            with column:

                checked = st.checkbox(
                    item["keyword"],

                    key=(
                        f"unknown_"
                        f"{st.session_state.active_set}_"
                        f"{i}"
                    ),
                )


                if checked:

                    selected_terms.append(
                        item["keyword"]
                    )


        apply_selection = (
            st.form_submit_button(
                "Study selected words",
                use_container_width=True,
            )
        )


    if apply_selection:

        st.session_state.selected_unknown = (
            selected_terms
        )

        st.session_state.card_index = 0

        st.session_state.practice_ready = False

        st.session_state.quiz_started = False
        st.session_state.quiz_submitted = False

        st.session_state.quiz_results = []


    selected_items = [
        item
        for item in items
        if item["keyword"]
        in st.session_state.selected_unknown
    ]


    # --------------------------------------------------------
    # Flashcards
    # --------------------------------------------------------

    if selected_items:

        st.divider()


        st.write(
            f"Selected for practice: "
            f"**{len(selected_items)} word(s)**"
        )


        idx = min(
            st.session_state.card_index,
            len(selected_items) - 1,
        )


        st.session_state.card_index = idx


        item = selected_items[idx]


        st.markdown(
            f"""
            <div class="flashcard">
                <div class="flashcard-term">
                    {item["keyword"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


        st.caption(
            f"Card {idx + 1} "
            f"of {len(selected_items)}"
        )


        with st.expander(
            "Show explanation"
        ):

            st.write(
                item["explanation"]
            )


            if item["aliases"]:

                st.caption(
                    "Also called / accepted: "
                    + ", ".join(
                        item["aliases"]
                    )
                )


        previous_col, next_col = (
            st.columns(2)
        )


        with previous_col:

            if st.button(
                "← Previous",
                disabled=(
                    idx == 0
                ),
                use_container_width=True,
            ):

                st.session_state.card_index -= 1

                st.rerun()


        with next_col:

            if st.button(
                "Next →",
                disabled=(
                    idx
                    == len(selected_items) - 1
                ),
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

            st.success(
                "Quiz unlocked. "
                "Open the Quiz tab."
            )


    # --------------------------------------------------------
    # No unknown words
    # --------------------------------------------------------

    else:

        st.info(
            "No words are currently selected. "
            "If you already know all 20 words, "
            "you can proceed directly to the quiz."
        )


        if st.button(
            "I know all 20 · Unlock quiz",
            type="primary",
        ):

            st.session_state.practice_ready = True

            st.success(
                "Quiz unlocked. "
                "Open the Quiz tab."
            )


# ============================================================
# TAB 3
# QUIZ
# ============================================================

with tab_quiz:

    st.subheader(
        "Final Quiz · 20 Questions"
    )

    st.write(
        "Read each description and "
        "type the correct keyword. "
        "Each word appears exactly once."
    )


    # --------------------------------------------------------
    # Quiz locked
    # --------------------------------------------------------

    if (
        not st.session_state.practice_ready
        and not st.session_state.quiz_started
        and not st.session_state.quiz_submitted
    ):

        st.warning(
            "Complete the Practice section "
            "before starting the quiz."
        )


    # --------------------------------------------------------
    # Start screen
    # --------------------------------------------------------

    elif (
        not st.session_state.quiz_started
        and not st.session_state.quiz_submitted
    ):

        name = st.text_input(
            "Name (English only)",
            value=(
                st.session_state.student_name
            ),
            placeholder="e.g., Minji Kim",
        )


        st.caption(
            "Use English letters only. "
            "Spaces, hyphens, apostrophes, "
            "and periods are allowed."
        )


        if st.button(
            "Start Quiz",
            type="primary",
        ):

            if not valid_english_name(name):

                st.error(
                    "Please enter your name "
                    "using English letters only."
                )


            else:

                st.session_state.student_name = (
                    name.strip()
                )


                order = list(
                    range(
                        len(items)
                    )
                )

                random.shuffle(order)


                st.session_state.quiz_order = (
                    order
                )


                st.session_state.quiz_start = (
                    now_kst()
                )

                st.session_state.quiz_end = None


                st.session_state.quiz_started = True
                st.session_state.quiz_submitted = False

                st.session_state.quiz_results = []


                # Remove old answers
                for key in list(
                    st.session_state.keys()
                ):

                    if key.startswith(
                        "quiz_answer_"
                    ):

                        del st.session_state[key]


                st.rerun()


    # --------------------------------------------------------
    # Quiz running
    # --------------------------------------------------------

    elif st.session_state.quiz_started:

        st.caption(
            f"Name: "
            f"{st.session_state.student_name}"
            f" · Started: "
            f"{fmt_time(st.session_state.quiz_start)}"
        )


        with st.form(
            f"quiz_form_"
            f"{st.session_state.active_set}"
        ):

            current_answers = []


            for q_no, item_idx in enumerate(
                st.session_state.quiz_order,
                start=1,
            ):

                item = items[item_idx]


                st.markdown(
                    f"**{q_no}. "
                    f'{item["question"]}**'
                )


                answer = st.text_input(
                    "Your answer",

                    key=(
                        f"quiz_answer_"
                        f"{st.session_state.active_set}_"
                        f"{item_idx}"
                    ),

                    max_chars=60,

                    placeholder=(
                        "Type the keyword"
                    ),

                    label_visibility="collapsed",
                )


                current_answers.append(
                    (
                        q_no,
                        item_idx,
                        answer,
                    )
                )


            submitted = (
                st.form_submit_button(
                    "Submit Quiz",
                    type="primary",
                    use_container_width=True,
                )
            )


        # ----------------------------------------------------
        # Submit
        # ----------------------------------------------------

        if submitted:

            blank_questions = [
                q_no
                for (
                    q_no,
                    _,
                    answer,
                )
                in current_answers
                if not answer.strip()
            ]


            if blank_questions:

                st.error(
                    "Please answer all 20 "
                    "questions before submitting."
                )


            else:

                results = []


                for (
                    q_no,
                    item_idx,
                    answer,
                ) in current_answers:

                    item = items[item_idx]


                    results.append(
                        {
                            "no": q_no,

                            "user_answer": (
                                answer.strip()
                            ),

                            "correct_answer": (
                                item["keyword"]
                            ),

                            "correct": (
                                answer_is_correct(
                                    answer,
                                    item,
                                )
                            ),
                        }
                    )


                st.session_state.quiz_results = (
                    results
                )


                st.session_state.quiz_end = (
                    now_kst()
                )


                st.session_state.quiz_started = False

                st.session_state.quiz_submitted = True


                st.rerun()


    # --------------------------------------------------------
    # Quiz finished
    # --------------------------------------------------------

    else:

        score = sum(
            1
            for r
            in st.session_state.quiz_results
            if r["correct"]
        )


        st.success(
            f"Quiz completed: "
            f"{score}/{SET_SIZE}"
        )


        st.write(
            "Open the **Result** tab "
            "to review your answers "
            "and download your PDF report."
        )


# ============================================================
# TAB 4
# RESULT
# ============================================================

with tab_result:

    st.subheader(
        "Quiz Result"
    )


    if not st.session_state.quiz_submitted:

        st.info(
            "Complete the quiz "
            "to see your result."
        )


    else:

        results = (
            st.session_state.quiz_results
        )


        score = sum(
            1
            for r in results
            if r["correct"]
        )


        percentage = (
            score
            / len(results)
            * 100
        )


        metric1, metric2, metric3 = (
            st.columns(3)
        )


        metric1.metric(
            "Score",
            f"{score}/{SET_SIZE}",
        )

        metric2.metric(
            "Percentage",
            f"{percentage:.0f}%",
        )

        metric3.metric(
            "Set",
            str(
                st.session_state.active_set
            ),
        )


        st.write(
            f"**Name:** "
            f"{st.session_state.student_name}"
        )


        st.write(
            f"**Start:** "
            f"{fmt_time(st.session_state.quiz_start)}"
        )


        st.write(
            f"**End:** "
            f"{fmt_time(st.session_state.quiz_end)}"
        )


        # ----------------------------------------------------
        # Results table
        # ----------------------------------------------------

        result_rows = []


        for r in results:

            result_rows.append(
                {
                    "No.": r["no"],

                    "Your answer": (
                        r["user_answer"]
                    ),

                    "Correct answer": (
                        r["correct_answer"]
                    ),

                    "Result": (
                        "✓"
                        if r["correct"]
                        else "✗"
                    ),
                }
            )


        st.dataframe(
            result_rows,
            hide_index=True,
            use_container_width=True,
        )


        # ----------------------------------------------------
        # PDF
        # ----------------------------------------------------

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
                f"digital_literacy_quiz_"
                f"{safe_name}_"
                f"set"
                f"{st.session_state.active_set}"
                f".pdf"
            ),

            mime="application/pdf",

            type="primary",

            use_container_width=True,
        )


        st.write("")


        if st.button(
            "Reset this set"
        ):

            reset_learning_state(
                st.session_state.active_set
            )

            st.rerun()
