import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["Applications", "Tab 2", "Tab 3"])

# First tab content
with tab1:
    st.header("Example Applications to develop")
    st.subheader("Click a button to go to the respective application:")

    # You can replace these URLs with the actual application links you want to use
    url1 = "https://idiomquiz.streamlit.app/"
    url2 = "https://example.com/app2"
    url3 = "https://example.com/app3"

    # Create buttons to link to different applications
    if st.button("Go to Application 1: Idiom practice example"):
        st.write(f"You are being redirected to Application 1.")
        st.rerun()
        st.experimental_singleton(f"window.location.href = '{url1}';")
        
    if st.button("Go to Application 2"):
        st.write(f"You are being redirected to Application 2.")
        st.experimental_rerun()
        st.experimental_singleton(f"window.location.href = '{url2}';")
        
    if st.button("Go to Application 3"):
        st.write(f"You are being redirected to Application 3.")
        st.experimental_rerun()
        st.experimental_singleton(f"window.location.href = '{url3}';")

# Second and third tabs content
with tab2:
    st.header("This is Tab 2")
    st.write("Content for Tab 2 goes here.")

with tab3:
    st.header("This is Tab 3")
    st.write("Content for Tab 3 goes here.")

