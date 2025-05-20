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

Make sure you have correct identatioins when writing codes for each tab below.

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

## 4. Voca learning multi tab app sample

+ [app link](https://dlclass.streamlit.app/App_Voca-learning)
+ [py file link](https://github.com/MK316/Digital-Literacy-Class/blob/main/pages/%F0%9F%9A%A6App_Voca-learning.py)

## 5. QR code generator

```
import streamlit as st
import qrcode
from PIL import Image

st.title("🔳 QR Code Generator")

# User input
text = st.text_input("Enter text or URL to generate QR code:")

if text:
    # Generate QR code
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Display image
    st.image(img, caption="Your QR Code", use_container_width=False)

```
