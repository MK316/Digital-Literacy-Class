import streamlit as st
import pandas as pd
from collections import Counter
import base64
import io
import string

def create_word_frequency_dataframe(text, stopwords, proper_nouns):
    # Clean text by removing punctuation and converting to lower case except proper nouns
    clean_text = []
    words = text.split()
    for word in words:
        # Remove punctuation from word
        cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
        # Check if the cleaned, case-insensitive word is in the proper nouns list
        if cleaned_word in {pn.lower() for pn in proper_nouns}:  # Proper nouns comparison in case-insensitive manner
            # Find the original proper noun with preserved case
            proper_noun = next((pn for pn in proper_nouns if pn.lower() == cleaned_word), cleaned_word)
            clean_text.append(proper_noun)
        else:
            # If not a proper noun, convert to lower case for uniformity
            clean_text.append(cleaned_word.lower())

    # Filter out stopwords
    filtered_words = [word for word in clean_text if word.lower() not in stopwords]
    counter = Counter(filtered_words)
    df = pd.DataFrame(counter.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False)
    return df

def get_table_download_link_csv(df):
    # Generate a link to download the data as a CSV file
    towrite = io.StringIO()
    df.to_csv(towrite, index=False)  # Write the dataframe to a StringIO buffer as CSV
    towrite.seek(0)  # Move to the beginning of the buffer
    b64 = base64.b64encode(towrite.getvalue().encode()).decode()  # Encode the buffer content as Base64
    return f'<a href="data:file/csv;base64,{b64}" download="word_frequency.csv">Download CSV file</a>'

# Set up the main layout
st.set_page_config(page_title="Text Analysis Tools", page_icon="📝")
st.title('Text Analysis Tools')

# Creating tabs
tab1, tab2, tab3 = st.tabs(["Word Cloud", "Word Frequency", "TBA"])

# Word Frequency Tab
with tab2:
    st.header("Generate Word Frequency Dataframe")
    text_input_wf = st.text_area("Paste your text here:", key="wf_input")
    stopword_input = st.text_area("Enter stopwords separated by commas:", key="stopword_input")
    stopwords = {word.strip().lower() for word in stopword_input.split(',')} if stopword_input else set()
    proper_noun_input = st.text_area("Enter proper nouns separated by commas:", key="proper_noun_input")
    proper_nouns = {word.strip() for word in proper_noun_input.split(',')} if proper_noun_input else set()
    if st.button("Create Dataframe", key="create_df"):
        if text_input_wf:
            df = create_word_frequency_dataframe(text_input_wf, stopwords, proper_nouns)
            st.dataframe(df)
            st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)
        else:
            st.error("Please paste some text to generate the dataframe.")

# TBA Tab
with tab3:
    st.header("To Be Announced")
