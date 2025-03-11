import streamlit as st
import pandas as pd
from collections import Counter
import base64
import io
import string
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
from wordcloud import WordCloud, get_single_color_func
import random


class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns different shades based on the word."""
    def __init__(self, color_to_words, default_color):
        self.color_to_words = color_to_words
        self.default_color = default_color

    def get_color_func(self, color):
        """Returns a single_color_func associated with the word based on the input color."""
        return get_single_color_func(color)

    def __call__(self, word, **kwargs):
        """Returns a color for the given word using the color function defined."""
        return self.get_color_func(self.color_to_words.get(word, self.default_color))(word, **kwargs)


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

def generate_wordcloud(text, shape='square', color_to_words=None, default_color='black'):
    mask = None
    if shape == 'oval':
        mask = Image.new('L', (800, 800), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((50, 50, 750, 750), fill=255)
        mask = np.array(mask)
    elif shape == 'star':
        # You need to create or provide a star-shaped mask image file
        mask = np.array(Image.open('path_to_star_mask.png'))
    
    if not color_to_words:
        color_to_words = {}
    
    wordcloud = WordCloud(width=800, height=400, background_color='white', mask=mask,
                          color_func=SimpleGroupedColorFunc(color_to_words, default_color).__call__).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(plt)

# Set up the main layout
st.set_page_config(page_title="Text Analysis Tools", page_icon="📝")
st.title('Text Analysis Tools')

# Creating tabs
tab1, tab2, tab3 = st.tabs(["Word Cloud", "Word Frequency", "TBA"])

# Streamlit interface
with tab1:
    st.header("Generate a Word Cloud")
    text_input_wc = st.text_area("Paste your text here:", key="wc_input")
    shape_option = st.selectbox("Select Frame Shape:", ['square', 'oval', 'star'], index=0)
    
    # Setup for colors
    colors_input = st.text_area("Enter words and their colors separated by commas (e.g., love:red, peace:blue)", key="colors_input")
    color_to_words = {}
    default_color = 'gray'
    if colors_input:
        color_items = [item.split(':') for item in colors_input.split(',')]
        for color_item in color_items:
            if len(color_item) == 2:
                word, color = color_item
                color_to_words[word.strip()] = color.strip()

    if st.button("Generate Word Cloud", key="generate_wc"):
        if text_input_wc:
            generate_wordcloud(text_input_wc, shape=shape_option, color_to_words=color_to_words, default_color=default_color)
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

# TBA Tab
with tab3:
    st.header("To Be Announced")

