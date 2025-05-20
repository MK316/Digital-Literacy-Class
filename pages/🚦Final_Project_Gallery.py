import streamlit as st
import requests
import streamlit.components.v1 as components

# Define GitHub raw README.md URLs for each project (tabs 2–4)
project_urls = {
    "👥 Project 1 (G1)": "https://github.com/KY7437/G01Final/raw/main/README.md",
    "👥 Project 2 (G2)": "https://github.com/yunju05/G02Final/raw/main/README.md",
    "👥 Project 3 (G3)": "https://github.com/JW-1211/G03Final/raw/main/README.md"
}

# Add an intro tab to the beginning
tab_labels = ["📘 Introduction"] + list(project_urls.keys())

# Create tabs
tabs = st.tabs(tab_labels)

# Tab 1: Introduction
with tabs[0]:
    st.markdown("### 👋 Welcome to the Final Project Gallery")
    st.write("""
    This page showcases the final group projects from our Spring 2025 course, _Digital Literacy and English Education_.

    Use the tabs above to explore each group’s project. Each tab will display a live preview of the group’s `README.md` file from their GitHub repository.

    You can:
    - Read their project summary
    - See visual demos
    - Learn about the group’s goals and findings

    👉 Start by selecting a group tab.
    """)

    st.markdown("---")
    st.markdown("""
    + [Group 1 Github repo](https://github.com/KY7437/G01Final) 
    + [Group 2 repo](https://github.com/yunju05/G02Final) 
    + [Group 3 repo](https://github.com/JW-1211/G03Final)
    """)



    components.iframe("https://www.youtube.com/embed/ADi7F695d90", width=300, height=200)
    
# Remaining tabs (project readmes)
for i, (label, url) in enumerate(project_urls.items()):
    with tabs[i + 1]:  # offset by 1 due to the intro tab
        try:
            response = requests.get(url)
            response.raise_for_status()
            markdown_content = response.text
            st.markdown(markdown_content, unsafe_allow_html=False)
        except Exception as e:
            st.error(f"❌ Could not load README from {label}.")
            st.exception(e)


