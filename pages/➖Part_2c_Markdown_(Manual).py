import streamlit as st

# Create a container for tabs
tabs = st.tabs(["Markdown Manual", "Markdown Examples"])

# Tab 1: Markdown Manual
with tabs[0]:
    st.write("### Markdown Manual")
    st.markdown("This manual provides you with the basics and advanced usage of Markdown for documentation and other purposes. Please find the manual at the following link:")
    st.markdown("[Markdown Language Manual](https://github.com/MK316/Coding4ET/blob/main/Lessons/markdown.md)")

# Tab 2: Markdown Examples
with tabs[1]:
    st.write("### Markdown Examples")
    st.markdown("Here you will find examples of pages written in Markdown. These examples will help you understand how to effectively use Markdown for your projects. (This section will be linked later.)")

# Display the tabs
st.sidebar.title("Navigation")
st.sidebar.radio("Go to:", ["Markdown Manual", "Markdown Examples"])


