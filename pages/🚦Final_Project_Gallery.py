import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import numpy as np

font_url = "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/main/data/NanumGothic-Regular.ttf"
font_path = "/tmp/NanumGothic.ttf"

        
# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📘 Introduction",
    "👥 Project 1 (G1)",
    "👥 Project 2 (G2)",
    "👥 Project 3 (G3)",
    "⛄ Peer Evaluation (Ready)"
])

# Tab 1: Introduction
with tab1:
    st.markdown("### 👋 Welcome to the Final Project Gallery")
    st.write("""
    This page showcases the final group projects from our Spring 2025 course, _Digital Literacy and English Education_.

    - Each group consisted of four to five second-year future English teachers who collaborated over the course of one month. 
    - Their task was to design and demonstrate a code-based application deployed on Streamlit that could be used in English lesson planning and teaching practice.
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

    # Korean font (download from GitHub if not available)
    font_url = "https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/main/data/NanumGothic-Regular.ttf"
    font_path = "/tmp/NanumGothic.ttf"

    st.write("❄️ Peer review summaries of each group’s app and its classroom application will be posted here after all presentations are finished.")

    # Load feedback data
    df = pd.read_csv("https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/refs/heads/main/data/DL-feedback.csv")

    # Group selector
    group_list = df['Group'].unique()
    selected_group = st.selectbox("🔍 Select a group to view feedback:", group_list)

    # Filter by selected group
    group_df = df[df['Group'] == selected_group]

    st.markdown(f"## 🧾 Feedback Summary for {selected_group}")

    question_labels = {
        "Q01": "1. Easy to navigate",
        "Q02": "2. Useful for English learning",
        "Q03": "3. Explained classroom use",
        "Q04": "4. Creativity/originality",
        "Q05": "5. Helpful for my teaching",
        "Q06": "6. Adaptable for student levels",
        "Q07": "7. Overall effectiveness"
    }

    # --- SWOT Chart using Matplotlib ---
    st.markdown("### 1. 🧭 SWOT Matrix for This Group")

    swot_descriptions = {
        "Group 1": {
            "Strengths": ["Well-structured 'Study Alone' page with clear learning progression."],
            "Weaknesses": ["App instructions were a bit lengthy and may cause confusion without improved readability."],
            "Opportunities": ["Expandable across proficiency levels.", "Potential to integrate speaking or writing components."],
            "Threats": ["Limited access for users unfamiliar with tech.", "Navigation may be less intuitive for some students."]
        },
        "Group 2": {
            "Strengths": ["Effective grammar activities like sentence rearrangement and crosswords."],
            "Weaknesses": ["Lack of instructional videos and post-lesson review tools."],
            "Opportunities": ["Good potential for peer collaboration and self-directed learning.", "Scope for enhanced multimedia content."],
            "Threats": ["Overloaded vocabulary lists.", "Insufficient scaffolding for lower-level students."]
        },
        "Group 3": {
            "Strengths": ["Innovative integration of AI grammar checker and clear Padlet guidelines."],
            "Weaknesses": ["App selection may be too broad, reducing learner focus."],
            "Opportunities": ["Blended instruction with strong writing-grammar connections.", "Flexible components allow adaptive teaching."],
            "Threats": ["Overpacked content may exceed class time.", "Lack of built-in self-assessment for students."]
        }
    }

    swot_data = swot_descriptions.get(selected_group, {})

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    ax.text(-0.9, 0.9, "Strengths", fontsize=12, fontweight='bold')
    ax.text(0.5, 0.9, "Opportunities", fontsize=12, fontweight='bold')
    ax.text(-0.9, -0.2, "Weaknesses", fontsize=12, fontweight='bold')
    ax.text(0.5, -0.2, "Threats", fontsize=12, fontweight='bold')

    for i, point in enumerate(swot_data.get("Strengths", [])):
        ax.text(-0.9, 0.75 - i * 0.15, f"- {point}", fontsize=10)
    for i, point in enumerate(swot_data.get("Opportunities", [])):
        ax.text(0.5, 0.75 - i * 0.15, f"- {point}", fontsize=10)
    for i, point in enumerate(swot_data.get("Weaknesses", [])):
        ax.text(-0.9, -0.35 - i * 0.15, f"- {point}", fontsize=10)
    for i, point in enumerate(swot_data.get("Threats", [])):
        ax.text(0.5, -0.35 - i * 0.15, f"- {point}", fontsize=10)

    st.pyplot(fig)
    st.markdown("---")
