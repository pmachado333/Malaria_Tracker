import streamlit as st
import os
import matplotlib.pyplot as plt
from PIL import Image
from st_clickable_images import clickable_images
from Binary_Model import Binary_Model
from streamlit_image_select import image_select
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout='wide')

img1 = Image.open('Images/SLB.jpg' )

img2 = Image.open('Images/docbot_frontpage.jpg' )

img3 = Image.open('Images/yolo.jpg' )

img4 = Image.open('Images/CNN.jpg' )

img1_res = img1.resize((300,300))

img2_res = img2.resize((300,300))

img3_res = img3.resize((300,300))

img4_res = img4.resize((300,300))

col1,col2, col3, col4 = st.columns(4)


col1.image(img1_res)

if col1.button("About Us", use_container_width = True):
    switch_page(page_name = 'DoctorBot')

col2.image(img2_res)

if col2.button("DoctorBot", use_container_width = True):
    switch_page(page_name = 'DoctorBot')

col3.image(img3_res)

if col3.button("Models", use_container_width = True):
    switch_page(page_name = 'Models')

col4.image(img4_res)

if col4.button("About CNN", use_container_width = True):
    switch_page(page_name = 'About CNN MultiClassifier')






#col1.image(img2_res)
#
## Add the button in the second column
#col2.markdown(
#    """
#    <style>
#    .centered {
#        display: flex;
#        flex-direction: column;
#        align-items: center;
#        justify-content: center;
#        height: 100%;
#    }
#    </style>
#    """,
#    unsafe_allow_html=True
#)
#
## Add the button in the second column with the centered class
#col2.markdown('<div class="centered">', unsafe_allow_html=True)
#
#if st.button("Click Me"):
#    switch_page(page_name = 'DoctorBot')
#col2.markdown('</div>', unsafe_allow_html=True)


#with col1:
#    result = image_select(
#    label="",
#    images=[white, img1],
#    captions=["", ''],
#    index=0,
#    use_container_width = True,
#    return_value="original")
#
#    result = image_select(
#    label="",
#    images=[white, img2],
#    captions=["", ''],
#    index = 0,
#    use_container_width = True,
#    return_value="original")
