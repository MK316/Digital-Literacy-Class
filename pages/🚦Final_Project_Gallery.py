import streamlit as st
import requests

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📘 Introduction",
    "👥 Project 1 (G1)",
    "👥 Project 2 (G2)",
    "👥 Project 3 (G3)",
    "⛄ Peer Review (Coming soon)"
])

# Tab 1: Introduction
with tab1:
    st.markdown("### 👋 Welcome to the Final Project Gallery")
    st.write("""
    This page showcases the final group projects from our Spring 2025 course, _Digital Literacy and English Education_.

    - Each group consisted of four to five second-year future English teachers who collaborated over the course of one month. 
    - Their task was to design and demonstrate a code-based application that could be used in English lesson planning and teaching practice.
    - Use the tabs above to explore each group’s project. Each tab will display a live preview of the group’s `README.md` file from their GitHub repository.

    You can:
    ✅ Use the application customized for their target learner group.
    ✅ Read their project summary
    ✅ See visual demos
    ✅ Learn about the group’s goals and findings

    👉 Start by selecting a group tab.
    """)


# Tab 2: Project 1 (G1)
with tab2:
    st.markdown("### English Classroom with Code-based Applications")
    st.markdown("### 🌳 Group 1 APP Project")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Left column: QR image

    # Right column: Blue button
    with col1:
        st.markdown("#### ")
        st.markdown(
            """
            <a href="https://s25g01.streamlit.app/" target="_blank">
                <button style="background-color:#1f77b4; color:white; padding:10px 24px; border:none; border-radius:8px; font-size:16px; cursor:pointer;">
                    Visit the Application
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        image_url = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/DLG1.png"
        st.image(image_url, caption="Enter via QR", width=100)

    # GitHub link at the bottom
    st.markdown("---")
    st.markdown("📁 GitHub files to view: [link](https://github.com/yunju05/G02Final/raw/main/README.md)")

# Tab 3: Project 2 (G2)
with tab3:
    st.markdown("### English Classroom with Code-based Applications")
    st.markdown("### 🌳 Group 2 APP Project")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Left column: QR image


    # Right column: Blue button
    with col1:
        st.markdown("#### ")
        st.markdown(
            """
            <a href="https://g02final.streamlit.app/" target="_blank">
                <button style="background-color:#1f77b4; color:white; padding:10px 24px; border:none; border-radius:8px; font-size:16px; cursor:pointer;">
                    Visit the Application
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        image_url2 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/DLG2.png"
        st.image(image_url2, caption="Enter via QR", width=100)
    # GitHub link at the bottom
    st.markdown("---")
    st.markdown("📁 GitHub files to view: [link](https://github.com/KY7437/G01Final/raw/main/README.md)")



# Tab 4: Project 3 (G3)

with tab4:
    st.markdown("### English Classroom with Code-based Applications")
    st.markdown("### 🌳 Group 3 APP Project")

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # Left column: QR image

    # Right column: Blue button
    with col1:
        st.markdown("#### ")
        st.markdown(
            """
            <a href="https://g03final.streamlit.app/" target="_blank">
                <button style="background-color:#1f77b4; color:white; padding:10px 24px; border:none; border-radius:8px; font-size:16px; cursor:pointer;">
                    Visit the Application
                </button>
            </a>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        image_url3 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/DLG3.png"
        st.image(image_url3, caption="Enter via QR", width=100)

    # GitHub link at the bottom
    st.markdown("---")
    st.markdown("📁 GitHub files to view: [link](https://github.com/JW-1211/G03Final/raw/main/README.md)")




with tab5:
    st.write("❄️ Peer review summaries of each group’s app and its classroom application will be posted here after all presentations are finished.")
    st.markdown("[Peer review link](https://forms.gle/Gfqi98HVKbEFcWiNA)")

