with guideline:

    import requests

    st.markdown("## 📚 Digital Textbook Resources")
    st.write("Choose either Lesson 3 or Lesson 5.")

    # Digital textbook buttons
    col1, col2 = st.columns(2)

    for col, (lesson, url) in zip(
        [col1, col2], LESSON_URLS.items()
    ):
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

    # Load project guidelines from GitHub
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
        content = load_guidelines(GUIDELINE_URL)
        st.markdown(content)

    except Exception:
        st.warning("Unable to load the project guidelines.")
        st.link_button(
            "📋 View Guidelines on GitHub",
            "https://github.com/MK316/Digital-Literacy-Class/"
            "blob/main/data/final_project_guidelines.md"
        )
