# Building Interactive English Teaching Tools with Streamlit

## 1. What is Streamlit?

**Streamlit** is a Python library that turns scripts into shareable web apps—great for creating quizzes, vocabulary tools, pronunciation aids, and more, all without needing web design experience.  

✅ Perfect for teachers who want to create simple apps to support language learning.  
🧑‍🏫 No need to know HTML or JavaScript!  

## 2. Getting Started

✔ A GitHub account  
✔ A free Streamlit Cloud account linked to GitHub  
✔ Basic Python knowledge (we’ll guide you)  

## 3. Workflow Overview

1. Write your app as a .py file (e.g., app.py) in your new repository
2. Write a file named requirements.txt with necessary libraries/pacakges that need installations
e.g., requirements.txt
```
streamlit
pandas
gtts
```  
3. Go to streamlit.io/cloud → Deploy your GitHub app


## 4. Create Your App File

Let's start with a simple vocabulary viewer. Copy the following code into a file named app.py.

#### 📘 App 1: Vocabulary List Viewer  

```
import streamlit as st
import pandas as pd

st.title("📚 Vocabulary List Viewer")

# Sample vocabulary data
data = {
    "Word": ["analyze", "construct", "define", "evaluate"],
    "Part of Speech": ["verb", "verb", "verb", "verb"],
    "Example": [
        "Please analyze the text.",
        "The students construct a model.",
        "Can you define this term?",
        "We evaluate the results together."
    ]
}

df = pd.DataFrame(data)
st.dataframe(df)

```
✅ Exercise: Replace the words and examples with your current lesson content.

#### 📘 App 2: Simple Multiple-Choice Quiz

```
import streamlit as st
import pandas as pd

st.title("📝 English Word Quiz")

question = "What is the synonym of *happy*?"
options = ["angry", "sad", "joyful", "tired", "hungry"]
answer = "joyful"

user_choice = st.radio("Choose the correct answer:", options)

if st.button("Check Answer"):
    if user_choice == answer:
        st.success("Correct!")
    else:
        st.error("Not quite. Try again.")

```

#### 📘 App 3: Pronunciation Practice with TTS

```
from gtts import gTTS
from io import BytesIO

st.title("🔊 Pronunciation Practice")

word = st.text_input("Enter a word to hear it:")

if word:
    tts = gTTS(word)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    st.audio(audio_fp.getvalue(), format="audio/mp3")

```

## 5. Multi paged application
