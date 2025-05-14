# Dataframe worksheet 2 (sample code to implement voca apps)

## Sample 1

Here's a complete Streamlit app that:

+ ✅ Loads a word frequency CSV from GitHub (e.g., Word, Frequency columns)
+ ✅ Displays a dropdown menu of the words
+ ✅ Uses gTTS to generate and play audio when a word is selected

**Note:** Don't forget to updatae 'requirements.txt' file when you expand your code files.


```
import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

st.title("🔊 Word Pronunciation Practice")

# --- Load CSV from GitHub ---
# @st.cache_data (optional - when you use a big data)

# Load word list from GitHub
url = "https://raw.githubusercontent.com/your-username/your-repo/main/word_frequency.csv"  # Replace this with your link
df = pd.read_csv(url)

# --- Dropdown to select word ---
st.markdown("## Select a word to hear its pronunciation")
selected_word = st.selectbox("Choose a word:", df["Word"].dropna().unique())

# --- Generate and play audio ---
if selected_word:
    tts = gTTS(selected_word, lang='en')
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format='audio/mp3')

```
