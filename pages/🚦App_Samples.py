import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["Applications", "Tab 2", "Tab 3"])

# First tab content
with tab1:
    st.markdown("### ⛳ Sample Applications to Develop")
    st.caption("Click a link to go to the respective application:")

    # You can replace these URLs with the actual application links you want to use
    url1 = "https://idiomquiz.streamlit.app/"
    url2 = "https://example.com/app2"
    url3 = "https://example.com/app3"

    # Create links to different applications
    st.markdown(f"[Go to Application 1: Idiom Quiz]({url1})", unsafe_allow_html=True)
    st.markdown(f"[Go to Application 2]({url2})", unsafe_allow_html=True)
    st.markdown(f"[Go to Application 3]({url3})", unsafe_allow_html=True)

# Second and third tabs content
with tab2:
    st.header("This is Tab 2")
    st.write("Content for Tab 2 goes here.")

with tab3:
    st.header("This is Tab 3")
    st.write("Content for Tab 3 goes here.")

    


