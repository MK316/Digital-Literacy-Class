# Streamlit code collection

## 1. Video link

#### 1. Youtube video

Sample video url: https://www.youtube.com/embed/ADi7F695d90

```
st.video("https://www.youtube.com/embed/ADi7F695d90")
```

or

```
url="https://www.youtube.com/embed/ADi7F695d90"
st.video(url)
```


#### 2. Youtube video: to controll the video size
   
```
import streamlit.components.v1 as components

components.iframe("https://www.youtube.com/embed/ADi7F695d90", width=300, height=200)
```

## 2. Line break

```
st.markdown("---")
```
