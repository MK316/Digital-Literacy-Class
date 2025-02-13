import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["Applications", "Link App", "Tab 3"])

# First tab content
with tab1:
    st.markdown("### ⛳ Sample Applications to Develop")
    st.caption("Click a link to go to the respective application:")

    # Application links
    url1 = "https://idiomquiz.streamlit.app/"
    url2 = "https://example.com/app2"
    url3 = "https://example.com/app3"

    # Create links to different applications
    st.markdown(f"❄️ [Go to Application 1: Idiom Quiz]({url1})", unsafe_allow_html=True)
    st.markdown(f"❄️ [Go to Application 2]({url2})", unsafe_allow_html=True)
    st.markdown(f"❄️ [Go to Application 3]({url3})", unsafe_allow_html=True)

with tab2:
    st.header("Interactive Audio")
    st.write("Click the image below to play the audio:")

    # Paths to your audio and image files
    audio_file_path = "https://github.com/MK316/Digital-Literacy-Class/raw/main/audio/phonetics.mp3"
    image_file_path = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/audio.png"

    # Display image as a clickable link that plays audio
    st.markdown(f"<a href='{audio_file_path}' target='_blank'><img src='{image_file_path}' alt='Play Audio' style='width:300px; cursor:pointer;' /></a>", unsafe_allow_html=True)

with tab3:
    st.header("This is Tab 3")
    st.write("Content for Tab 3 goes here.")
