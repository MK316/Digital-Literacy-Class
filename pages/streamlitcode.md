# 🌿 Streamlit code collection

## 1. Video link

#### 1.1 Youtube video

Sample video url: https://www.youtube.com/embed/ADi7F695d90

```
st.video("https://www.youtube.com/embed/ADi7F695d90")
```

or

```
url="https://www.youtube.com/embed/ADi7F695d90"
st.video(url)
```


#### 1.2. Youtube video: to controll the video size
   
```
import streamlit.components.v1 as components

components.iframe("https://www.youtube.com/embed/ADi7F695d90", width=300, height=200)
```

## 2. Line break

```
st.markdown("---")
```

## 3. Multi tabs

```
import streamlit as st

tab1, tab2, tab3 = st.tabs(["name1", "name2", "name3"])

with tab1:
   st.write("This is a message.")
   st.markdown("---")

with tab2:
   st.title("This is a title.")
   st.caption("Last updated: 25. 05. 20")

with tab3:
   st.header("This is a header.")
   st.write("This is optional.")
```
