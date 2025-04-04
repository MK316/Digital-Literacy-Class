import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌱 Apps by MK316", "🌹 Workshop sample", "🎨 Drawing", "🌐 TextBoard", "Test"])

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

    st.markdown("---")
    
     # Custom button with a link
    st.caption("8. Chemistry Education")
    app_url6 = "https://gnu-chemistry.streamlit.app"
    button_html = f"""
    <a href="{app_url6}" target="_blank">
        <button style='color: white; background-color: #CC0066; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
            Chemistry learning app gallery
        </button>
    </a>
    """
    st.markdown(button_html, unsafe_allow_html=True)
 #####
 
with tab2:
    st.markdown("### 1. 제1회 경상 디지털 교육 나눔 한마당")
    st.caption("2024.12.14")

    # Paths to your audio and image files
    st.markdown("#### 💦 [Go to workshop page](https://241214.streamlit.app/)")
    st.markdown("This page contains sample applications in learning vocabulary, listening, speaking as well as Lesson plan samples prepared by students.")
    

with tab3:
    st.caption("Use the canvas below to draw freely. You can change the stroke width and color.")

   # Place Stroke Width, Stroke Color, and Background Color in the same row
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        stroke_width = st.slider("✏️ Stroke Width", 1, 10, 5)
    with col2:
        stroke_color = st.color_picker("🖌 Stroke Color", "#000000")
    with col3:
        bg_color = st.color_picker("🖼 Background Color", "#FFFFFF")

    # Initialize session state for clearing
    if "clear_canvas" not in st.session_state:
        st.session_state["clear_canvas"] = False

    # Create the canvas (Unique key prevents duplication)
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=400,
        width=600,
        drawing_mode="freedraw",
        key="main_canvas" if not st.session_state["clear_canvas"] else "new_canvas"
    )

    # Clear Canvas button
    if st.button("🗑️ Clear Canvas"):
        st.session_state["clear_canvas"] = not st.session_state["clear_canvas"]
        st.rerun()  # This forces Streamlit to reload and clear the drawing



with tab4:

    st.markdown("#### 📝 Text Board")
    st.write("Pick a color and font size for each part, enter the text, and click 'Show'.")

    # Font size selection (same for all parts)
    font_size = st.slider("Select Font Size (px)", min_value=10, max_value=100, value=30)

    # Adjust column widths: [1,4] - Smaller column for color, larger for text input
    col1, col2 = st.columns([1, 4])
    with col1:
        color1 = st.color_picker("🎨 Part 1", "#FF0000")
    with col2:
        text1 = st.text_input("Enter text for Part 1", "")

    col3, col4 = st.columns([1, 4])
    with col3:
        color2 = st.color_picker("🎨 Part 2", "#008000")
    with col4:
        text2 = st.text_input("Enter text for Part 2", "")

    col5, col6 = st.columns([1, 4])
    with col5:
        color3 = st.color_picker("🎨 Part 3", "#0000FF")
    with col6:
        text3 = st.text_input("Enter text for Part 3", "")

    # Button to display combined text on one line
    if st.button("Show"):
        combined_text = f"""
        <p style='font-size:{font_size}px;'>
            <span style='color:{color1};'>{text1} </span>
            <span style='color:{color2};'>{text2} </span>
            <span style='color:{color3};'>{text3}</span>
        </p>
        """
        st.markdown("---")
        st.markdown(combined_text, unsafe_allow_html=True)

with tab5:
    st.markdown("## 📝 Live Textboard")

    st.caption("Type your text, and hit 'ENTER' to display it below in a larger font.")

    # Create a row layout with labels and text input
    col1, col2 = st.columns([1, 4])
    
    with col1:
        color1 = st.color_picker("Part 1", "#FF0000")
    with col2:
        text1 = st.text_input("Enter text for Part 1", key="text1")

    col3, col4 = st.columns([1, 4])
    
    with col3:
        color2 = st.color_picker("Part 2", "#008000")
    with col4:
        text2 = st.text_input("Enter text for Part 2", key="text2")

    col5, col6 = st.columns([1, 4])
    
    with col5:
        color3 = st.color_picker("Part 3", "#0000FF")
    with col6:
        text3 = st.text_input("Enter text for Part 3", key="text3")

    st.markdown("---")
    # Live updating text display with bigger font
    st.markdown(
        f'<p style="font-size: 50px; color: {color1}; display: inline;">{text1} </p>'
        f'<p style="font-size: 50px; color: {color2}; display: inline;">{text2} </p>'
        f'<p style="font-size: 50px; color: {color3}; display: inline;">{text3}</p>',
        unsafe_allow_html=True
    )
