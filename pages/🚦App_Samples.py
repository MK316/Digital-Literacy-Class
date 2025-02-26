import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["🌱 Apps by MK316", "🌹 Apps by Students", "🌐 TBA"])

# First tab content
with tab1:
    st.write("The applications linked here were created by MK316 using Python coding and are interactive apps built with Gradio and Streamlit. Deployment was carried out using Streamlit and Hugging Face.")
    st.caption("Last updated: Feb. 26, 2025")
    st.markdown("---")

    # Application links
    url1 = "https://idiomquiz.streamlit.app/"
    url2 = "https://mk316voca.streamlit.app/"
    url3 = "https://example.com/app3"

     # Custom button with a link
    st.caption("1. Vocabulary learning with sound")
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
####    
     # Custom button with a link
    st.caption("2. Teacher Certificate Exam questions")
    app_url2 = "https://mk-316-tce.hf.space/"
    button_html = f"""
    <a href="{app_url2}" target="_blank">
        <button style='color: white; background-color: #660000; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            TCE (Teacher Certificate Exam) question Application
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
#####
    st.markdown("---")
    
     # Custom button with a link
    st.caption("3. Making sounds: musical notes")
    app_url3 = "https://melody-play.streamlit.app/"
    button_html = f"""
    <a href="{app_url3}" target="_blank">
        <button style='color: white; background-color: #0066CC; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            Generate melody Application
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
 #####
    st.markdown("---")
    
     # Custom button with a link
    st.caption("4. Word frequency: from text to vocabulary list")
    app_url4 = "https://mk-316-freqlist.hf.space/"
    button_html = f"""
    <a href="{app_url4}" target="_blank">
        <button style='color: white; background-color: #CCCC00; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            Generate word list by frequency
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
 #####
    st.markdown("---")
    
     # Custom button with a link
    st.caption("5. Loanword Pronunciation: commonly used English words")
    app_url5 = "https://mk-316-korean-english.hf.space/"
    button_html = f"""
    <a href="{app_url5}" target="_blank">
        <button style='color: white; background-color: #003366; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            Loanword pronunciation application
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
 #####
    st.markdown("---")
    
     # Custom button with a link
    st.caption("6. Pronunciation Feedback")
    app_url6 = "https://mk-316-pronunciationfeedback.hf.space/"
    button_html = f"""
    <a href="{app_url6}" target="_blank">
        <button style='color: white; background-color: #006666; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            Pronunciation feedback application
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
 #####
 
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
