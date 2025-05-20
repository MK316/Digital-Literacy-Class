# 🌿 Streamlit code collection

## 1. Video link

#### 1.1 Youtube video

Sample video url: https://www.youtube.com/embed/ADi7F695d90

```
st.video("https://www.youtube.com/embed/ADi7F695d90")
```

or

```
url="https://www.youtube.com/embed/ADi7F695d90"
st.video(url)
```


#### 1.2. Youtube video: to controll the video size
   
```
import streamlit.components.v1 as components

components.iframe("https://www.youtube.com/embed/ADi7F695d90", width=300, height=200)
```

## 2. Line break

```
st.markdown("---")
```

## 3. Multi tabs

Make sure you have correct identatioins when writing codes for each tab below.

```
import streamlit as st

tab1, tab2, tab3 = st.tabs(["name1", "name2", "name3"])

with tab1:
   st.write("This is a message.")
   st.markdown("---")

with tab2:
   st.title("This is a title.")
   st.caption("Last updated: 25. 05. 20")

with tab3:
   st.header("This is a header.")
   st.write("This is optional.")
```

## 4. Voca learning multi tab app sample

+ [app link](https://dlclass.streamlit.app/App_Voca-learning)
+ [py file link](https://github.com/MK316/Digital-Literacy-Class/blob/main/pages/%F0%9F%9A%A6App_Voca-learning.py)

## 5. QR code generator

```
import streamlit as st
import qrcode
from PIL import Image

st.title("🔳 QR Code Generator")

# User input
text = st.text_input("Enter text or URL to generate QR code:")

if text:
    # Generate QR code
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Display image
    st.image(img, caption="Your QR Code", use_container_width=False)

```

## 6. Dictation app code (sample)

```
import streamlit as st
from gtts import gTTS
from io import BytesIO

# --- Sentences to dictate ---
sentences = [
    "The sun is shining brightly.",
    "She goes to school every morning.",
    "Can you help me carry these books?"
]

# --- Initialize session state ---
if "index" not in st.session_state:
    st.session_state.index = 0
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# --- Title and Instructions ---
st.title("🎧 Dictation Practice")
st.markdown("Listen to the sentence and type exactly what you hear, including **punctuation** and **capitalization**.")

# --- Generate and play audio ---
if st.session_state.index < len(sentences):
    current_sentence = sentences[st.session_state.index]
    tts = gTTS(current_sentence)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")
else:
    st.success("✅ You’ve completed all the sentences!")
    st.stop()

# --- Text input box (preserves input) ---
st.session_state.user_input = st.text_input("Type what you heard:", value=st.session_state.user_input)

# --- Submit button ---
if st.button("Submit"):
    st.session_state.submitted = True
    if st.session_state.user_input.strip() == current_sentence:
        st.success("✅ Correct!")
        st.session_state.index += 1
        st.session_state.user_input = ""
        st.session_state.submitted = False
    else:
        st.error("❌ There's a mistake. Please check and try again.")

# --- Optional: Reset ---
if st.button("🔄 Start Over"):
    st.session_state.index = 0
    st.session_state.user_input = ""
    st.session_state.submitted = False

```
