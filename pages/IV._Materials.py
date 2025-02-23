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
    st.markdown("### Story 1: The midnight library")
    st.markdown("""
    In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

    As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

    Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
    """)
    st.markdown("---")

    # Displaying the image
    st.image(image_url1, caption="The midnight library", width=400)


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
