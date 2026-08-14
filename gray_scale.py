import streamlit as st
from PIL import Image
import time

st.title('Color to Gray Scale Converter')
st.write('Upload Image....')

uploaded_image = st.file_uploader('')
if uploaded_image:
    with st.spinner("Loading data..."):
        time.sleep(2)  # Simulate a slow task
    ui = Image.open(uploaded_image)
    gray_ui = ui.convert('L')
    st.image(gray_ui)
    st.success("Done!")

st.write('Take an image now....')
with st.expander("Open camera: "):
    photo = st.camera_input('photo')

if photo:
    with st.spinner("Loading data..."):
        time.sleep(2)  # Simulate a slow task
    img = Image.open(photo)
    gray_img = img.convert('L')
    st.image(gray_img)
    st.success("Done!")