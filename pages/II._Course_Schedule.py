import streamlit as st
import requests
import streamlit.components.v1 as components

tabs = st.tabs(["🍐 Weekly", "📙 Github IDs", "🐾 Padlet", "🐳 Group work"])

with tabs[0]:
    # URL of the raw markdown file on GitHub
    markdown_url = "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/main/pages/readme.md"
        
    try:
        response = requests.get(markdown_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        markdown_content = response.text
        st.markdown(markdown_content, unsafe_allow_html=True)
    except requests.exceptions.HTTPError as err:
        st.error(f"Failed to retrieve Markdown content: {err}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

with tabs[1]:
    st.markdown("#### Github IDs to share")
    st.page_link("https://docs.google.com/spreadsheets/d/1z2uYvH-foo3BZ6a4_T80TK7HOQbIJIYIUe5SWOEaGyk/edit?usp=sharing", label="Make your own account and share your IDs here", icon="➡️")
    

with tabs[2]:
    st.header("🐾 Files to share: on Padlet")
    st.markdown("+ [This Padlet](https://padlet.com/mirankim316/DL25) serves as a dynamic hub for our Acoustics course. Here, you'll find additional course materials, additional reading resources, and online tools. It's also a space for sharing files and submitting assignments.")
    st.components.v1.iframe("https://padlet.com/mirankim316/DL25", width=700, height=800)

with tabs[3]:
    st.markdown("#### Group work: Seminar room reservation (TBA)")
    st.page_link("https://www.gnu.ac.kr/sadae/cm/cntnts/cntntsView.do?mi=10831&cntntsId=5364", label="Go to Center for Future Education, College of Education at GNU", icon="➡️")
