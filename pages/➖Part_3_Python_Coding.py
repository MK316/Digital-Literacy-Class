import streamlit as st
import random

# Set up tabs
tab1, tab2, tab3 = st.tabs(["Python Audio Quiz", "Tab 2", "Tab 3"])

# GitHub raw URLs for the audio files
AUDIO_FILES = {
    "intro": "https://github.com/MK316/Digital-Literacy-Class/raw/main/data/samplequiz/Sample-intro.mp3",
    "SQ01": "https://github.com/MK316/Digital-Literacy-Class/raw/main/data/samplequiz/SQ01.mp3",
    "SQ02": "https://github.com/MK316/Digital-Literacy-Class/raw/main/data/samplequiz/SQ02.mp3",
    "SQ03": "https://github.com/MK316/Digital-Literacy-Class/raw/main/data/samplequiz/SQ03.mp3",
    "SQ04": "https://github.com/MK316/Digital-Literacy-Class/raw/main/data/samplequiz/SQ04.mp3",
    "SQ05": "https://github.com/MK316/Digital-Literacy-Class/raw/main/data/samplequiz/SQ05.mp3",
}

# Initialize session state variables
if "questions" not in st.session_state:
    st.session_state.questions = ["SQ01", "SQ02", "SQ03", "SQ04", "SQ05"]
    st.session_state.correct_answers = {
        "SQ01": "A",
        "SQ02": "A",
        "SQ03": "B",
        "SQ04": "C",
        "SQ05": "A",
    }
    st.session_state.asked_questions = []
    st.session_state.score = 0
    st.session_state.quiz_finished = False
    st.session_state.current_question = None
    st.session_state.waiting_for_next = False  # Track when waiting for a new question

# Tab 1: Python Audio Quiz
with tab1:
    st.header("Python Audio Quiz")

    # Display introduction audio
    st.audio(AUDIO_FILES["intro"], format="audio/mp3")

    # Start button logic (only show if quiz is not finished)
    if not st.session_state.quiz_finished and st.button("Start Quiz"):
        if len(st.session_state.asked_questions) < 5:
            # Select a random question that hasn't been asked yet
            remaining_questions = list(set(st.session_state.questions) - set(st.session_state.asked_questions))
            if remaining_questions:
                selected_question = random.choice(remaining_questions)
                st.session_state.asked_questions.append(selected_question)
                st.session_state.current_question = selected_question
                st.session_state.waiting_for_next = False  # Reset the waiting flag
            else:
                st.session_state.quiz_finished = True  # All questions answered
        else:
            st.session_state.quiz_finished = True  # Quiz complete

    # Display the current question if one is selected
    if st.session_state.current_question and not st.session_state.quiz_finished:
        st.audio(AUDIO_FILES.get(st.session_state.current_question, ""), format="audio/mp3")

        # Display answer choices
        options = ["A", "B", "C", "D"]
        user_choice = st.radio("Select your answer:", options, key=st.session_state.current_question)

        if st.button("Submit Answer"):
            correct_answer = st.session_state.correct_answers[st.session_state.current_question]
            if user_choice == correct_answer:
                st.session_state.score += 1  # Increase score if correct
            
            # Move to the next question automatically
            st.session_state.current_question = None
            st.session_state.waiting_for_next = True
            st.rerun()  # Force an immediate rerun to display the next question

    # Display final score when quiz is finished
    if st.session_state.quiz_finished:
        st.success(f"Quiz Complete! You scored {st.session_state.score} out of 5.")
        
        # Add a restart button
        if st.button("Start/Next"):
            st.session_state.asked_questions = []
            st.session_state.score = 0
            st.session_state.quiz_finished = False
            st.session_state.current_question = None
            st.experimental_rerun()  # Restart the quiz immediately

# Tab 2: Placeholder for additional content
with tab2:
    st.header("Tab 2 Content")
    st.write("This is where you can add content for the second tab.")

# Tab 3: Placeholder for additional content
with tab3:
    st.header("Tab 3 Content")
    st.write("This is where you can add content for the third tab.")
