# 📙 Building Interactive English Teaching Tools with Streamlit

+ Go to [Streamlit](https://streamlit.io/cloud)

## 1. What is Streamlit?

**Streamlit** is a Python library that turns scripts into shareable web apps—great for creating quizzes, vocabulary tools, pronunciation aids, and more, all without needing web design experience.  

✅ Perfect for teachers who want to create simple apps to support language learning.  
✅ No need to know HTML or JavaScript!  

## 2. Getting Started

✅ A GitHub account  
✅ A free Streamlit Cloud account linked to GitHub  
✅ Basic Python knowledge

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

🌀 [App1](https://mk316-app1.streamlit.app/)

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
🌀 [App2](https://mk316-app2.streamlit.app/)

```
import streamlit as st
import pandas as pd

st.title("📝 English Word Quiz")

question = "What is the synonym of *happy*?"
options = ["angry", "sad", "joyful", "tired", "hungry"]
answer = "joyful"

# ✅ Display the question
st.markdown(question)

user_choice = st.radio("Choose the correct answer:", options)

if st.button("Check Answer"):
    if user_choice == answer:
        st.success("Correct!")
    else:
        st.error("Not quite. Try again.")


```

#### 📘 App 3: Multiple-Choice Quiz using csv file

✅ Prepare a csv file with column names 'Question, Answer, Option1, Option2, Option3, Option4, Option5'  

🌀 [Sample csv file](https://raw.githubusercontent.com/MK316/App1/refs/heads/main/quiz_questions.csv)  
🌀 [APP3](https://mk316-app3.streamlit.app/)

```
import streamlit as st
import pandas as pd
import requests
import io

st.title("📘 English Quiz from CSV")

# --- STEP 1: Load TSV (tab-separated) CSV from GitHub ---
csv_url = "https://raw.githubusercontent.com/yourid/repo/main/quiz_questions.csv"  # use .tsv if applicable

try:
    response = requests.get(csv_url)
    response.raise_for_status()
    
    # ✅ Use sep='\t' for tab-separated files
    df = pd.read_csv(io.StringIO(response.text))

    # ✅ Normalize column names
    df.columns = df.columns.str.strip().str.replace(" ", "").str.capitalize()

except Exception as e:
    st.error(f"❌ Failed to load quiz data: {e}")
    st.stop()

# --- STEP 2: Display Quiz Questions ---
st.header("🧠 Take the Quiz")

if df.empty:
    st.warning("The quiz file is empty or incorrectly formatted.")
else:
    for idx, row in df.iterrows():
        question = row["Question"]
        options = [row[f"Option{i}"] for i in range(1, 6)]
        correct_answer = row["Answer"]

        st.subheader(f"Q{idx+1}: {question}")
        user_choice = st.radio("Choose one:", options, key=f"q_{idx}")

        if st.button("Check Answer", key=f"check_{idx}"):
            if user_choice == correct_answer:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Not quite. The correct answer is **{correct_answer}**")

```


#### 📘 App 4: Pronunciation Practice with TTS

📌 **Important: The following code contains an error. Find it and fix it to make the application work properly.**  
🌀 [App4](https://mk316-app4.streamlit.app/)

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

## 5. Multi paged application (Next time)
