import streamlit as st
import requests

# Create a container for tabs
tabs = st.tabs(["Markdown Manual", "Markdown Examples"])

# Tab 1: Markdown Manual
with tabs[0]:
    st.write("### Markdown Manual")
    
    # URL of the Markdown file on GitHub
    md_url = "https://raw.githubusercontent.com/MK316/Coding4ET/raw/main/Lessons/markdown.md"
    
    # Fetch the content of the Markdown file
    response = requests.get(md_url)
    
    if response.status_code == 200:
        markdown_text = response.text
        st.markdown(markdown_text, unsafe_allow_html=True)
    else:
        st.error("Failed to load the Markdown manual. Please check the URL and try again.")
        
# Tab 2: Markdown Examples
with tabs[1]:
    st.write("### Markdown Examples")
    st.markdown("Here you will find examples of pages written in Markdown. These examples will help you understand how to effectively use Markdown for your projects. (This section will be linked later.)")



