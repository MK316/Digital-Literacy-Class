import streamlit as st
from gtts import gTTS
from io import BytesIO

# Text for TTS
text = ("Deploying an app means making it available for others to use online. "
        "After writing and testing your code, you can host your app on a platform like Streamlit Cloud, "
        "Hugging Face Spaces, or GitHub Pages. These platforms take care of the setup, "
        "so you don't need advanced server knowledge. For beginners, Streamlit is a great choice because "
        "it allows you to deploy a Python app with just a few clicks. "
        "You upload your code to GitHub, connect it to Streamlit Cloud, and your app goes live with a shareable link. "
        "This makes it easy to create and share interactive applications without complex configurations.")

# Generate TTS audio
tts = gTTS(text, lang="en")
audio_buffer = BytesIO()
tts.write_to_fp(audio_buffer)
audio_buffer.seek(0)

# Display content
st.write("### App Deployment for Beginners")
st.caption("Description: ", text)

# Play TTS audio
st.audio(audio_buffer, format="audio/mp3")
