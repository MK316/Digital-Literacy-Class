import streamlit as st
import pandas as pd
from collections import Counter
import base64
import io
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from gtts import gTTS
import os
from nltk.tokenize import sent_tokenize

# Function to preprocess text and remove contractions
def preprocess_text(word, proper_nouns):
    proper_noun_map = {pn.lower(): pn for pn in proper_nouns}
    contractions = ["'s", "'ve", "'d", "'ll", "'re", "'m", "'nt"]
    for contraction in contractions:
        if word.endswith(contraction):
            word = word[:-len(contraction)]
            break
    cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
    return proper_noun_map.get(cleaned_word.lower(), cleaned_word.lower())

# Function to create a word frequency dataframe
def create_word_frequency_dataframe(text, stopwords, proper_nouns):
    words = text.split()
    clean_text = [preprocess_text(word, proper_nouns) for word in words]
    filtered_words = [word for word in clean_text if word.lower() not in stopwords]
    counter = Counter(filtered_words)
    df = pd.DataFrame(counter.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False)
    return df

# Function to generate a word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(plt)

# Initialize the main layout
st.set_page_config(page_title="Text Analysis Tools", page_icon="📝")
st.title('Text Analysis Tools')

# Setup tabs
tab1, tab2, tab3 = st.tabs(["Word Cloud", "Word Frequency", "Text to Speech"])

# Text to Speech Tab
with tab3:
    st.header("Text to Speech Conversion")
    text_input_tts = st.text_area("Paste your text here to convert into speech:", key="tts_input")
    if text_input_tts:
        sentences = sent_tokenize(text_input_tts)
        selected_sentence = st.selectbox("Choose a sentence to hear it spoken:", sentences, key="sentence_select")
        
        if st.button("Generate Audio", key="generate_audio"):
            tts = gTTS(text=selected_sentence, lang='en')
            audio_file = 'output.mp3'
            tts.save(audio_file)
            audio_file = open(audio_file, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3', start_time=0)
