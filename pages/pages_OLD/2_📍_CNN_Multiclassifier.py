import streamlit as st
import multi_classification as mc
from PIL import Image
import numpy as np
from tensorflow.keras.models import save_model , load_model

st.set_page_config(page_title='CNN MultiClassifier', page_icon='./team_pic/SLB_LOGO.png')
st.sidebar.image('./team_pic/SLB_LOGO.png', width=80)
# Define the header text
image = Image.open("./image_dependencies/muscito.jpg")
col1, col2 = st.columns([11,3])
with col1:
    st.markdown("# MultiClassification Model")
with col2:
    st.image('./image_dependencies/muscito.jpg')

##### CSS #####
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# col11, col12 = st.columns(2)
# col11.metric("Stavanger", "15 °C", "1.2 °C")
# col12.metric("Abu Dhabi", "42 °C", "-3.2 °C")


#### Species ####
st.markdown("  \n")
st.markdown("##### Upload your Thin smear image below. \
    If you are infected with Malaria the computer will \
    tell you which paracite is in your blood")
st.markdown(" \n")
st.markdown(" \n")

fal = Image.open('./image_dependencies/Falciparum.png')
mal = Image.open('./image_dependencies/Malariae.png')
ova = Image.open('./image_dependencies/Ovale.png')
viv = Image.open('./image_dependencies/Vivax.png')

image_size = (230, 190) # Set the desired image size
col1, col2, col3, col4 = st.columns(4) # Create two columns for the images
col1.image(fal.resize(image_size), caption='Falciparum') # 1st image
col2.image(mal.resize(image_size), caption='Malariae') # 2nd image
col3.image(ova.resize(image_size), caption='Ovale') # 3rd image
col4.image(viv.resize(image_size), caption='Vivax') # 4th image

st.markdown("  \n")

#### Image uploader ####
uploaded_image = st.file_uploader(" ", type=["tif", "png", "jpg"])
#st.write("Label description: <span style='color:blue'>This is the label description.</span>", unsafe_allow_html=True)

label_dict = {'Falciparum':0,'Malariae':1, 'Ovale':2, 'Vivax':3 }

if uploaded_image is not None:

    pil_image = Image.open(uploaded_image)  # Convert to PIL Image
    smear = mc.preproc(pil_image) #Preprocess the Image file
    model = load_model('Base_MultiClassification')  #Load the Keras model, saved in dir
    y_pred = model.predict(smear)  #predict class

    #Map the predicted label to the corresponding Paracite
    predicted_labels = y_pred.argmax(axis=1)
    predicted_label = predicted_labels[0]
    inverse_dict = {v: k for k, v in label_dict.items()}
    predicted_class = inverse_dict[predicted_label]
    st.image(uploaded_image)
    #st.write(predicted_class)

    ### Interpretation - update UI ###
    finger = Image.open("./image_dependencies/finger.png")
    if predicted_label == 1:
        col1.image(finger.resize(image_size), caption='Infected by Falciparum')
    elif predicted_label == 2:
        col2.image(finger.resize(image_size), caption='Infected by Malariae')
    elif predicted_label == 3:
        col3.image(finger.resize(image_size), caption='Infected by Ovale')
    elif predicted_label == 4:
        col4.image(finger.resize(image_size), caption='Infected by Vivax')
    else:
        # Handle the case when the number is outside the range 1-4
        st.subheader('We could not detect the parasite')
        #st.error("Invalid number returned from the function.")


### Next Chapter ###
