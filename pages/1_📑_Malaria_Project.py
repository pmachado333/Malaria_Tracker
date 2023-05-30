import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


st.sidebar.image('./team_pic/SLB_LOGO.png', width=80)
# Page title
st.markdown('# Fast Malaria Tracker')


# Malaria problem worldwide
st.markdown("### The Malaria Problem Worldwide")

st.write("Malaria continues to be a significant global health challenge, affecting millions of people around the world. "
         "It is caused by the Plasmodium parasite and transmitted through the bites of infected mosquitoes. "
         "Early and accurate detection of malaria is crucial for effective treatment and prevention of its spread.")

malaria_map = Image.open('./image_dependencies/Malaria_world.png')
st.image(malaria_map)

st.write('**Yearly Deaths with Malaria**')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
col1, col2, col3, col4, = st.columns(4)
col1.metric("2019", "409 000", "7.7 %")
col2.metric("2020", "558 000", " 36 %")
col3.metric("2021", "627 000", "12 %")
col4.metric("2022", "619 000", "-1.2 %")



# Our mission\
st.write('')
st.write('')
st.markdown("### Our Mission")
st.write("At SLB, our mission is to make malaria detection more efficient and widely accessible, particularly "
         "in resource-constrained areas. By harnessing the power of deep learning and cutting-edge technology, we aim "
         "to empower healthcare professionals, researchers, and organizations in the fight against malaria.")

st.write("Through our innovative approach, we strive to contribute to the global efforts to eliminate malaria, "
         "improve patient outcomes, and ultimately save lives. Join us in our mission and together, let's make a difference "
         "in the battle against malaria.")

# Our target
st.write('')
st.write('')
st.markdown("### Our Target")
st.write('')
st.write('**1.Malaria Detection**')
malaria_detection = Image.open('./image_dependencies/malaria_detection.png')
st.image(malaria_detection)
st.write('')
st.write('')
st.write('**2.Malaria Classification**')
cla_falciparum = Image.open('./image_dependencies/cla_falciparum.png')
cla_malariae = Image.open('./image_dependencies/cla_malariae.png')
cla_ovale = Image.open('./image_dependencies/cla_ovale.png')
cla_vivax = Image.open('./image_dependencies/cla_vivax.png')
col1, col2, col3, col4, = st.columns(4)

with col1:
   st.write("**Falcuparum**")
   st.image(cla_falciparum)
with col2:
   st.write("**Malariae**")
   st.image(cla_malariae)
with col3:
   st.write("**Ovale**")
   st.image(cla_ovale)
with col4:
   st.write("**Vivax**")
   st.image(cla_vivax)

# How deep learning models work
st.write('')
st.write('')
st.markdown("### How Our Deep Learning Models Work")
st.write("Our team has developed state-of-the-art deep learning models specifically designed to analyze thin blood smear samples "
         "and identify malaria infections. These models employ advanced algorithms and artificial intelligence techniques "
         "to accurately detect the presence of Plasmodium parasites in the samples.")

st.write("By utilizing deep learning, we are able to achieve exceptional levels of accuracy and speed in malaria diagnosis, "
         "reducing the time and resources required for manual examination. Our models have undergone rigorous training and "
         "validation using extensive datasets, ensuring their reliability and effectiveness.")






######## Model Description part

st.markdown("### Deep Learning Models Description")
st.write(
    "Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites. "
    "There are several species of malaria parasites, and accurate identification of the parasite species "
    "is crucial for effective treatment. Traditional manual identification methods are time-consuming "
    "and prone to human error. Therefore, we developed several deep learning models to automate and improve the accuracy "
    "of malaria species detection."
)
st.markdown("#### 1. Convonlutional Neural Network Model")

cnn_structure = Image.open('./image_dependencies/cnn_structure.PNG')
st.image(cnn_structure)


st.markdown("#### 1.1 Detection with CNN Model")

st.write('')
st.write("#### 1.2 Classify with CNN Model")
st.write(
    "Our CNN model is trained on a large dataset of thin blood smear samples, which have been labeled "
    "with the corresponding malaria species. The model leverages deep learning techniques to learn "
    "complex patterns and features from the microscopic images of blood smears."
)


st.write("###### Key Features")
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

st.write("###### How to Use")
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

st.write("###### Multi-Class Parasite Detection")

st.write("""
         Kindly review the metrics and pre-processing fundamental for our multiclass detection model. In this scenario, our primary goal was to accurately determine the specific parasite present when a subject is infected. We aimed to achieve high precision and recall for each parasite class, ensuring accurate identification in every case.
         """)

st.write("\n\n")

st.write("""
         To ensure the effectiveness of our multiclass detection model, we carefully reviewed and considered several metrics and pre-processing techniques. These are essential for optimizing the performance and accuracy of the model.
         """)

st.write("###### Initial Dataset Imbalance:")

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

st.write('')
st.write('')

######### YOLO model
yolo_logo = Image.open('./image_dependencies/yolo_logo.PNG')

col1, col2 = st.columns([5,2])
with col1:
    st.markdown("### 2. You Only Look Once Model")
with col2:
    st.image(yolo_logo)

yolo_structure = Image.open('./image_dependencies/yolo_structure.PNG')
st.image(yolo_structure)

st.write("""
    YOLO (You Only Look Once) is an advanced object detection algorithm widely used for efficient and real-time detection of multiple objects in images.
    It has garnered significant attention due to its exceptional performance in the field of computer vision.

    The YOLO model was developed with two primary objectives:

    1. Binary Detection: The model's primary objective is to accurately determine the presence or absence of Malaria infection in the subject. By analyzing the image, it provides a reliable assessment of whether the subject is infected with Malaria or not.

    2. Multi-Class Parasite Detection: Furthermore, the YOLO model also possesses the capability to discern different types of Malaria parasites. By leveraging its deep learning architecture, it offers valuable insights into the specific type of Malaria infection.
    """)
yolov8n = Image.open('./image_dependencies/YOLOV8n.jpg')
st.image(yolov8n)


st.markdown("#### 2.1 Detection with YOLO Model")

st.write("""
         Below are the performance metrics for the binary detection model. Our primary focus was to maximize the recall for infection detection to ensure that no individual goes undiagnosed. However, we also aimed for a sufficiently high
         precision to prevent generating psychological distress among uninfected individuals.

         Additionally, we will present the precision curve against the confidence value. This curve will provide a visual representation of how the precision of the model varies at different confidence thresholds, aiding in understanding the trade-off between precision and recall in the detection process.
         """)


pr_curve_binary = Image.open('./models/Metrics/metrics_Binary/PR_curve.png')
st.image(pr_curve_binary)

p_curve_binary = Image.open('./models/Metrics/metrics_Binary/P_curve.png')
st.image(p_curve_binary)

st.markdown("#### 2.2 Classify with YOLO Model")

st.write("""
         Kindly review the metrics for our multiclass detection model. In this scenario, our primary goal was to accurately determine the specific parasite present when a subject is infected. We aimed to achieve high precision and recall for each parasite class, ensuring accurate identification in every case.
         """)


pr_curve_multiclass = Image.open('./models/Metrics/metrics_Multiclass/PR_curve.png')
st.image(pr_curve_multiclass)

p_curve_multiclass = Image.open('./models/Metrics/metrics_Multiclass/P_curve.png')
st.image(p_curve_multiclass)

st.markdown("#### 2.3 Classification Examples")

st.write("""
        Below, you will find a side-by-side image comparison. On the left-hand side, we showcase images labeled by highly skilled medical doctors with years of experience in their respective fields. On the right-hand side, you will see images labeled by our cutting-edge AI model.

These comparisons serve as a testament to the incredible progress we have made in leveraging AI technology to augment medical diagnostics. Our goal is to enhance the accuracy, efficiency, and accessibility of medical image analysis, ultimately improving patient care and outcomes.

Please explore the images and witness the synergy between human expertise and machine intelligence. We continuously strive to refine and enhance our models, collaborating closely with medical professionals to ensure the highest standards of accuracy and reliability.
         """)

image_labels = Image.open('./models/Metrics/metrics_Multiclass/val_batch0_labels.jpg')
image_pred = Image.open('./models/Metrics/metrics_Multiclass/val_batch0_pred.jpg')
col1, col2 = st.columns(2)
with col1:
    st.image(image_labels, caption="Labeled by skilled medical doctors", use_column_width=True, width=600)
with col2:
    st.image(image_pred, caption="Labeled by our model", use_column_width=True, width=600)
