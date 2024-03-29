import streamlit as st
import os
import matplotlib.pyplot as plt
from PIL import Image
from st_clickable_images import clickable_images
from Binary_Model import Binary_Model
from streamlit_image_select import image_select
from streamlit_extras.switch_page_button import switch_page



st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

logo = Image.open("logo.jpg")
image_size = (100, 100)
col1, col2,col3,col4 = st.columns([1,4,9,2])


with col1:
   st.header(" ")
   st.image(logo.resize((200,200)), use_column_width=False)

with col3:
    st.header(" ")
    st.header(" ")
    st.header(" ")
    st.header(" ")
    st.markdown('<h1 style="font-family: nsimsum; color: darkgrey;"><i>Empowering Doctors, Saving Lives</i></p>', unsafe_allow_html=True)
    #st.header('Empowering Doctors, Saving Lives')
st.markdown('\n\n\n')
st.markdown('\n\n\n')
st.markdown('\n\n\n')
st.markdown('\n\n\n')
st.markdown('\n\n\n')

img1 = Image.open('Images/SLB.jpg' )

img2 = Image.open('Images/docbot_frontpage.jpg' )

img3 = Image.open('Images/yolo.jpg' )

img4 = Image.open('Images/CNN.jpg' )

height = 250

img1_res = img1.resize((300,height))

img2_res = img2.resize((300,height))

img3_res = img4.resize((300,height))

img4_res = img3.resize((300,height))

col1,col2, col3, col4 = st.columns(4)


col1.image(img1_res, use_column_width=True)

if col1.button("About Us", use_container_width = True):
    switch_page(page_name = 'About Us')

col2.image(img2_res, use_column_width=True)

if col2.button("DoctorBot", use_container_width = True):
    switch_page(page_name = 'DoctorBot')

col3.image(img3_res, use_column_width=True)

if col3.button("Malaria Detection", use_container_width = True):
    switch_page(page_name = 'Malaria Detection')

col4.image(img4_res, use_column_width=True)

if col4.button("Why AI?", use_container_width = True):
    switch_page(page_name = 'Why AI?')
