import streamlit as st
from PIL import Image
import time

#sort of a drop down to enable camera with user's choice
with st.expander("Open camera: "):
    photo = st.camera_input('photo')
    # started a camera here

if photo:
    #runs only if a photo is taken, because webbrowser asks for permission, while the user does something the img
    # instance gets created, wherein the user could or couldnt take a photo
    with st.spinner("Loading data..."):
        #sort of a progess bar like stuff
        time.sleep(3)  #loads for three seconds
    img = Image.open(photo)
    #img has the captured photos add
    gray_img = img.convert('L')
    #gray_img has the add of grayscaled photo
    st.image(gray_img)
    #rendered using this
    st.success("Done!")
    #after all the code done is displayed in green