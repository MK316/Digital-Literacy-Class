# Streamlit code collection

### Video link

1. Youtube video

```
st.video("https://www.youtube.com/embed/ADi7F695d90")
```

or

```
url="https://www.youtube.com/embed/ADi7F695d90"
st.video(url)
```


2. Youtube video with controlled size
   
```
import streamlit.components.v1 as components

components.iframe("https://www.youtube.com/embed/ADi7F695d90", width=300, height=200)
```

