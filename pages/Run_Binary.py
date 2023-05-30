from PIL import Image
import streamlit as st
import numpy as np
from Binary_Model import Binary_Model

image_uploader = st.file_uploader(label = '', type = ['png', 'jpg'])
if image_uploader is not None:
    pil_image = Image.open(image_uploader)


    np_image = np.array(pil_image)

    model = Binary_Model()

    if model.run_model(np_image)[0][0]>0.5:
        st.subheader('Infected')
    else:
        st.subheader('Uninfected')
    st.image(image_uploader)
