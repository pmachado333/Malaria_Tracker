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
         Kindly review the metrics and pre-processing fundamental for our multiclass detection model. In this scenario, our primary goal was to accurately determine the specific parasite present when a subject is infected. We aimed to achieve high precision and recall for each parasite class, ensuring accurate identification in every case.
         """)

st.write("\n\n")

st.write("""
         To ensure the effectiveness of our multiclass detection model, we carefully reviewed and considered several metrics and pre-processing techniques. These are essential for optimizing the performance and accuracy of the model.
         """)

st.subheader("Initial Dataset Imbalance:")

st.write("""
         The initial dataset provided for training was unbalanced, which posed a challenge to the overall performance of the model. To address this issue, we implemented a comprehensive pre-processing step focused on balancing the data per class. This involved utilizing advanced data augmentation methodologies to generate synthetic data and increase the representation of minority classes. As a result, the class balance was significantly improved, leading to better training and evaluation outcomes.
         """)


image_preBalance = Image.open('./image_dependencies/balancement_initial.png')
image_postBalance = Image.open('./image_dependencies/balancement_enhanced.png')
col1, col2 = st.columns(2)
with col1:
    st.image(image_preBalance, caption="Class balance before data augmentation", use_column_width=True, width=600)
with col2:
    st.image(image_postBalance, caption="Class balance after data augmentation", use_column_width=True, width=600)


######################################

st.write("\n\n")

st.write("""
         We trained and evaluated the model before and after applying the data augmentation techniques. The results clearly demonstrate a substantial increase in performance and the overall quality of the model. By effectively balancing the dataset, our model exhibits improved capability in accurately detecting parasites across multiple classes.
         """)


LC_preBalance = Image.open('./image_dependencies/lc_1.png')
LC_postBalance = Image.open('./image_dependencies/lc_3.png')
col1, col2 = st.columns(2)
with col1:
    st.image(LC_preBalance, caption="Learning Curves before data augmentation", use_column_width=True, width=600)
with col2:
    st.image(LC_postBalance, caption="Learning Curves after data augmentation", use_column_width=True, width=600)


st.write("""
        Despite the advancements achieved through data augmentation, it is important to acknowledge the inherent limitations of convolutional neural networks (CNNs) for this specific task. CNNs are not specifically designed for parasite detection, which can contribute to suboptimal performance. Therefore, we strongly recommend evaluating our model using a You Only Look Once (YOLO) model, which is specifically tailored for object detection tasks. Adopting a YOLO model can potentially enhance the performance and accuracy of parasite identification.
        \n\n
        Our multi-class parasite detection model provides a robust solution for accurately identifying parasites in thin blood smear samples. Through the use of advanced pre-processing techniques, including data augmentation, we have significantly improved the performance and quality of the model. However, to further enhance the capabilities of the system, we suggest exploring the implementation of a YOLO model specifically designed for object detection in this context.
         """)
