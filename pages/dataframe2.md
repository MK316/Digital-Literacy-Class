# Dataframe worksheet 2 (sample code to implement voca apps)


## 🌱 Multi tab code in streamlit files

+ Note that our streamlit sample (finalproject25) has three tabs
+ Here's how to set tabs in a single .py file

```
tab1, tab2, tab3 = st.tabs(["tab1_name", "tab2_name", "tab3_name"])

with tab1:
    st.write("Text")

with tab2:
    st.markdown("# Lesson 1")

with tab3:
    st.caption("This is a vocabulary learning app.")

```

## 🌱 Libraries to specify and import

+ Libraries to import for 3 sample codes
  
```
import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random
```

📌 Among the libraries listed above, "streamlit, pandas," and "gtts" should also be included in your requirements.txt file.

## 🌀 Sample 1: Wordlist - displaying a dataframe (csv) on the screen

```
with tab1:
    st.markdown("### 📋 Word Frequency Table")

    url = "https://raw.githubusercontent.com/your-username/your-repo/main/word_frequency.csv"
    df = pd.read_csv(url)

    if st.button("Show Word List"):
        st.dataframe(df, use_container_width=True)
```


## 🌀 Sample 2: Listen to the word (using dropdown box)

Here's a complete Streamlit app that:

+ ✅ Loads a word frequency CSV from GitHub (e.g., Word, Frequency columns)
+ ✅ Displays a dropdown menu of the words
+ ✅ Uses gTTS to generate and play audio when a word is selected

**Note:** Don't forget to updatae 'requirements.txt' file when you expand your code files.

```
with tab2:
    st.title("🔊 Word Pronunciation Practice")
    
    url = "https://raw.githubusercontent.com/your-username/your-repo/main/word_frequency.csv"  # Replace this with your link
    df = pd.read_csv(url)
    
    st.markdown("## Select a word to hear its pronunciation")
    selected_word = st.selectbox("Choose a word:", df["Word"].dropna().unique())
    
    if selected_word:
        tts = gTTS(selected_word, lang='en')
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3')
```

+ Same code with comments

```
import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

st.title("🔊 Word Pronunciation Practice")

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

## 🌀 Sample 2

