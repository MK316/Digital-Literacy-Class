
import streamlit as st


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
    "Group 1": "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/Group1.png",
    "Group 2": "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/Group2.png",
    "Group 3": "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/Group3.png",
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
    import pandas as pd
    return pd.read_csv(FEEDBACK_URL)


@st.cache_resource
def get_korean_font():
    """Download a Korean font when needed."""

    import os
    import requests

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
        if st.checkbox("Show QR code", key="show_project_qr"):
            st.image(project["qr"], caption="Enter via QR", width=100)

    st.divider()

    st.markdown(
        f"📁 GitHub files to view: "
        f"[README.md]({project['github']})"
    )


def display_peer_evaluation():
    try:
        import pandas as pd
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud
        import numpy as np
    except ImportError as exc:
        st.error(f"Peer evaluation dependency unavailable: {exc}")
        return

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
        return

    if "Group" not in df.columns:
        st.error(
            "The feedback dataset does not contain "
            "a 'Group' column."
        )
        return

    group_list = df["Group"].dropna().unique()

    if len(group_list) == 0:
        st.warning(
            "No group feedback is available."
        )
        return

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

# ==================================================
# Digital Textbook Links (GitHub Pages)
# ==================================================
LESSON_URLS = {
    "Lesson 3": "https://mk316.github.io/Lessons/lessons/lesson3/Lesson3.html",
    "Lesson 5": "https://mk316.github.io/Lessons/lessons/lesson5/Lesson5.html",
}

# ==================================================
# Main Page
# ==================================================
# st.title("📘 Digital Literacy and English Education")
st.caption("Fall 2026 | Final Group Project")

intro, guideline, samples = st.tabs([
    "📘 Introduction",
    "📋 Guideline",
    "💡 Samples",
])

with intro:
    st.markdown("## 🎯 Fall 2026 Final Project")
    st.markdown("""
Your final group project is to design a **multipage Streamlit app** based
on a lesson plan, integrating digital learning applications and materials
for use in an English classroom.

Choose either **Lesson 3 or Lesson 5** as the basis for your project.
Rather than covering all the textbook content, select **two complementary
areas of English language learning** and build your lesson around them.
Possible combinations include:

- Listening and Speaking
- Vocabulary and Grammar
- Listening and Writing
- Speaking and Writing
- Reading and Writing

Other combinations are welcome. Make sure both selected areas are clearly
reflected in your learning objectives, classroom activities, and app design.
Your app should support a coherent lesson rather than simply present a
collection of unrelated digital activities.

Explore the HTML-based digital textbook resources for Lessons 3 and 5
in the **Guideline** tab.
    """)
    st.info("Focus on meaningful learning and classroom use, not the amount of textbook content covered.")

with guideline:
    st.markdown("## 📋 Project Guidelines")
    st.markdown("### 1. Select a lesson")
    st.write("Choose either Lesson 3 or Lesson 5 as your source material.")
    for lesson, url in LESSON_URLS.items():
        if url:
            st.link_button(f"📖 {lesson} – Digital Textbook", url)
        else:
            st.caption(f"📖 {lesson} – Digital Textbook (Coming soon)")

    st.markdown("""
### 2. Choose two learning focuses
Select two complementary language learning areas and define clear learning objectives.

### 3. Develop a lesson plan
Plan the sequence of classroom activities, including how the teacher and learners will use the digital resources.

### 4. Build a multipage Streamlit app
Organize pages according to your lesson plan. Integrate relevant learning activities, applications, and teaching materials so that both learning focuses are clearly represented.

### 5. Test and deploy
Check the navigation, links, activities, and classroom usability of your app before deploying it to Streamlit Cloud.
    """)

with samples:
    st.markdown("## 💡 Project Samples")
    st.write("Explore previous student projects for ideas about app design and classroom use.")
    category = st.selectbox(
        "Select a project category:",
        ["Choose a project category", "Spring 2025 – Final Projects", "Fall 2026 – Mini Projects"],
        key="sample_category",
    )

    if category == "Choose a project category":
        st.caption("Select a category to explore student projects.")
    elif category == "Fall 2026 – Mini Projects":
        st.write("Vocabulary learning apps developed by six groups of future English teachers.")
        group = st.selectbox("Select a group:", list(MINI_PROJECT_APPS), key="mini_group")
        st.link_button("🚀 Visit the Application", MINI_PROJECT_APPS[group], type="primary")
        st.caption("Opens in a new browser tab.")
    else:
        st.write("Lesson planning and classroom teaching apps developed by three groups of future English teachers.")
        group = st.selectbox("Select a group:", list(FINAL_PROJECTS), key="final_group")
        display_final_project(group)
        st.divider()
        with st.expander("⛄ Peer Evaluation – Spring 2025"):
            if st.checkbox("Load peer evaluation results", key="load_peer_results"):
                display_peer_evaluation()
