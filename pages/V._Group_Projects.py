import streamlit as st

# Create three tabs
tabs = st.tabs(["📌 Project list", "💻 GitHub IDs", "🖼️ Project Gallery"])

# First tab: Instructions
with tabs[0]:
    st.markdown("### 📌 Project List")
    st.write("""
    Welcome to the project portal! This page will provide details of each project when scheduled:
    """)

    st.markdown("#### No project is assigned yet. (as of 2025. 03. 09)")

# Second tab: GitHub IDs
with tabs[1]:
    st.markdown("### 💻 GitHub IDs for Group Projects")
    st.page_link("https://docs.google.com/spreadsheets/d/1z2uYvH-foo3BZ6a4_T80TK7HOQbIJIYIUe5SWOEaGyk/edit?usp=sharing", label="Make your own account and share your IDs here", icon="➡️")
  

# Third tab: Project Gallery
with tabs[2]:
    st.markdown("### 🖼️ Project Gallery")
    st.write("Once the projects are submitted, they will be displayed below:")

# Footer
st.markdown("---")
st.caption("📌 Note: Make sure to update your GitHub links and project files before the deadline.")
