import streamlit as st

# Define the URLs for the audio and image from GitHub
audio_url1 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.mp3"
image_url1 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.png"

audio_url2 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.mp3"
image_url2 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.png"

audio_url3 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.mp3"
image_url3 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.png"

# Create Tabs
tabs = st.tabs(["Tab 1: Stories", "Tab 2", "Tab 3"])

# Tab 1: Multimedia Content
with tabs[0]:
    st.header("Welcome to Our Educational Resource")
    st.write("This section provides multimedia educational content for better learning.")

    # Displaying the image
    st.image(image_url1, caption="Visual Aid for the Lesson")

    # Embedding the audio file
    st.audio(audio_url1, format='audio/mp3')

# Tab 2: Additional Content
with tabs[1]:
    st.header("Further Reading and Resources")
    st.write("Here you can find additional reading materials and resources.")

# Tab 3: Discussions and Feedback
with tabs[2]:
    st.header("Join the Discussion")
    st.write("Share your thoughts and feedback with our community.")
