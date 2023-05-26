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

# Set page title
st.title("You Only Look (LIVE) Once")



############### SIDE PANEL #######################

# Display the metrics in the main content area


############################################

# Add a radio button for selecting options
#option = st.sidebar.radio("Select an option", ("Malarie Detection", "Parasite Classification"))

# Add an image uploader
uploaded_image = st.file_uploader("Upload a thin blood smear sample to be evaluated", type=["jpg", "jpeg", "png"])


if uploaded_image is not None:
    # Convert uploaded file to PIL Image
    pil_image = Image.open(uploaded_image)

    # Convert PIL Image to NumPy array
    np_image = np.array(pil_image)

# Process the uploaded image
if uploaded_image is not None:
    # Display the uploaded image

    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_image, caption="Original Image", use_column_width=True, width=600)


    #st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Perform image processing based on the selected option



####### BACKEND
if st.session_state != True:
    model_binary, model_multiclass = call_models()

#model_binary = YOLO('./models/best_binary.pt')
#model_multiclass = YOLO('./models/best_multiclass.pt')


if uploaded_image is not None:
    delete_folder()

    model_binary.predict(source=np_image, classes=1,
                project = './RUNS_STREAMLIT/', save=True, plots=True,
                line_thickness =10, hide_conf = True, conf=0.05)
    # Open the image file
    image_pred = Image.open('./RUNS_STREAMLIT/predict/image0.jpg')

    with col2:
        st.image(image_pred, caption="Binary Classification", use_column_width=True, width=600)
    # Display the image using Streamlit
    #st.image(image_pred, caption="Predicted", use_column_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_image, caption="Original Image", use_column_width=True, width=600)


    model_multiclass.predict(source=np_image,
                project = './RUNS_STREAMLIT_multiclass/', save=True, plots=True,
                line_thickness =10, hide_conf = True, conf=0.05)
    # Open the image file
    image_pred_2 = Image.open('./RUNS_STREAMLIT_multiclass/predict/image0.jpg')

    with col2:
        st.image(image_pred_2, caption="Multi Parasite Classification", use_column_width=True, width=600)
