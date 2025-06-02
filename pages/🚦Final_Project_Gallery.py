import streamlit as st
import requests

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📘 Introduction",
    "👥 Project 1 (G1)",
    "👥 Project 2 (G2)",
    "👥 Project 3 (G3)"
])

# Tab 1: Introduction
with tab1:
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

# Tab 2: Project 1 (G1)
with tab2:
    st.markdown("### Group 1 Lesson with Code-based application")
    image_url = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/DLG1.png"    
    st.image(image_url, caption="This image is linked from GitHub", width=200)
    
    st.markdown("""
    + Group 1 Digital Classroom: [Click to Enter](https://g01final.streamlit.app/)
    + Github files to view: [link](https://github.com/yunju05/G02Final/raw/main/README.md)

# Tab 3: Project 2 (G2)
with tab3:
    st.markdown("### Group 2 Lesson with Code-based application")
    image_url = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/DLG2.png"    
    st.image(image_url, caption="This image is linked from GitHub", width=200)
    
    st.markdown("""
    + Group 2 Digital Classroom: [Click to Enter](https://g02final.streamlit.app/)
    + Github files to view: [link](https://github.com/KY7437/G01Final/raw/main/README.md)
# Tab 4: Project 3 (G3)
with tab4:
    st.markdown("### Group 3 Lesson with Code-based application")
    image_url = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/DLG3.png"    
    st.image(image_url, caption="This image is linked from GitHub", width=200)
    
    st.markdown("""
    + Group 3 Digital Classroom: [Click to Enter](https://g03final.streamlit.app/)
    + Github files to view: [link](https://github.com/JW-1211/G03Final/raw/main/README.md)
