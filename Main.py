import streamlit as st
import os
import matplotlib.pyplot as plt
from PIL import Image
from st_clickable_images import clickable_images
from Binary_Model import Binary_Model
from streamlit_image_select import image_select
from streamlit_extras.switch_page_button import switch_page



st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

img1 = Image.open('Images/SLB.jpg' )

img2 = Image.open('Images/docbot_frontpage.jpg' )

img3 = Image.open('Images/yolo.jpg' )

img4 = Image.open('Images/CNN.jpg' )

img1_res = img1.resize((300,300))

img2_res = img2.resize((300,300))

img3_res = img3.resize((300,300))

img4_res = img4.resize((300,300))

col1,col2, col3, col4 = st.columns(4)


col1.image(img1_res, use_column_width=True)

if col1.button("About Us", use_container_width = True):
    switch_page(page_name = 'About Us')

col2.image(img2_res, use_column_width=True)

if col2.button("DoctorBot", use_container_width = True):
    switch_page(page_name = 'DoctorBot')

col3.image(img3_res, use_column_width=True)

if col3.button("Models", use_container_width = True):
    switch_page(page_name = 'Models')

col4.image(img4_res, use_column_width=True)

if col4.button("About CNN", use_container_width = True):
    switch_page(page_name = 'Malaria Project')
