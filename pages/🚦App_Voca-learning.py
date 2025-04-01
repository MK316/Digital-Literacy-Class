import streamlit as st
import pandas as pd
import random
from gtts import gTTS

# Step 1: Load CSV data from URL
data_url = "https://raw.githubusercontent.com/MK316/241214/refs/heads/main/data/verb_sample.csv"

if data_url:
    try:
        # Read the CSV file
        verb_data = pd.read_csv(data_url)
        required_columns = {'Verb', 'Regularity', 'Past', 'PP'}
        if not required_columns.issubset(set(verb_data.columns)):
            st.error(f"The CSV file must contain the following columns: {', '.join(required_columns)}.")
        else:
            # Initialize session state
            if 'selected_verbs' not in st.session_state:
                st.session_state.selected_verbs = []
            if 'test_verbs_tab2' not in st.session_state:
                st.session_state.test_verbs_tab2 = []
            if 'test_verbs_tab3' not in st.session_state:
                st.session_state.test_verbs_tab3 = []
            if 'test_verbs_tab4' not in st.session_state:
                st.session_state.test_verbs_tab4 = []
            if 'current_verb_tab2' not in st.session_state:
                st.session_state.current_verb_tab2 = None
            if 'current_verb_tab3' not in st.session_state:
                st.session_state.current_verb_tab3 = None
            if 'current_verb_tab4' not in st.session_state:
                st.session_state.current_verb_tab4 = None
            if 'feedback_tab2' not in st.session_state:
                st.session_state.feedback_tab2 = ""
            if 'feedback_tab3' not in st.session_state:
                st.session_state.feedback_tab3 = ""
            if 'feedback_audio_path' not in st.session_state:
                st.session_state.feedback_audio_path = None

            # Callbacks
            def next_verb_tab2():
                st.session_state.current_verb_tab2 = None

            def next_verb_tab3():
                st.session_state.current_verb_tab3 = None

            def next_verb_tab4():
                st.session_state.current_verb_tab4 = None
                st.session_state.feedback_audio_path = None

            # Tab structure
            tab1, tab2, tab3, tab4 = st.tabs(["📌 Select Verbs", "🔸[1] Practice Regularity", "🔸[2] Practice Tense Forms", "🔸[3] Practice with Sounds"])

            # Tab 1: Select verbs
            with tab1:
                st.header("Select Verbs for Practice")
                st.caption("Note: The selected verbs will appear in the practices [1], [2] and [3].")
                # Reset selection button
                if st.button("Reset Selection", key="reset_selection"):
                    for i in range(len(verb_data)):
                        st.session_state[f'verb_checkbox_{i}'] = False
                    st.session_state.selected_verbs = []
                    st.session_state.test_verbs_tab2 = []
                    st.session_state.test_verbs_tab3 = []
                    st.session_state.test_verbs_tab4 = []
                    st.session_state.current_verb_tab2 = None
                    st.session_state.current_verb_tab3 = None
                    st.session_state.current_verb_tab4 = None
                    st.success("Selections have been reset. You can choose new verbs.")

                selected_verb_indices = []
                for i, row in verb_data.iterrows():
                    verb = row['Verb']
                    if st.checkbox(verb, key=f'verb_checkbox_{i}'):
                        selected_verb_indices.append(i)

                if st.button("Submit Selection", key="submit_selection"):
                    st.session_state.selected_verbs = verb_data.loc[selected_verb_indices, 'Verb'].tolist()
                    st.session_state.test_verbs_tab2 = st.session_state.selected_verbs.copy()
                    st.session_state.test_verbs_tab3 = st.session_state.selected_verbs.copy()
                    st.session_state.test_verbs_tab4 = st.session_state.selected_verbs.copy()
                    st.success(f"Selected verbs: {st.session_state.selected_verbs}")

        # Initialize additional session state
        if 'proceed_to_next_tab2' not in st.session_state:
            st.session_state.proceed_to_next_tab2 = False
        
        # Callback for next button
        def next_verb_tab2():
            st.session_state.proceed_to_next_tab2 = True
        
        # Tab 2: Practice Regularity
        with tab2:
            st.header("Practice Regularity")
        
            if not st.session_state.selected_verbs:
                st.warning("No verbs selected. Please go to Tab 1 and select verbs first.")
            else:
                if not st.session_state.test_verbs_tab2:
                    st.success("Completed! You practiced all the selected verbs.")
                else:
                    if st.session_state.proceed_to_next_tab2 or not st.session_state.current_verb_tab2:
                        st.session_state.current_verb_tab2 = random.choice(st.session_state.test_verbs_tab2)
                        st.session_state.feedback_tab2 = ""
                        st.session_state.proceed_to_next_tab2 = False  # Reset the flag
        
                    st.write(f"Is '{st.session_state.current_verb_tab2}' regular or irregular?")
                    answer = st.radio("Choose one:", ["Regular", "Irregular"], key="answer_radio_tab2")
        
                    if st.button("Submit Answer", key="submit_answer_tab2"):
                        correct_answer = verb_data.loc[
                            verb_data['Verb'] == st.session_state.current_verb_tab2, 'Regularity'
                        ].values[0]
                        if answer.lower() == correct_answer.lower():
                            st.session_state.feedback_tab2 = f"Correct: {st.session_state.current_verb_tab2} is {correct_answer}."
                            st.session_state.test_verbs_tab2.remove(st.session_state.current_verb_tab2)
                        else:
                            st.session_state.feedback_tab2 = f"Incorrect: {st.session_state.current_verb_tab2} is {correct_answer}."
        
                        st.write(st.session_state.feedback_tab2)
        
                    st.button("Next", key="next_tab2", on_click=next_verb_tab2)

            # Tab 3: Practice Past and Past Participle
            with tab3:
                st.header("Practice Past and Past Participle")

                if not st.session_state.selected_verbs:
                    st.warning("No verbs selected. Please go to Tab 1 and select verbs first.")
                else:
                    if not st.session_state.test_verbs_tab3:
                        st.success("Completed! You practiced all the selected verbs.")
                    else:
                        if not st.session_state.current_verb_tab3:
                            st.session_state.current_verb_tab3 = random.choice(st.session_state.test_verbs_tab3)
                            st.session_state.feedback_tab3 = ""

                        st.write(f"'{st.session_state.current_verb_tab3}'.")

                        past_answer = st.text_input("Past form:", key="past_answer_tab3")
                        pp_answer = st.text_input("Past Participle form:", key="pp_answer_tab3")

                        if st.button("Submit Answer", key="submit_answer_tab3"):
                            correct_past = verb_data.loc[
                                verb_data['Verb'] == st.session_state.current_verb_tab3, 'Past'
                            ].values[0]
                            correct_pp = verb_data.loc[
                                verb_data['Verb'] == st.session_state.current_verb_tab3, 'PP'
                            ].values[0]

                            if (past_answer.lower() == correct_past.lower() and
                                    pp_answer.lower() == correct_pp.lower()):
                                st.session_state.feedback_tab3 = f"Correct: {st.session_state.current_verb_tab3} - {correct_past} - {correct_pp}."
                                st.session_state.test_verbs_tab3.remove(st.session_state.current_verb_tab3)
                            else:
                                st.session_state.feedback_tab3 = f"Incorrect: {st.session_state.current_verb_tab3} - {correct_past} - {correct_pp}."

                            st.write(st.session_state.feedback_tab3)

                        st.button("Next", key="next_tab3", on_click=next_verb_tab3)

            # Tab 4: Practice with Sounds
            with tab4:
                st.header("Practice with Sounds")

                if not st.session_state.selected_verbs:
                    st.warning("No verbs selected. Please go to Tab 1 and select verbs first.")
                else:
                    if not st.session_state.test_verbs_tab4:
                        st.success("Completed! You practiced all the selected verbs.")
                    else:
                        if not st.session_state.current_verb_tab4:
                            st.session_state.current_verb_tab4 = random.choice(st.session_state.test_verbs_tab4)
                            st.session_state.feedback_audio_path = None

                        verb = st.session_state.current_verb_tab4
                        question_text = f"What are the past and past participle forms of the verb {verb}?"
                        question_audio = gTTS(question_text, lang='en')
                        question_audio_path = f"{verb}_question.mp3"
                        question_audio.save(question_audio_path)
                        st.audio(question_audio_path, format="audio/mp3")

                        user_answer = st.text_input(
                            f"Type your answer for '{verb}' in the format 'base-past-pp':", key="answer_tab4"
                        )

                        if st.button("Submit Answer", key="submit_answer_tab4"):
                            correct_past = verb_data.loc[
                                verb_data['Verb'] == verb, 'Past'
                            ].values[0]
                            correct_pp = verb_data.loc[
                                verb_data['Verb'] == verb, 'PP'
                            ].values[0]
                            correct_answer = f"{verb}-{correct_past}-{correct_pp}"

                            if user_answer.strip().lower() == correct_answer.lower():
                                feedback_text = f"That's correct!: {correct_answer}."
                                st.session_state.test_verbs_tab4.remove(verb)
                            else:
                                feedback_text = f"Please try again!: The correct answer is {correct_answer}."

                            feedback_audio = gTTS(feedback_text, lang='en')
                            feedback_audio_path = f"{verb}_feedback.mp3"
                            feedback_audio.save(feedback_audio_path)
                            st.session_state.feedback_audio_path = feedback_audio_path

                        if st.session_state.feedback_audio_path:
                            st.audio(st.session_state.feedback_audio_path, format="audio/mp3")

                        st.button("Next", key="next_tab4", on_click=next_verb_tab4)

    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
