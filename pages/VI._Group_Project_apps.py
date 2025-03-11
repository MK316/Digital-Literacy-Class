import streamlit as st
import pandas as pd
from collections import Counter
import base64
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from gtts import gTTS
from io import BytesIO
import io
import string
import random


def preprocess_text(word, proper_nouns):
    proper_noun_map = {pn.lower(): pn for pn in proper_nouns}
    contractions = ["'s", "'ve", "'d", "'ll", "'re", "'m", "'nt"]
    for contraction in contractions:
        if word.endswith(contraction):
            word = word[:-len(contraction)]
            break
    cleaned_word = word.translate(str.maketrans('', '', string.punctuation))
    return proper_noun_map.get(cleaned_word.lower(), cleaned_word.lower())

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

st.set_page_config(page_title="Text Analysis Tools", page_icon="📝")
st.title('Try apps with your story')

tab1, tab2, tab3, tab4 = st.tabs(["💬 Word Cloud", "🌱 Word Frequency", "🎧 Read-aloud-Listen", "🎯 Words with picture"])

with tab1:
    st.header("Generate a Word Cloud")
    text_input_wc = st.text_area("Paste your text here:", key="wc_input")
    if st.button("Generate Word Cloud", key="generate_wc"):
        if text_input_wc:
            generate_wordcloud(text_input_wc)
        else:
            st.error("Please paste some text to generate the word cloud.")

with tab2:
    st.header("Generate Word Frequency Dataframe")
    text_input_wf = st.text_area("Paste your text here:", key="wf_input")
    stopword_input = st.text_area("Enter stopwords separated by commas:", key="stopword_input")
    stopwords = {word.strip().lower() for word in stopword_input.split(',')} if stopword_input else set()
    proper_noun_input = st.text_area("Enter proper nouns separated by commas:", key="proper_noun_input")
    proper_nouns = {word.strip() for word in proper_noun_input.split(',')} if proper_noun_input else set()
    if st.button("Create Dataframe", key="create_df_wf"):
        if text_input_wf:
            df = create_word_frequency_dataframe(text_input_wf, stopwords, proper_nouns)
            st.dataframe(df)
            st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)
        else:
            st.error("Please paste some text to generate the dataframe.")

with tab3:
    st.subheader("Text-to-Speech Converter (using Google TTS)")
    text_input = st.text_area("Enter the text you want to convert to speech:")
    language = st.selectbox("Choose a language: 🇰🇷 🇺🇸 🇬🇧 ", ["English (American)", "English (British)", "Korean"])

    tts_button = st.button("Convert Text to Speech")
    
    if tts_button and text_input:
        # Map human-readable language selection to language codes and optionally to TLDs for English
        lang_codes = {
            "English (American)": ("en", 'com'),
            "English (British)": ("en", 'co.uk'),
            "Korean": ("ko", None),
        }
        language_code, tld = lang_codes[language]

        # Assuming you have a version of gTTS that supports tld or you have modified it:
        # This check ensures that the tld parameter is only used when not None.
        if tld:
            tts = gTTS(text=text_input, lang=language_code, tld=tld, slow=False)
        else:
            tts = gTTS(text=text_input, lang=language_code, slow=False)
        
        speech = io.BytesIO()
        tts.write_to_fp(speech)
        speech.seek(0)

        # Display the audio file
        st.audio(speech.getvalue(), format='audio/mp3')



with tab4:
    # Define the data for each setting
    classroom_items = {
        "Desk": "A piece of furniture with a flat top used for working.",
        "Blackboard": "A dark panel for writing on with chalk.",
        "Chalk": "A small stick of colored calcium used for writing on blackboards.",
        "Notebook": "A book of blank or ruled pages for writing notes.",
        "Pen": "A writing instrument used to apply ink to a surface.",
        "Bookshelf": "A shelf or shelves for holding books.",
        "Books": "Printed works consisting of pages bound together.",
        "Clock": "A device for telling the time.",
        "Globe": "A spherical model of the Earth.",
        "Map": "A diagrammatic representation of an area of land or sea showing physical features.",
        "Backpack": "A bag with shoulder straps, carried on the back, and used for carrying things."
    }
    
    living_room_items = {
        "Sofa": "A comfortable seat wide enough for two or three people.",
        "Cushion": "A soft bag of some ornamental material, used for sitting, reclining, or kneeling.",
        "Coffee table": "A small, low table suitable for placing in front of a sofa.",
        "Books": "Printed works consisting of pages bound together.",
        "Vase": "An open container, often used to hold cut flowers.",
        "Television": "A device for receiving television broadcasts.",
        "Bookshelf": "A shelf or shelves for holding books.",
        "Lamp": "A device for giving light, especially one that has a covering or is set on a post.",
        "Plant": "A living organism that grows on land or in water and lacks locomotive movement or obvious nervous or sensory organs.",
        "Rug": "A floor covering of thick woven material or animal skin, typically not extending over the entire floor."
    }
    
    def generate_audio(text):
        try:
            tts = gTTS(text=text, lang='en')
            audio_bytes = io.BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            return audio_bytes
        except Exception as e:
            st.error(f"Failed to generate audio: {e}")
            return None
    
    st.markdown('### 🌈 Learn Vocabulary with Scenes')
    
    col1, col2 = st.columns(2)
    items = {}
    chosen_scene = None
    
    with col1:
        st.image('https://github.com/MK316/Digital-Literacy-Class/raw/main/images/classroom.png', caption='Scene 1. Classroom', width=300)
        if st.button("🍊 Click to Choose an item", key="classroom"):
            chosen_scene = "Classroom"
            items = classroom_items
    
    with col2:
        st.image('https://github.com/MK316/Digital-Literacy-Class/raw/main/images/livingroom.png', caption='Scene 2. Living Room', width=300)
        if st.button("🍋 Click to choose an item", key="living_room"):
            chosen_scene = "Living Room"
            items = living_room_items
    
    if items and chosen_scene:  # Ensure items is not empty and a scene was chosen
        item, description = random.choice(list(items.items()))
        audio_description = f"{item}. {item} is {description.lower()}"
        audio_bytes = generate_audio(audio_description)
        
        if audio_bytes:
            st.write(f"You selected **{chosen_scene}**.")
            st.write(f"📍 **{item}**: {description}")
            st.audio(audio_bytes, format='audio/mp3')
