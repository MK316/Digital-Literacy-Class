import streamlit as st

# Set page title
st.set_page_config(page_title="Language App Design Guide", layout="wide")

# Main Title
st.markdown("### 🏗️ Designing a Language Learning Application")
st.caption("A step-by-step guide from idea to deployment")

# Create Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "💡 Brainstorming Ideas", 
    "🎯 Defining Learning Goals", 
    "🖌️ Designing the App", 
    "💻 Coding the App", 
    "🎮 Adding Interactivity", 
    "🚀 Deployment & Maintenance"
])

# 1️⃣ Brainstorming Ideas
with tab1:
    st.markdown("## 💡 Brainstorming Ideas")
    st.write(
        """
        Before building a language learning app, start with an **idea**. Ask yourself:
        - What specific **language skill** will this app focus on? (e.g., speaking, listening, writing, pronunciation)
        - Who is the **target audience**? (Beginners, intermediate learners, professionals, students?)
        - What **problems** do language learners face, and how can technology help solve them?
        - Should it be **game-based, quiz-based, chatbot-assisted, or interactive storytelling**?
        """
    )
    st.info("🔍 **Tip:** Explore existing apps to see what works and what can be improved.")

# 2️⃣ Defining Learning Goals
with tab2:
    st.markdown("## 🎯 Defining Learning Goals")
    st.write(
        """
        A well-designed app should align with **clear learning objectives**:
        - **Micro-goals**: What should users learn in **each session**? (e.g., 10 new words, 5 conversation patterns)
        - **Long-term goals**: What skills will learners develop **after weeks or months** of use?
        - **Skill-based learning**:
          - 📖 **Reading** – Text comprehension quizzes, vocabulary-building tools.
          - 🎧 **Listening** – Audio-based exercises, dictation.
          - 🗣️ **Speaking** – AI chatbots, pronunciation analysis.
          - ✍️ **Writing** – Sentence-building tasks, grammar correction.
        """
    )
    st.warning("🎯 **Good practice:** Follow language learning frameworks like CEFR (A1-C2 levels).")

# 3️⃣ Designing the App
with tab3:
    st.markdown("## 🖌️ Designing the App")
    st.write(
        """
        **User-friendly design is essential.** Consider:
        - 🎨 **UI/UX design**: Keep it **minimal, intuitive, and accessible**.
        - 🖥️ **Features & layout**:
          - Home screen with clear navigation
          - Lessons & exercises
          - Progress tracking (e.g., scores, streaks)
        - 🛠️ **Wireframing tools**: Try using Figma, Canva, or Miro to sketch out the interface.
        """
    )
    st.success("🔹 **Best practice:** Keep the interface **simple and engaging** to reduce cognitive load for learners.")

# 4️⃣ Coding the App
with tab4:
    st.markdown("## 💻 Coding the App")
    st.write(
        """
        **Choose a programming language & framework**:
        - 🐍 **Python** – Beginner-friendly, great for AI-powered apps.
        - 🌐 **Web-based**: Use **Streamlit**, Flask, or Django.

        **Basic structure for a language quiz app (Python & Streamlit example)**:
        ```python
        import streamlit as st

        st.title("🗣️ Language Quiz App")
        question = "What is the meaning of 'Bonjour'?"
        options = ["Hello", "Goodbye", "Thank you"]
        answer = "Hello"

        user_answer = st.radio("Select your answer:", options)
        if st.button("Check Answer"):
            if user_answer == answer:
                st.success("✅ Correct!")
            else:
                st.error("❌ Try again!")
        ```
        """
    )
    st.info("💻 **Tip:** Use APIs like Google Translate or SpeechRecognition for advanced features.")

# 5️⃣ Adding Interactivity
with tab5:
    st.markdown("## 🎮 Adding Interactivity")
    st.write(
        """
        **Engagement is key**! Consider:
        - 🎙️ **Speech Recognition** (Let users practice pronunciation)
        - 🎲 **Gamification** (Points, levels, rewards)
        - 📝 **Personalized Feedback** (Correct mistakes with AI-generated tips)
        - 🤖 **Chatbots for real conversations** (Use GPT APIs for AI-driven interactions)
        """
    )
    st.success("🚀 **Best Practice:** Use voice, visuals, and interactive elements to create an immersive experience.")

# 6️⃣ Deployment & Maintenance
with tab6:
    st.markdown("## 🚀 Deployment & Maintenance")
    st.write(
        """
        **Once your app is ready, launch it online!**
        - 🌍 **Web Apps**: Deploy using **Streamlit Cloud, Hugging Face Spaces, or Heroku**.
        - 📊 **Monitor & Update**:
          - Collect **user feedback** to improve UI/UX.
          - Update features based on **learner needs**.
          - Ensure **bug fixes & performance improvements**.
        """
    )
    st.warning("🔄 **Tip:** Keep updating your app to keep learners engaged!")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit | [MK316](https://mk316.github.io)")
