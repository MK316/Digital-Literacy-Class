import streamlit as st
import webbrowser

def main():
    st.title('Digital Tools')
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["💻 Coding platforms", " 📌 Digital tools" ,"🍒 Customized apps"])
    
    with tab1:
        st.markdown('#### Python coding & repositories')
        st.caption("Useful sites to start Python coding and app development")
        st.markdown("---")
        # Dictionary of useful links and their descriptions
        resources = {
            "🔎 Github": {
                "url": "https://github.com",
                "site": "https://github.com",
                "description": "Code repository"
            },
            
            "🔎 Google Colab": {
                "url": "https://colab.research.google.com/",
                "site": "https://colab.research.google.com/",
                "description": "Write code to run online"
            },

            "🔎 ChatGPT": {
                "url": "https://openai.com/index/chatgpt/",
                "site": "https://openai.com/index/chatgpt/",
                "description": "Generative AI."
                },
            "🔎 GNU LMS": {
                "url": "https://rec.ac.kr/gnu",
                "site": "https://rec.ac.kr/gnu",
                "description": "GNU 학습시스템"
            }
        }

        # Display links and descriptions
        for name, info in resources.items():
            st.markdown(f"##### {name}")
            st.markdown(info['description'])
            st.markdown(f"[Visit the site]({info['url']})")
            st.markdown(info['site'])
            st.markdown("---")

            st.write(" ")  # Add some space between entries


    with tab2:
        st.header('Digital & AI tools')
        st.write("Get familiar with digital tools online")
        st.markdown("---")
        # Dictionary of useful links and their descriptions
        resources = {
            "🔎 YouGlish": {
                "url": "https://youglish.com/",
                "description": "Use YouTube videos to practice pronunciation in context and see how words are used in real-life speeches."
            },
            "🔎 PlayPhrase": {
                "url": "https://www.playphrase.me/",
                "description": "Search and play English phrases."
            },
            "🔎 Speechnotes": {
                "url": "https://speechnotes.co",
                "description": "a web-based voice recognition tool that transforms speech into text, perfect for students and professionals."
            },
            "🔎 Elevenlabs": {
                "url": "https://elevenlabs.io",
                "description": "A voice synthesis platform that enables realistic and customizable voice generation for various applications."
            },
            "🔎 SUNO": {
                "url": "https://suno.io",
                "description": "A music synthesis platform that generates various music genres."
            },  
            "🔎 AhaSlides": {
                "url": "https://presenter.ahaslides.com/apps/home",
                "description": "A clouding presentation platform with on spot survey and data sharing."
            },
            "🔎 Invideo": {
                "url": "https://invideo.io/",
                "description": "A Text-to-Video generating AI."
            },
            "🔎 SORA": {
                "url": "https://sora.com/",
                "description": "A Text-to-Video generating AI."
            },
            "🔎 Skybox AI": {
                "url": "https://skybox.blockadelabs.com/",
                "description": "A 360 degree worlds from text."
            },
            "🔎 ZEP": {
                "url": "https://zep.us/en",
                "description": "Fun Metaverse."
            },
        }

        # Display links and descriptions
        for name, info in resources.items():
            st.markdown(f"##### {name}")
            st.markdown(f"[Visit the site]({info['url']})")
            st.markdown(info['description'])
            st.write(" ")  # Add some space between entries
    
    with tab3:
        st.markdown('#### 🌱 Customized Applications: examples')
        # CSS to style the markdown links as buttons
        button_style = """
        <style>
            a.button_link {
                display: inline-block;
                text-align: center;
                background-color: #009999;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            a.button_link:hover {
                background-color: #FF7878;
            }
        </style>
        """
    
        # Apply the CSS
        st.markdown(button_style, unsafe_allow_html=True)
    
        # Creating clickable markdown buttons
        st.markdown('<a href="https://mk-316-accuracyfeedback.hf.space" class="button_link" target="_blank">🍋 App 1: Accuracy Feedback</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-tts-pitch.hf.space" class="button_link" target="_blank">🍐 App 2: Intonation contour</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-foreignaccent.hf.space" class="button_link" target="_blank">🐼 App 3: Foreign accent examples</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://https://mk-316-pronunciationfeedback.hf.space/" class="button_link" target="_blank">📝 App 4: Pronunciation Feedback</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-korean-english.hf.space" class="button_link" target="_blank">🎧 App 5: Loanword English Pronunciation</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-oxford5k.hf.space" class="button_link" target="_blank">🐇 App 6: Oxford 5K Vocabulary practice</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-wer-recording.hf.space/" class="button_link" target="_blank">🌻 App 7: Pronunciation Feedback</a>', unsafe_allow_html=True)
        
    

    st.markdown("---")
    
     # Custom button with a link
    st.caption("7. WER Pronunciation Feedback: free recording")
    app_url6 = "https://mk-316-wer-recording.hf.space/"
    button_html = f"""
    <a href="{app_url6}" target="_blank">
        <button style='color: white; background-color: #00CCFF; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            Pronunciation feedback application
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
 #####

if __name__ == "__main__":
    main()
