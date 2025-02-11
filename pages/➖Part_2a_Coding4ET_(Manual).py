import streamlit as st
import streamlit.components.v1 as components
import requests

def main():
#    st.title('Coding4ET Tutorials')

    tabs = st.tabs(["Table of contents", "Acknowledgment", "Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4", "Lesson 5", "Advncd. manual"])

    # Manual tab content
    with tabs[0]:
        st.subheader("")
        readme_url = 'https://github.com/MK316/Coding4ET/blob/main/README.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    
    with tabs[1]:
        st.subheader("")
        readme_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/overview.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    with tabs[2]:
        st.subheader("")
        readme_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/Lesson01.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    with tabs[3]:
        st.subheader("")
        readme_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/Lesson02.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    with tabs[4]:
        st.subheader("Lesson 3 Videos")
        handle_lesson_3_videos()  # Display Lesson 3 video buttons

    with tabs[5]:
        st.subheader("")
        readme_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/Lesson04.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    with tabs[6]:
        st.subheader("")
        readme_url = 'https://github.com/MK316/Coding4ET/blob/main/Lessons/Lesson05.md'
        readme_content = fetch_github_readme(readme_url)
        st.markdown(readme_content, unsafe_allow_html=True)

    with tabs[7]:
        st.subheader("Practical Python Manual by David Beazley")
        st.caption("This manual is suitable for those who want to further study the basics of Python coding.")
        st.caption("Github source: https://github.com/dabeaz-course/practical-python.")
        st.write("Click below to go to the manual page.")
        readme_url = 'https://wikidocs.net/book/4606'
        link_text = f"📗 View the manual [here]({readme_url})"
        st.markdown(link_text, unsafe_allow_html=True)
    
def handle_lesson_3_videos():
    video_links = {
        'Lesson 3.1': 'https://www.youtube.com/embed/uigxMFBR0Wg',
        'Lesson 3.2': 'https://www.youtube.com/embed/gPIe1Tgie1Q',
        'Lesson 3.3': 'https://www.youtube.com/embed/ofhRZ6k3Ryw',
        'Lesson 3.4': 'https://www.youtube.com/embed/vSsClackic4'
    }
    for lesson in video_links:
        if st.button(lesson):
            components.html(get_iframe(video_links[lesson]), height=300)

def get_iframe(video_url):
    return f"<iframe width='400' height='300' src='{video_url}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"

def fetch_github_readme(url):
    response = requests.get(url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/'))
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to load README. [View on GitHub]({url})"

if __name__ == "__main__":
    main()
