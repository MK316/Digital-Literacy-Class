import streamlit as st
from PIL import Image
import os

# Define the URLs for the audio and image from GitHub
audio_url1 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.mp3"
image_url1 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story01.png"

audio_url2 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story02.mp3"
image_url2 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story02.png"

audio_url3 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story03.mp3"
image_url3 = "https://github.com/MK316/Digital-Literacy-Class/raw/main/materials/story03.png"

# Create Tabs
tabs = st.tabs(["📓 Slides: Intro", "🐾 Sample Stories", "TBA"])

# CSS to align dropdown with buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "pages/slides01/"  
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

# Initialize session state
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0  

# Stop if no slides found
if num_slides == 0:
    st.error("No slides found in the specified folder.")
    st.stop()

# ✅ Function to display the image full-width
def display_image():
    slide_path = os.path.join(slides_path, slide_files[st.session_state.slide_index])
    image = Image.open(slide_path)

    # Resize while maintaining aspect ratio
    st.image(image, caption=f"📖 Slide {st.session_state.slide_index + 1} of {num_slides}", use_container_width=True)

with tabs[0]:
    # 🔹 Navigation Controls
    col1, col2, col3, col4 = st.columns([1, 1, 1, 5])
    
    with col1:
        if st.button("⛳", key="start", help="Reset to the first slide"):
            st.session_state.slide_index = 0
            st.rerun()

    with col2:
        if st.button("◀️", key="previous", help="Go back to the previous slide"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1
                st.rerun()
            else:
                st.warning("This is the first slide.")

    with col3:
        if st.button("▶️", key="next", help="Go to the next slide"):
            if st.session_state.slide_index < num_slides - 1:
                st.session_state.slide_index += 1
                st.rerun()
            else:
                st.warning("Final slide reached.")

    with col4:
        # Dropdown to select slides
        selected_slide = st.selectbox(
            "📑 Jump to Slide",
            options=[f"Slide {i + 1}" for i in range(num_slides)],
            index=st.session_state.slide_index
        )

        # Update slide index if dropdown selection changes
        selected_slide_index = int(selected_slide.split()[-1]) - 1
        if selected_slide_index != st.session_state.slide_index:
            st.session_state.slide_index = selected_slide_index
            st.rerun()

    # ✅ Ensure full-width image display
    display_image()
    
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
