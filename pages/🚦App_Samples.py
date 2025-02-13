import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["Applications", "link app", "Tab 3"])

def create_clickable_image(audio_file, image_file):
    # Updated HTML with debugging and error handling in JavaScript
    html_str = f"""
    <html>
    <body>
    <!-- Audio element -->
    <audio id="myAudio">
      <source src="{audio_file}" type="audio/mpeg">
      Your browser does not support the audio element.
    </audio>
    <!-- Image element with onclick JavaScript to play audio and log actions -->
    <img src="{image_file}" alt="Play Audio" onclick="playAudio()" style="cursor: pointer;" width="300"/>
    <script>
    function playAudio() {{
        var audio = document.getElementById('myAudio');
        audio.play().then(() => console.log('Audio playing...')).catch(e => console.error('Error playing audio:', e));
    }}
    </script>
    </body>
    </html>
    """
    return html_str



# First tab content
with tab1:
    st.markdown("### ⛳ Sample Applications to Develop")
    st.caption("Click a link to go to the respective application:")

    # You can replace these URLs with the actual application links you want to use
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

    # Paths to your audio and image files (replace these with actual paths)
    audio_file_path = "https://github.com/MK316/Digital-Literacy-Class/raw/main/audio/phonetics.mp3"  # Change to the path of your audio file
    image_file_path = "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/audio.png"  # Change to the path of your image file

    # Create HTML content for clickable image that plays audio
    html_content = create_clickable_image(audio_file_path, image_file_path)

    # Display HTML content in Streamlit
    st.markdown(html_content, unsafe_allow_html=True)

with tab3:
    st.header("This is Tab 3")
    st.write("Content for Tab 3 goes here.")

    


