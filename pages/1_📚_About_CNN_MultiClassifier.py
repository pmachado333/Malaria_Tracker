import streamlit as st
from PIL import Image


st.set_page_config(page_title='About CNN MultiClassifier', page_icon='./team_pic/SLB_LOGO.png')
st.sidebar.image('./team_pic/SLB_LOGO.png', width=80)
#st.title("About CNN Model for Malarie species detection")


st.title("Malaria Species Detection with CNN")
st.write(
    "Welcome to our web application for detecting malaria species present in thin blood smear samples "
    "using a Convolutional Neural Network (CNN) model."
)

st.header("Problem Statement")
st.write(
    "Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites. "
    "There are several species of malaria parasites, and accurate identification of the parasite species "
    "is crucial for effective treatment. Traditional manual identification methods are time-consuming "
    "and prone to human error. Therefore, we developed a CNN model to automate and improve the accuracy "
    "of malaria species detection."
)

st.header("Our Solution")
st.write(
    "Our CNN model is trained on a large dataset of thin blood smear samples, which have been labeled "
    "with the corresponding malaria species. The model leverages deep learning techniques to learn "
    "complex patterns and features from the microscopic images of blood smears."
)

st.header("Key Features")
st.write(
    "- **Automated Malaria Species Detection**: Our model can classify the malaria species present in a "
    "given thin blood smear sample automatically, saving time and reducing human error."
    "\n\n"
    "- **Accuracy and Reliability**: The CNN model achieves high accuracy and reliability in identifying "
    "the malaria species, outperforming traditional manual methods."
    "\n\n"
    "- **User-Friendly Interface**: Our web application provides an intuitive and user-friendly interface "
    "to upload thin blood smear images and obtain the predicted malaria species."
)

st.header("How to Use")
st.write(
    "Using our web application is simple:"
    "\n\n"
    "1. Click on the 'Upload Image' button to select a thin blood smear image from your device."
    "\n\n"
    "2. Once the image is uploaded, our CNN model will analyze it and predict the malaria species present."
    "\n\n"
    "3. The predicted malaria species will be displayed on the screen."
)



st.write("\n\n")
st.write("\n\n")

st.subheader("Multi-Class Parasite Detection")

st.write("""
         Kindly review the metrics for our multiclass detection model. In this scenario, our primary goal was to accurately determine the specific parasite present when a subject is infected. We aimed to achieve high precision and recall for each parasite class, ensuring accurate identification in every case.
         """)


# pr_curve_multiclass = Image.open('./models/Metrics/metrics_Multiclass/PR_curve.png')
# st.image(pr_curve_multiclass)

# p_curve_multiclass = Image.open('./models/Metrics/metrics_Multiclass/P_curve.png')
# st.image(p_curve_multiclass)
