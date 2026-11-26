}

# ==================================================
# AI Movie Sample (YouTube)
# ==================================================
AI_MOVIE_URL = "https://youtu.be/29cv0iC8hqM"  # Paste your YouTube video URL here.

# ==================================================
# Main Page
# ==================================================
st.title("📘 Digital Literacy and English Education")
st.caption("Fall 2026 | Final Group Project")

intro, guideline, samples, ai_movie = st.tabs([
    "📘 Introduction",
    "📋 Guideline",
    "💡 Samples",
    "🎬 AI Movie",
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
    import requests

    st.markdown("## 📚 Digital Textbook Resources")
    st.write("Choose either Lesson 3 or Lesson 5.")

    cols = st.columns(2)
    for col, (lesson, url) in zip(cols, LESSON_URLS.items()):
        with col:
            if url:
                st.link_button(
                    f"📖 {lesson} – Digital Textbook",
                    url,
                    use_container_width=True
                )
            else:
                st.caption(f"📖 {lesson} (Coming soon)")

    st.divider()

    GUIDELINE_URL = (
        "https://raw.githubusercontent.com/MK316/"
        "Digital-Literacy-Class/main/data/"
        "final_project_guidelines.md"
    )

    @st.cache_data(ttl=60)
    def load_guidelines(url):
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.content.decode("utf-8")

    try:
        st.markdown(load_guidelines(GUIDELINE_URL))
    except (requests.RequestException, UnicodeError):
        st.warning("Unable to load the project guidelines.")
        st.link_button(
            "📋 View Guidelines on GitHub",
            "https://github.com/MK316/Digital-Literacy-Class/"
            "blob/main/data/final_project_guidelines.md"
        )


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


# ==================================================
# AI Movie
# ==================================================
with ai_movie:
    st.markdown("## 🎬 AI Movie Sample")
    st.write("This sample short film demonstrates how generative AI can be used to create video content for English language learning and teaching.")
    st.markdown("[Manual online](https://mk316.github.io/Lessons/lessons/ai_movie/AI_Movie_Guide.html?v=8&utm_source=chatgpt.com)")
    st.markdown("If the link fails to open: [manual html download](https://drive.google.com/file/d/1vsA1OHzNys4l_AysYywN_4KuT2f5mVAS/view?usp=sharing)")
    st.caption("The file to download is more user-friendly")
    if AI_MOVIE_URL.strip():
        st.video(AI_MOVIE_URL)
    else:
        st.info("The sample video will be available soon.")
