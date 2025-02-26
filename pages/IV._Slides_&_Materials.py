import streamlit as st

# Define the URLs for the audio and image from GitHub
audio_url1 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.mp3"
image_url1 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.png"

audio_url2 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story02.mp3"
image_url2 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story02.png"

audio_url3 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story03.mp3"
image_url3 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story03.png"

# Create Tabs
tabs = st.tabs(["Slides: Intro", "Sample Stories", "Tab 3"])

# Tab 1: Multimedia Content
with tabs [0]:
    st.caption("To be updated")


    st.page_link("slides01.py", label="🏠 Lecture slides week01")


    
with tabs[1]:
    st.markdown("### 🌺 Story 1: The midnight library")
    # Embedding the audio file
    st.audio(audio_url1, format='audio/mp3')

    # Displaying the image
    st.image(image_url1, caption="The midnight library", width=400)

    st.markdown("""
    In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

    As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

    Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
    """)
    st.markdown("---")

    st.markdown("### 🌺 Story 2: The whispering woods")
    # Embedding the audio file
    st.audio(audio_url2, format='audio/mp3')

    # Displaying the image
    st.image(image_url2, caption="The whispering woods", width=400)

    st.markdown("""
    Leo and his friends discovered a path leading to the Whispering Woods, known for the trees that could talk. The locals avoided it, saying it was bewitched, but the adventurous teens couldn’t resist exploring.

    As they walked deeper into the woods, the trees started whispering. Each tree told stories of ancient times, of battles fought and lovers separated. The trees also warned them about the dangers of forgetting the past and the importance of nature.

    Moved by these stories, the friends promised to protect the woods and share their knowledge. They left the woods wiser, with a deeper respect for nature and its untold stories, ready to advocate for its preservation.    """)
    st.markdown("---")

    st.markdown("### 🌺 Story 3: The lost compass")
    # Embedding the audio file
    st.audio(audio_url3, format='audio/mp3')

    # Displaying the image
    st.image(image_url3, caption="The midnight library", width=400)

    st.markdown("""
    Emma found an old compass in her attic one rainy afternoon. It wasn’t just any compass—it pointed to one’s greatest desire rather than magnetic north. Emma, driven by curiosity, followed the compass’s lead, which took her on a journey through her city like never before.

    The compass led her to various places: a lonely old bookstore, a deserted park, and finally, a small, forgotten art gallery. At each stop, she discovered pieces of her own hidden passions: literature, nature, and art. The journey ended at the gallery, where the compass stopped moving. There, surrounded by beautiful paintings, Emma realized her desire to become an artist.

    Inspired, Emma went home to start her first painting, the compass now her most treasured possession, guiding her not just through the city, but through her dreams.    """)
    st.markdown("---")
    
# Tab 2: Additional Content
with tabs[2]:
    st.header("TBA")
    st.write("")

# Tab 3: Discussions and Feedback
with tabs[2]:
    st.header("TBA")
    st.write("")
