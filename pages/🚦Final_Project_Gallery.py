import streamlit as st
import requests

# Define GitHub raw README.md URLs for each project
project_urls = {
    "👥 Project intro": "",
    "👥 Project 1 (G1)": "https://github.com/KY7437/G01Final/blob/main/README.md",
    "👥 Project 2 (G2)": "https://github.com/yunju05/G02Final/blob/main/README.md",
    "👥 Project 3 (G3)": "https://github.com/JW-1211/G03Final/blob/main/README.md"
}

# Create tabs for each project
tabs = st.tabs(list(project_urls.keys()))

# Loop through each tab and load the corresponding README
for tab, (label, url) in zip(tabs, project_urls.items()):
    with tab:
        try:
            response = requests.get(url)
            response.raise_for_status()
            markdown_content = response.text
            st.markdown(markdown_content, unsafe_allow_html=False)
        except Exception as e:
            st.error(f"❌ Could not load README from {label}.")
            st.exception(e)
