import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

font_path = "https://github.com/google/fonts/blob/main/ofl/nanumgothic/NanumGothic-Regular.ttf"

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
    st.write("❄️ Peer review summaries of each group’s app and its classroom application will be posted here after all presentations are finished.")


# Load data
    df = pd.read_csv("https://raw.githubusercontent.com/MK316/Digital-Literacy-Class/refs/heads/main/data/DL-feedback.csv")  # <- replace with actual file path if needed
    
    # Sidebar selection
    group_list = df['Group'].unique()
    selected_group = st.selectbox("🔍 Select a group to view feedback:", group_list)
    
    # Filter by group
    group_df = df[df['Group'] == selected_group]
    
    st.markdown(f"## 🧾 Feedback Summary for {selected_group}")
    
    # --- Q01 to Q07: Bar chart summaries ---
    st.markdown("### 📊 Quantitative Ratings (1–10 Scale)")
    question_labels = {
        "Q01": "1. Easy to navigate",
        "Q02": "2. Useful for English learning",
        "Q03": "3. Explained classroom use",
        "Q04": "4. Creativity/originality",
        "Q05": "5. Helpful for my teaching",
        "Q06": "6. Adaptable for student levels",
        "Q07": "7. Overall effectiveness"
    }
    
    ratings_means = group_df.loc[:, "Q01":"Q07"].mean()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ratings_means.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_ylabel("Average Rating")
    ax.set_ylim(0, 10)
    ax.set_title("Average Ratings for Each Category")
    ax.set_xticklabels([question_labels[col] for col in ratings_means.index], rotation=45, ha='right')
    st.pyplot(fig)
    
    # --- Q08 & Q09: Wordcloud and comments ---
    for col, title in zip(["Q08", "Q09"], ["Q08: Most impressive aspect", "Q09: Suggestions for improvement"]):
        st.markdown(f"### ☁️ {title}")
        text_data = " ".join(str(comment) for comment in group_df[col] if pd.notnull(comment))
    
        if text_data.strip():
            wc = WordCloud(
                width=600,
                height=300,
                background_color="white",
                font_path=font_path  # 👈 Add this line
            ).generate(text_data)

            st.image(wc.to_array(), use_container_width=True)
    
            with st.expander("📋 Show all comments"):
                for i, comment in enumerate(group_df[col], 1):
                    if pd.notnull(comment):
                        st.markdown(f"- {comment}")
        else:
            st.info("No comments available for this question.")
    
