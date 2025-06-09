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

    # Plot Quadrogram (empty quadrants)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    ax.text(-0.9, 0.9, "Strengths", fontsize=12, fontweight='bold')
    ax.text(0.4, 0.9, "Opportunities", fontsize=12, fontweight='bold')
    ax.text(-0.9, -0.1, "Weaknesses", fontsize=12, fontweight='bold')
    ax.text(0.4, -0.1, "Threats", fontsize=12, fontweight='bold')

    st.pyplot(fig)

    # Display SWOT descriptions below
    for quadrant in ["Strengths", "Weaknesses", "Opportunities", "Threats"]:
        st.markdown(f"**{quadrant}**")
        for item in swot_data.get(quadrant, []):
            st.markdown(f"- {item}")

    # --- Bar Chart: Group vs Overall Average ---
    st.markdown("### 2. 📊 Quantitative Ratings (1–10 Scale)")
    group_means = group_df.loc[:, "Q01":"Q07"].mean()
    overall_means = df.loc[:, "Q01":"Q07"].mean()
    labels = [question_labels[q] for q in group_means.index]
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(9, 4.5))
    bars1 = ax.bar(x - width/2, group_means.values, width, label=f"{selected_group}", color='skyblue')
    bars2 = ax.bar(x + width/2, overall_means.values, width, label='All Groups (Average)', color='yellow')
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.1, f"{height:.1f}", ha='center', va='bottom', fontsize=8)
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.1, f"{height:.1f}", ha='center', va='bottom', fontsize=8, color='gray')
    ax.set_ylabel("Average Rating")
    ax.set_title("Average Ratings: Group vs Overall")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_ylim(0, 10)
    ax.legend()
    st.pyplot(fig)
    # --- Bar Chart: Group vs Overall Average ---
    st.markdown("### 2. 📊 Quantitative Ratings (1–10 Scale)")
    group_means = group_df.loc[:, "Q01":"Q07"].mean()
    overall_means = df.loc[:, "Q01":"Q07"].mean()
    labels = [question_labels[q] for q in group_means.index]
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(9, 4.5))
    bars1 = ax.bar(x - width/2, group_means.values, width, label=f"{selected_group}", color='skyblue')
    bars2 = ax.bar(x + width/2, overall_means.values, width, label='All Groups (Average)', color='yellow')
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.1, f"{height:.1f}", ha='center', va='bottom', fontsize=8)
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.1, f"{height:.1f}", ha='center', va='bottom', fontsize=8, color='gray')
    ax.set_ylabel("Average Rating")
    ax.set_title("Average Ratings: Group vs Overall")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_ylim(0, 10)
    ax.legend()
    st.pyplot(fig)

    # --- Wordcloud and Comments: Q08 & Q09 ---
    for col, title in zip(["Q08", "Q09"], ["Q08: Most impressive aspect", "Q09: Suggestions for improvement"]):
        st.markdown(f"### ☁️ {title}")
        text_data = " ".join(str(comment) for comment in group_df[col] if pd.notnull(comment))
        if not os.path.exists(font_path):
            response = requests.get(font_url)
            with open(font_path, "wb") as f:
                f.write(response.content)
        if text_data.strip():
            wc = WordCloud(
                width=600,
                height=300,
                background_color="white",
                font_path=font_path
            ).generate(text_data)
            st.image(wc.to_array(), use_container_width=True)
            with st.expander("📋 Show all comments"):
                for i, comment in enumerate(group_df[col], 1):
                    if pd.notnull(comment):
                        st.markdown(f"- {comment}")
        else:
            st.info("No comments available for this question.")
