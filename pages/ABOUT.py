import streamlit as st
from PIL import Image

st.title("About YOLO Model for Malarie Detection")

st.write("""
    YOLO (You Only Look Once) is an advanced object detection algorithm widely used for efficient and real-time detection of multiple objects in images.
    It has garnered significant attention due to its exceptional performance in the field of computer vision.

    The YOLO model was developed with two primary objectives:

    1. Binary Detection: The model's primary objective is to accurately determine the presence or absence of Malaria infection in the subject. By analyzing the image, it provides a reliable assessment of whether the subject is infected with Malaria or not.

    2. Multi-Class Parasite Detection: Furthermore, the YOLO model also possesses the capability to discern different types of Malaria parasites. By leveraging its deep learning architecture, it offers valuable insights into the specific type of Malaria infection.
    """)

st.write("\n\n")
st.write("\n\n")
st.subheader("Binary Detection Metrics")

st.write("""
         Below are the performance metrics for the binary detection model. Our primary focus was to maximize the recall for infection detection to ensure that no individual goes undiagnosed. However, we also aimed for a sufficiently high
         precision to prevent generating psychological distress among uninfected individuals.

         Additionally, we will present the precision curve against the confidence value. This curve will provide a visual representation of how the precision of the model varies at different confidence thresholds, aiding in understanding the trade-off between precision and recall in the detection process.
         """)


pr_curve_binary = Image.open('./models/Metrics/metrics_Binary/PR_curve.png')
st.image(pr_curve_binary)

p_curve_binary = Image.open('./models/Metrics/metrics_Binary/P_curve.png')
st.image(p_curve_binary)



st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.subheader("Multi-Class Parasite Detection")

st.write("""
         Kindly review the metrics for our multiclass detection model. In this scenario, our primary goal was to accurately determine the specific parasite present when a subject is infected. We aimed to achieve high precision and recall for each parasite class, ensuring accurate identification in every case.
         """)


pr_curve_multiclass = Image.open('./models/Metrics/metrics_Multiclass/PR_curve.png')
st.image(pr_curve_multiclass)

p_curve_multiclass = Image.open('./models/Metrics/metrics_Multiclass/P_curve.png')
st.image(p_curve_multiclass)
