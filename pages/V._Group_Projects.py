
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
tab1, tab2 = st.tabs([
    "📘 Mini-project",
    "👥 TBA",
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




with tab2:

    display_final_project("Group 1")


