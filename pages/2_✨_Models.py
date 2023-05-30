##### Doing a single page to compile all models available

import streamlit as st
import multi_classification as mc
from PIL import Image
import numpy as np
from tensorflow.keras.models import save_model , load_model
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import shutil
import os

def delete_folder():
    """ This function delete the temp images generated in the model"""
    # Get the folder path from user input
    folder_path = './RUNS_STREAMLIT/'
    folder_path_2 = './RUNS_STREAMLIT_multiclass/'

    # Check if the folder path is provided
    if folder_path:
        # Check if the folder exists
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            # Delete the folder
            shutil.rmtree(folder_path)
            #st.success(f"Folder {folder_path} has been successfully deleted!")
        else:
            pass
            #st.warning("Please provide a valid folder path")

    if folder_path_2:
        # Check if the folder exists
        if os.path.exists(folder_path_2) and os.path.isdir(folder_path_2):
            # Delete the folder
            shutil.rmtree(folder_path_2)
            #st.success(f"Folder {folder_path} has been successfully deleted!")
        else:
            pass
            #st.warning("Please provide a valid folder path")




def call_models():
    model_binary = YOLO('./models/best_binary.pt')
    model_multiclass = YOLO('./models/best_multiclass.pt')
    st.session_state['models_called'] = True
    return model_binary, model_multiclass

st.set_page_config(page_title='Deep Learning Models', page_icon='./team_pic/SLB_LOGO.png')
st.sidebar.image('./team_pic/SLB_LOGO.png', width=80)
# Define the header text
image = Image.open("./image_dependencies/muscito.jpg")
col1, col2 = st.columns([11,3])
with col1:
    st.markdown("# Deep Learning Models")
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
    tell you which parasite is in your blood")
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




label_dict = {'Falciparum':0,'Malariae':1, 'Ovale':2, 'Vivax':3 }


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


option = st.radio("Choose a Model:", ("CNN MultiClassifier", "YOLO"), index=0)

st.write("Welcome to our platform! If you're seeking additional details about the ideal model tailored to your specific needs, \
         we kindly invite you to explore the 'Model Information' section. There, you'll discover a wealth of insightful information \
             to help guide you towards the perfect choice. Feel free to peruse and empower yourself with the knowledge necessary to \
                 make an informed decision. Should you require any further assistance, our team is always here!")

model_selection = option

#### Image uploader ####
uploaded_image = st.file_uploader(" ", type=["tif", "png", "jpg"])

if model_selection == 'YOLO':
    if uploaded_image is not None:
        # Convert uploaded file to PIL Image
        pil_image = Image.open(uploaded_image)

        # Convert PIL Image to NumPy array
        np_image = np.array(pil_image)

    if st.session_state != True:
        model_binary, model_multiclass = call_models()

#model_binary = YOLO('./models/best_binary.pt')
#model_multiclass = YOLO('./models/best_multiclass.pt')


    if uploaded_image is not None:
        delete_folder()

        try:
            model_binary.predict(source=np_image, classes=1,
                        project = './RUNS_STREAMLIT/', save=True, plots=True,
                        hide_conf = True, conf=0.05, retina_masks=True)
            # Open the image file
            image_pred = Image.open('./RUNS_STREAMLIT/predict/image0.jpg')

            #with col2:
            st.image(image_pred, caption="Binary Classification", use_column_width=True)
            # Display the image using Streamlit
            #st.image(image_pred, caption="Predicted", use_column_width=True)

            #col1, col2 = st.columns(2)
            #with col1:
            #st.image(uploaded_image, caption="Original Image", use_column_width=True, width=600)


            model_multiclass.predict(source=np_image,
                        project = './RUNS_STREAMLIT_multiclass/', save=True, plots=True,
                        hide_conf = True, conf=0.05, retina_masks=True)
            # Open the image file
            image_pred_2 = Image.open('./RUNS_STREAMLIT_multiclass/predict/image0.jpg')

            #with col2:
            st.image(image_pred_2, caption="Multi Parasite Classification", use_column_width=True)
        except:
            st.subheader('Sorry, This image format is not accepted.')

if model_selection == 'CNN MultiClassifier':
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
##### CSS #####

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col11, col12 = st.columns(2)
#col11.metric("Stavanger", "15 °C", "1.2 °C")
col12.metric("Malaria Infection 2021", "247 M")
