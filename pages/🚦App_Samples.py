import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["Applications", "Link App", "Tab 3"])

# First tab content
with tab1:
    st.markdown("### ⛳ Sample Applications to Develop")
    st.caption("Click a link to go to the respective application:")

    # Application links
    url1 = "https://idiomquiz.streamlit.app/"
    url2 = "https://mk316voca.streamlit.app/"
    url3 = "https://example.com/app3"

    # # Create links to different applications
    # st.markdown(f"❄️ [Go to Application 1: Idiom Quiz]({url1})", unsafe_allow_html=True)
    # st.markdown(f"❄️ [Go to Application 2: CEFR vocabulary practice (Listen and Spell)]({url2})", unsafe_allow_html=True)
    # st.markdown(f"❄️ [Go to Application 3]({url3})", unsafe_allow_html=True)

     # Custom button with a link
    app_url1 = "https://mk316voca.streamlit.app/"
    button_html = f"""
    <a href="{app_url1}" target="_blank">
        <button style='color: white; background-color: #2ca02c; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            Go to CEFR Voca Application
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    st.markdown("---")
    
     # Custom button with a link
    app_url2 = "https://mk-316-tce.hf.space/"
    button_html = f"""
    <a href="{app_url2}" target="_blank">
        <button style='color: white; background-color: #2ca02c; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            TCE Application
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    
with tab2:
    st.header("Interactive Audio (doesn't work for now")
    st.write("Click the image below to play the audio:")

    # Paths to your audio and image files
    audio_file_path = "https://github.com/MK316/Digital-Literacy-Class/raw/main/audio/phonetics.mp3"
    image_file_path = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/audio.png"

    # Embedding an audio player that plays when the image is clicked
    audio_html = f"""
    <audio id="audioPlayer" controls style="display:none;">
        <source src="{audio_file_path}" type="audio/mpeg">
        Your browser does not support the audio tag.
    </audio>
    <img src="{image_file_path}" alt="Play Audio" onclick="document.getElementById('audioPlayer').play();" style="cursor: pointer; width: 300px;" />
    """
    st.markdown(audio_html, unsafe_allow_html=True)

with tab3:
    st.header("This is Tab 3")
    st.write("Content for Tab 3 goes here.")
