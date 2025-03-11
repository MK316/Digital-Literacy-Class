import streamlit as st
import pandas as pd
from collections import Counter
import base64
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize
from gtts import gTTS
import os
from io import BytesIO
import io

# Ensure that the 'punkt' resource is available
def setup_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("Downloading NLTK 'punkt' resource...")
        nltk.download('punkt', quiet=True)  # quiet=True reduces the output clutter
        print("Download complete.")

setup_nltk()


def preprocess_text(word, proper_nouns):
    # Create a mapping of lowercased proper nouns to their original case
    proper_noun_map = {pn.lower(): pn for pn in proper_nouns}
    
    # Remove contractions and possessive endings before other punctuation
    contractions = ["'s", "'ve", "'d", "'ll", "'re", "'m", "'nt"]
    for contraction in contractions:
        if word.endswith(contraction):
            word = word[:-len(contraction)]
            break
    
    # Remove remaining punctuation
    cleaned_word = word.translate(str.maketrans('', '', string.punctuation))

    # Check if the cleaned word is a proper noun (case insensitive match)
    if cleaned_word.lower() in proper_noun_map:
        return proper_noun_map[cleaned_word.lower()]
    return cleaned_word.lower()

def create_word_frequency_dataframe(text, stopwords, proper_nouns):
    words = text.split()
    clean_text = [preprocess_text(word, proper_nouns) for word in words]
    filtered_words = [word for word in clean_text if word.lower() not in stopwords]
    counter = Counter(filtered_words)
    df = pd.DataFrame(counter.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False)
    return df

def get_table_download_link_csv(df):
    towrite = io.StringIO()
    df.to_csv(towrite, index=False)
    towrite.seek(0)
    b64 = base64.b64encode(towrite.getvalue().encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="word_frequency.csv">Download CSV file</a>'

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(plt)

# Set up the main layout
st.set_page_config(page_title="Text Analysis Tools", page_icon="📝")
st.title('Text Analysis Tools')

# Creating tabs
tab1, tab2, tab3 = st.tabs(["Word Cloud", "Word Frequency", "Read by sentences"])

# Word Cloud Tab
with tab1:
    st.header("Generate a Word Cloud")
    text_input_wc = st.text_area("Paste your text here:", key="wc_input")
    if st.button("Generate Word Cloud", key="generate_wc"):
        if text_input_wc:
            generate_wordcloud(text_input_wc)
        else:
            st.error("Please paste some text to generate the word cloud.")

# Word Frequency Tab
with tab2:
    st.header("Generate Word Frequency Dataframe")
    text_input_wf = st.text_area("Paste your text here:", key="wf_input")
    stopword_input = st.text_area("Enter stopwords separated by commas:", key="stopword_input")
    stopwords = {word.strip().lower() for word in stopword_input.split(',')} if stopword_input else set()
    proper_noun_input = st.text_area("Enter proper nouns separated by commas:", key="proper_noun_input")
    proper_nouns = {word.strip() for word in proper_noun_input.split(',')} if proper_noun_input else set()

    st.write("Words are processed by first removing common contractions and possessive endings ('s, 've, etc.), then other punctuation is stripped. Proper nouns are preserved in their specified form.")

    if st.button("Create Dataframe", key="create_df_wf"):
        if text_input_wf:
            df = create_word_frequency_dataframe(text_input_wf, stopwords, proper_nouns)
            st.dataframe(df)
            st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)
        else:
            st.error("Please paste some text to generate the dataframe.")

with tab3:
    st.header("Text to Speech Conversion")
    text_input_tts = st.text_area("Paste your text here to convert into speech:", key="tts_input")
    if st.button('Start', key='start_tts'):
        if text_input_tts:
            try:
                sentences = sent_tokenize(text_input_tts)
                selected_sentence = st.selectbox("Choose a sentence to hear it spoken:", sentences, key="sentence_select")
                
                if st.button("Generate Audio", key="generate_audio"):
                    tts = gTTS(text=selected_sentence, lang='en')
                    audio_file = BytesIO()
                    tts.save(audio_file)
                    audio_file.seek(0)
                    st.audio(audio_file, format='audio/mp3', start_time=0)
            except Exception as e:
                st.error(f"An error occurred while processing text: {str(e)}")
        else:
            st.error("Please paste some text to start.")
