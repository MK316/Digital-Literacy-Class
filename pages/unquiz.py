from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="UNESCO AI CFT Quiz",
    page_icon="📘",
    layout="wide",
)


# ------------------------------------------------------------
# HTML FILE
# ------------------------------------------------------------

APP_DIR = Path(__file__).resolve().parent

HTML_FILE = (
    APP_DIR
    / "data"
    / "index.html"
)


if not HTML_FILE.is_file():

    st.error(
        "index.html was not found."
    )

    st.code(
        str(HTML_FILE)
    )

    st.stop()


# ------------------------------------------------------------
# LOAD HTML
# ------------------------------------------------------------

html_code = HTML_FILE.read_text(
    encoding="utf-8"
)


# ------------------------------------------------------------
# EMBED
# ------------------------------------------------------------

components.html(
    html_code,
    height=3500,
    scrolling=True,
)
