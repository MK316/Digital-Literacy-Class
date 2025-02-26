import streamlit as st

# Set page title
st.set_page_config(page_title="Python for Future Language Teachers", layout="wide")

# Main Title
st.markdown("## 🐍 Python for Future Language Teachers")
st.caption("Explore how Python can benefit both beginners and future educators in the digital age.")

# Create Tabs
tab1, tab2 = st.tabs(["🚀 Introduction to Python", "🎓 Why Coding for Future Language Teachers"])

# 📌 Tab 1: Introduction to Python
with tab1:
    st.markdown("### 🚀 Introduction to Python: A Beginner’s Guide")
    
    st.write(
        """
        Python is one of the most widely used and beginner-friendly programming languages today. 
        Designed for simplicity and readability, Python is ideal for those new to coding. 
        It is a **high-level, general-purpose language**, meaning it can be used in many fields, 
        including web development, data analysis, artificial intelligence, and automation.
        """
    )

    st.markdown("#### ✅ Why Learn Python?")
    st.markdown(
        """
        - **Easy to Read and Write** – Python’s simple syntax makes it ideal for beginners.  
        - **Versatile** – Used in web development, data science, automation, and more.  
        - **Popular in the Industry** – Major companies like Google and NASA use Python.  
        - **Strong Community Support** – Vast learning resources and online support.  
        - **Useful for Automation** – Helps automate repetitive tasks, improving efficiency.  
        """
    )

    st.markdown("#### 🔹 Getting Started with Python")
    st.write(
        """
        Learning Python does not require advanced technical skills. Here’s how to begin:
        1️⃣ **Download Python** from [python.org](https://www.python.org/).  
        2️⃣ **Use an IDE (Integrated Development Environment)** like VS Code or PyCharm.  
        3️⃣ **Start with basic commands** like printing messages and performing calculations.  
        4️⃣ **Practice regularly** with small projects and exercises.
        """
    )

    st.info("Python is a **powerful yet beginner-friendly** language, making it a great choice for anyone entering the world of coding. Whether for automation, analysis, or education, Python **opens doors to new possibilities**.")

# 📌 Tab 2: Why Coding Matters for Future Language Teachers
with tab2:
    st.markdown("### 🎓 Why Coding Matters for Future Language Teachers")

    st.write(
        """
        As technology continues to shape education, **understanding basic programming** can be a game-changer 
        for language teachers. Python helps educators design **interactive learning experiences, develop authentic materials, 
        and enhance digital literacy**—all essential skills for modern language education.
        """
    )

    st.markdown("#### 🔹 1️⃣ Creating Interactive Learning Tools")
    st.write(
        """
        Python allows teachers to build **custom language learning applications** that support learner-centered instruction.  
        Some possibilities include:  
        - **Chatbots** to simulate real-life English conversations.  
        - **Pronunciation and spelling quizzes** with instant feedback.  
        - **Interactive storytelling tools** where students navigate different scenarios.  
        """
    )

    st.markdown("#### 🔹 2️⃣ Developing Authentic Digital Materials")
    st.write(
        """
        Python can help educators **generate and customize** meaningful learning materials:
        - **Web scraping** tools to collect real-world news, interviews, or dialogues.  
        - **Automated vocabulary lists** based on word frequency analysis.  
        - **Text readability analyzers** to adapt content to students' proficiency levels.  
        """
    )

    st.markdown("#### 🔹 3️⃣ Strengthening Digital Literacy for Educators and Students")
    st.write(
        """
        Digital literacy is a crucial skill for modern teachers. Python can help by:  
        - Automating **grading and feedback** for writing assignments.  
        - Providing **data-driven insights** to enhance teaching strategies.  
        - Creating **adaptive learning programs** that adjust based on student progress.  
        """
    )

    st.success(
        "**Python is not just for programmers—it is a tool for educators** who want to innovate their teaching. "
        "By integrating coding skills into language education, teachers can create **engaging, personalized learning experiences** "
        "that prepare students for the digital world."
    )

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit | [MK316](https://mk316.github.io)")

