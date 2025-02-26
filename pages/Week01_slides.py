import streamlit as st
from PIL import Image
import os

# Create Tabs
tabs = st.tabs(["Week01", "TBA", "TBA"])

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
