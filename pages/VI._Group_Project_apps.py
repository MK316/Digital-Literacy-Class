import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import base64

def generate_wordcloud(text):
    # Generate and display a word cloud
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def get_table_download_link(df):
    # Generate a link to download the data as an Excel file
    towrite = io.BytesIO()
    df.to_excel(towrite, encoding='utf-8', index=False, header=True)  
    towrite.seek(0)  
    b64 = base64.b64encode(towrite.read()).decode()
    return f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="word_frequency.xlsx">Download Excel file</a>'

def create_word_frequency_dataframe(text):
    # Create a dataframe of words and their frequencies
    words = text.split()
    counter = Counter(words)
    df = pd.DataFrame(counter.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False)
    return df

# Set up the main layout
st.set_page_config(page_title="Text Analysis Tools", page_icon="📝")
st.title('Text Analysis Tools')

# Creating tabs
tab1, tab2, tab3 = st.tabs(["Word Cloud", "Word Frequency", "TBA"])

# Word Cloud Tab
with tab1:
    st.header("Generate a Word Cloud")
    text_input = st.text_area("Paste your text here:")
    if st.button("Generate Word Cloud"):
        if text_input:
            generate_wordcloud(text_input)
        else:
            st.error("Please paste some text to generate the word cloud.")

# Word Frequency Tab
with tab2:
    st.header("Generate Word Frequency Dataframe")
    text_input = st.text_area("Paste your text here:")
    if st.button("Create Dataframe"):
        if text_input:
            df = create_word_frequency_dataframe(text_input)
            st.dataframe(df)
            st.markdown(get_table_download_link(df), unsafe_allow_html=True)
        else:
            st.error("Please paste some text to generate the dataframe.")

# TBA Tab
with tab3:
    st.header("To Be Announced")

