import streamlit as st
st.set_page_config(page_title="Class Padlet Wall", layout="wide")

st.header("🐾 Sharing for classroom activities")
st.markdown("""
    This Padlet serves as a dynamic hub for Q & As regarding the course. Personal inquiries can be directred via E-mail at _mirankim@gnu.ac.kr_  
    """)
st.components.v1.iframe("https://padlet.com/mirankim316/F26_dlee", width=800, height=800)
