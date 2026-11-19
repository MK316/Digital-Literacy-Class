
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import numpy as np


# ==================================================
# Page Configuration
# ==================================================
st.set_page_config(
    page_title="Digital Literacy Project Gallery",
    page_icon="📘",
    layout="wide"
)


# ==================================================
# Mini Projects: Fall 2026 (Groups 1–6)
# ==================================================
MINI_PROJECT_APPS = {
    "Group 1": "https://g1wordgame.streamlit.app/",
    "Group 2": "https://g2miniproject.streamlit.app/",
    "Group 3": "https://baewovocayoyo.streamlit.app/",
    "Group 4": "https://g4-vocaquiz-mini.streamlit.app/",
    "Group 5": "https://g5-vocaquiz-sushivoca3000.streamlit.app/",
    "Group 6": "https://vocab-life.streamlit.app/",
}


# ==================================================
# Final Projects: Spring 2025 (Groups 1–3)
# ==================================================
FINAL_PROJECTS = {
    "Group 1": {
        "app": "https://s25g01.streamlit.app/",
        "qr": (
            "https://github.com/MK316/"
            "Digital-Literacy-Class/raw/main/images/DLG1.png"
        ),
        "github": (
            "https://github.com/KY7437/"
            "G01Final/blob/main/README.md"
        )
    },
    "Group 2": {
        "app": "https://g02final.streamlit.app/",
        "qr": (
            "https://github.com/MK316/"
            "Digital-Literacy-Class/raw/main/images/DLG2.png"
        ),
        "github": (
            "https://github.com/yunju05/"
            "G02Final/blob/main/README.md"
        )
    },
    "Group 3": {
        "app": "https://g03final.streamlit.app/",
        "qr": (
            "https://github.com/MK316/"
            "Digital-Literacy-Class/raw/main/images/DLG3.png"
        ),
        "github": (
            "https://github.com/JW-1211/"
            "G03Final/blob/main/README.md"
        )
    }
}


# ==================================================
# Resources
# ==================================================
FONT_URL = (
    "https://raw.githubusercontent.com/MK316/"
    "Digital-Literacy-Class/main/data/"
    "NanumGothic-Regular.ttf"
)

FONT_PATH = "/tmp/NanumGothic.ttf"

FEEDBACK_URL = (
    "https://raw.githubusercontent.com/MK316/"
    "Digital-Literacy-Class/refs/heads/main/"
    "data/DL-feedback.csv"
)

SWOT_IMAGE_URLS = {
    "Group 1": (
        "https://github.com/MK316/"
        "Digital-Literacy-Class/raw/main/images/Group1.png"
    ),
    "Group 2": (
        "https://github.com/MK316/"
        "Digital-Literacy-Class/raw/main/images/Group2.png"
    ),
    "Group 3": (
        "https://github.com/MK316/"
        "Digital-Literacy-Class/raw/main/images/Group3.png"
    )
}

QUESTION_LABELS = {
    "Q01": "1. Easy to navigate",
    "Q02": "2. Useful for English learning",
    "Q03": "3. Explained classroom use",
    "Q04": "4. Creativity/originality",
    "Q05": "5. Helpful for my teaching",
    "Q06": "6. Adaptable for student levels",
    "Q07": "7. Overall effectiveness"
}


# ==================================================
# Helper Functions
# ==================================================

@st.cache_data(ttl=3600)
def load_feedback_data():
    """Load peer evaluation data from GitHub."""
    return pd.read_csv(FEEDBACK_URL)


@st.cache_resource
def get_korean_font():
    """Download a Korean font when needed."""

    if os.path.exists(FONT_PATH):
        return FONT_PATH

    try:
        response = requests.get(
            FONT_URL,
            timeout=15
        )
        response.raise_for_status()

        with open(FONT_PATH, "wb") as f:
            f.write(response.content)

        return FONT_PATH

    except (requests.RequestException, OSError):
        return None


def display_final_project(group_name):
    """Display an existing Spring 2025 final project."""

    project = FINAL_PROJECTS[group_name]

    st.markdown(
        "### English Classroom with Code-based Applications"
    )

    st.markdown(
        f"### 🌳 {group_name} APP Project"
    )

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### Visit the Application")

        st.link_button(
            "🚀 Visit the Application",
            project["app"],
            type="primary",
            use_container_width=True
        )

        st.caption(
            "Opens in a new browser tab."
        )

    with col2:
        st.image(
            project["qr"],
            caption="Enter via QR",
            width=100
        )

    st.divider()

    st.markdown(
        f"📁 GitHub files to view: "
        f"[README.md]({project['github']})"
    )


def display_mini_projects():
    """Display all six mini-project links."""

    st.markdown("### 🚀 Group Mini Projects")

    st.write("""
    Explore the vocabulary learning apps developed
    by six groups of future English teachers.

    Each group designed and deployed a vocabulary
    learning application using Streamlit.

    **Click a group button to open its application
    in a new browser tab.**
    """)

    # Display six apps in two columns and three rows
    groups = list(MINI_PROJECT_APPS.items())

    for i in range(0, len(groups), 2):

        col1, col2 = st.columns(2)

        for col, (group_name, app_url) in zip(
            [col1, col2],
            groups[i:i + 2]
        ):

            with col:
                st.link_button(
                    f"🔗 {group_name} Mini Project",
                    app_url,
                    use_container_width=True
                )

    st.caption(
        "All six apps are hosted on Streamlit Cloud."
    )


# ==================================================
# Main Page
# ==================================================
st.title("📘 Digital Literacy Project Gallery")

st.caption(
    "Digital Literacy and English Education | "
    "Student-developed English Learning Applications"
)


# ==================================================
# Create Tabs
# ==================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📘 Introduction",
    "👥 Project 1 (G1)",
    "👥 Project 2 (G2)",
    "👥 Project 3 (G3)",
    "⛄ Peer Evaluation (Ready)"
])


# ==================================================
# TAB 1: Introduction
# ==================================================
with tab1:

    st.markdown(
        "### 👋 Welcome to the Project Gallery"
    )

    st.write("""
    This gallery showcases applications developed
    by students in *Digital Literacy and English
    Education*.

    The gallery includes vocabulary learning mini
    projects from Fall 2026 and final group projects
    from Spring 2025.

    Students worked collaboratively to design,
    develop, and deploy code-based applications
    that could be used in English learning and
    teaching practice.
    """)

    st.divider()

    # ----------------------------------------------
    # Fall 2026 Mini Projects
    # ----------------------------------------------
    st.markdown("## 🍂 Fall 2026")

    display_mini_projects()

    st.divider()

    # ----------------------------------------------
    # Spring 2025 Final Projects
    # ----------------------------------------------
    st.markdown("## 🌸 Spring 2025")

    st.markdown("### 🌳 Final Group Projects")

    st.write("""
    The Spring 2025 final projects were developed
    by groups of four to five second-year
    future English teachers over approximately
    one month.

    Their task was to create and demonstrate
    a Streamlit application for English lesson
    planning or classroom teaching.

    Select **Project 1, Project 2, or Project 3**
    from the tabs above to explore each project.
    """)

    st.markdown("""
    **You can:**

    - ✅ Try the application designed for its target learners.
    - ✅ Read the project summary on GitHub.
    - ✅ Access the application using its QR code.
    - ✅ Explore the group's instructional ideas.
    """)


# ==================================================
# TAB 2: Spring 2025 Final Project G1
# ==================================================
with tab2:

    display_final_project("Group 1")


# ==================================================
# TAB 3: Spring 2025 Final Project G2
# ==================================================
with tab3:

    display_final_project("Group 2")


# ==================================================
# TAB 4: Spring 2025 Final Project G3
# ==================================================
with tab4:

    display_final_project("Group 3")


# ==================================================
# TAB 5: Peer Evaluation
# ==================================================
with tab5:

    st.markdown("### ⛄ Peer Evaluation")

    st.write("""
    Peer review summaries of each group's
    application and its classroom use are
    presented below.
    """)

    # ----------------------------------------------
    # Load Feedback
    # ----------------------------------------------
    try:
        df = load_feedback_data()

    except Exception as e:
        st.error(
            f"Unable to load peer evaluation data: {e}"
        )
        st.stop()

    if "Group" not in df.columns:
        st.error(
            "The feedback dataset does not contain "
            "a 'Group' column."
        )
        st.stop()

    group_list = df["Group"].dropna().unique()

    if len(group_list) == 0:
        st.warning(
            "No group feedback is available."
        )
        st.stop()

    selected_group = st.selectbox(
        "🔍 Select a group to view feedback:",
        group_list
    )

    group_df = df[
        df["Group"] == selected_group
    ]

    st.markdown(
        f"## 🧾 Feedback Summary for {selected_group}"
    )

    # ----------------------------------------------
    # SWOT Image
    # ----------------------------------------------
    if selected_group in SWOT_IMAGE_URLS:

        st.image(
            SWOT_IMAGE_URLS[selected_group],
            caption=f"SWOT Analysis: {selected_group}",
            use_container_width=True
        )

    # ----------------------------------------------
    # Quantitative Ratings
    # ----------------------------------------------
    st.markdown(
        "### 📊 Quantitative Ratings (1–10 Scale)"
    )

    rating_columns = [
        f"Q{i:02d}"
        for i in range(1, 8)
    ]

    missing_columns = [
        col for col in rating_columns
        if col not in df.columns
    ]

    if missing_columns:

        st.warning(
            "Missing rating columns: "
            + ", ".join(missing_columns)
        )

    else:

        # Convert ratings to numeric
        for col in rating_columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

        group_df = df[
            df["Group"] == selected_group
        ]

        group_means = group_df[
            rating_columns
        ].mean()

        overall_means = df[
            rating_columns
        ].mean()

        labels = [
            QUESTION_LABELS[q]
            for q in rating_columns
        ]

        x = np.arange(len(labels))
        width = 0.35

        fig, ax = plt.subplots(
            figsize=(9, 4.5)
        )

        bars1 = ax.bar(
            x - width / 2,
            group_means.values,
            width,
            label=selected_group,
            color="skyblue"
        )

        bars2 = ax.bar(
            x + width / 2,
            overall_means.values,
            width,
            label="All Groups (Average)",
            color="yellow"
        )

        # Group value labels
        for bar in bars1:

            height = bar.get_height()

            if np.isfinite(height):

                ax.text(
                    bar.get_x()
                    + bar.get_width() / 2,
                    height + 0.1,
                    f"{height:.1f}",
                    ha="center",
                    va="bottom",
                    fontsize=8
                )

        # Overall value labels
        for bar in bars2:

            height = bar.get_height()

            if np.isfinite(height):

                ax.text(
                    bar.get_x()
                    + bar.get_width() / 2,
                    height + 0.1,
                    f"{height:.1f}",
                    ha="center",
                    va="bottom",
                    fontsize=8,
                    color="gray"
                )

        ax.set_ylabel("Average Rating")

        ax.set_title(
            "Average Ratings: Group vs Overall"
        )

        ax.set_xticks(x)

        ax.set_xticklabels(
            labels,
            rotation=45,
            ha="right"
        )

        ax.set_ylim(0, 10.5)

        ax.legend()

        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    # ----------------------------------------------
    # Word Clouds and Open-ended Comments
    # ----------------------------------------------
    questions = {
        "Q08": "Most impressive aspect",
        "Q09": "Suggestions for improvement"
    }

    for col, title in questions.items():

        st.markdown(
            f"### ☁️ {col}: {title}"
        )

        if col not in group_df.columns:

            st.info(
                "No data available for this question."
            )
            continue

        comments = group_df[col].dropna()

        comments = [
            str(comment)
            for comment in comments
            if str(comment).strip()
        ]

        text_data = " ".join(comments)

        if text_data.strip():

            korean_font = get_korean_font()

            try:

                wc = WordCloud(
                    width=600,
                    height=300,
                    background_color="white",
                    font_path=korean_font
                ).generate(text_data)

                st.image(
                    wc.to_array(),
                    use_container_width=True
                )

            except Exception as e:

                st.warning(
                    f"Could not generate word cloud: {e}"
                )

            # Display all comments
            with st.expander(
                f"📋 Show all comments ({len(comments)})"
            ):

                for comment in comments:

                    st.markdown(
                        f"- {comment}"
                    )

        else:

            st.info(
                "No comments available for this question."
            )
