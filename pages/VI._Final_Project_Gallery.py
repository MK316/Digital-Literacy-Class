
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import numpy as np


# ==================================================
# Page Configuration
# ==================================================
st.set_page_config(
    page_title="Final Project Gallery | Fall 2026",
    page_icon="📘",
    layout="wide"
)


# ==================================================
# Mini Projects: Fall 2026 (Groups 1–6)
# ==================================================
MINI_PROJECT_APPS = {
    "Group 1": "https://g1wordgame.streamlit.app/",
    "Group 2": "https://g2miniproject.streamlit.app/",
    "Group 3": "https://baewovocayoyo.streamlit.app/",
    "Group 4": "https://g4-vocaquiz-mini.streamlit.app/",
    "Group 5": "https://g5-vocaquiz-sushivoca3000.streamlit.app/",
    "Group 6": "https://vocab-life.streamlit.app/",
}


# ==================================================
# Final Projects: Spring 2025 (Groups 1–3)
# ==================================================
FINAL_PROJECTS = {
    "Group 1": {
        "app": "https://s25g01.streamlit.app/",
        "qr": (
            "https://github.com/MK316/"
            "Digital-Literacy-Class/raw/main/images/DLG1.png"
        ),
        "github": (
            "https://github.com/KY7437/"
            "G01Final/blob/main/README.md"
        )
    },
    "Group 2": {
        "app": "https://g02final.streamlit.app/",
        "qr": (
            "https://github.com/MK316/"
            "Digital-Literacy-Class/raw/main/images/DLG2.png"
        ),
        "github": (
            "https://github.com/yunju05/"
            "G02Final/blob/main/README.md"
        )
    },
    "Group 3": {
        "app": "https://g03final.streamlit.app/",
        "qr": (
            "https://github.com/MK316/"
            "Digital-Literacy-Class/raw/main/images/DLG3.png"
        ),
        "github": (
            "https://github.com/JW-1211/"
            "G03Final/blob/main/README.md"
        )
    }
}


# ==================================================
# Resources
# ==================================================
FONT_URL = (
    "https://raw.githubusercontent.com/MK316/"
    "Digital-Literacy-Class/main/data/"
    "NanumGothic-Regular.ttf"
)

FONT_PATH = "/tmp/NanumGothic.ttf"

FEEDBACK_URL = (
    "https://raw.githubusercontent.com/MK316/"
    "Digital-Literacy-Class/refs/heads/main/"
    "data/DL-feedback.csv"
)

SWOT_IMAGE_URLS = {
    "Group 1": "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/Group1.png",
    "Group 2": "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/Group2.png",
    "Group 3": "https://github.com/MK316/Digital-Literacy-Class/raw/main/images/Group3.png",
}
