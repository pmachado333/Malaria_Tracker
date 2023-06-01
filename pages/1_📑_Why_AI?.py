import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(initial_sidebar_state='expanded', layout='wide')
st.sidebar.image('./team_pic/SLB_LOGO.png', width=80)
# Page title
#st.markdown('# Fast Malaria Tracker')


# Malaria problem worldwide
# st.markdown("### The Malaria Problem Worldwide")

# st.write("Malaria continues to be a significant global health challenge, affecting millions of people around the world. "
#          "It is caused by the Plasmodium parasite and transmitted through the bites of infected mosquitoes. "
#          "Early and accurate detection of malaria is crucial for effective treatment and prevention of its spread.")

# malaria_map = Image.open('./image_dependencies/Malaria_world.png')
# st.image(malaria_map)

st.markdown('### Yearly Casualties with Malaria')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
col1, col2, col3, col4, = st.columns(4)
col1.metric("2019", "409 000", "7.7 %")
col2.metric("2020", "558 000", " 36 %")
col3.metric("2021", "627 000", "12 %")
col4.metric("2022", "619 000", "-1.2 %")


st.write('')
st.write('')
st.write('')
st.write('')
###################################################################
###################################################################
st.markdown('### Current State')
#with st.expander("Expand for details"):

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

metric11, metric22 = st.columns(2)
metric11.metric("Diagnosis time", "15 minutes")
metric22.metric("Malaria detection rate", "95 %")

# st.write("""
# - 15 minutes from blood test sample to Malaria diagnosis
# - 95 % correct malaria detection, from professionals.
# """)
st.write('')
st.write('<span style="color:blue">Questions...(?)</span>', unsafe_allow_html=True)
#st.write('Questions...(?)')
st.write("""
1. Shall we accept a 5% casualty rate?
2. What if Malaria detection was instant and you don’t have to wait 15 minutes?
3. Is this a burden to the health care system?
4. Is there a cost associated to Malaria detection procedures that potentially can be reduced?
5. What are the consequences if infected individual travels to a location without local expertise on Malaria detecion?
""")
st.write('')
st.write('')

st.title('')
st.title('')
st.markdown('### Why AI?')

st.write('')
st.write('')
col31, col32, col33  = st.columns(3)
Efficiency_Image = Image.open('./Images/Efficiency.jpg').resize((200,200))
Remote_Image =  Image.open('./Images/Remote.jpg').resize((200,200))
Accuracy_Image = Image.open('./Images/Accuracy.jpg').resize((200,200))
with col31:
    st.image(Efficiency_Image)
with col32:
    st.image(Remote_Image)
with col33:
    st.image(Accuracy_Image)

#with st.expander("Expand for details"):
st.write("""
        - **Efficiency**: AI algorithms can analyze large amounts of data and images quickly, providing a faster and more efficient diagnosis compared to manual methods. This is particularly beneficial in areas with a high malaria burden, where prompt diagnosis is crucial for effective treatment.
        - **Remote**: AI-powered diagnostic tools can be deployed in remote or resource-limited areas where access to skilled healthcare professionals or laboratory facilities may be limited. Or, in locations where Malaria knowledge is lackluster.
        - **Accuracy**: AI-based systems can provide consistent and reliable results, reducing the potential for human error and variability in diagnosis. This is especially important for detecting low-level infections or differentiating between malaria species accurately.
        """)

###################################################################
###################################################################




st.write('')
st.write('')
# st.markdown("### How Our Deep Learning Models Work")

# #with st.expander("Expand for details"):
# st.write("Our team has developed state-of-the-art deep learning models specifically designed to analyze thin blood smear samples "
#         "and identify malaria infections. These models employ advanced algorithms and artificial intelligence techniques "
#         "to accurately detect the presence of Plasmodium parasites in the samples.")

######## Model Description part

st.markdown("### Deep Learning Models Description")

with st.expander("Expand for details"):
    st.write(
        "Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites. "
        "There are several species of malaria parasites, and accurate identification of the parasite species "
        "is crucial for effective treatment. Traditional manual identification methods are time-consuming "
        "and prone to human error. Therefore, we developed several deep learning models to automate and improve the accuracy "
        "of malaria species detection."
    )
    st.markdown("#### 1. Convonlutional Neural Network Model")

    cnn_structure = Image.open('./image_dependencies/cnn_structure.PNG')
    st.image(cnn_structure, caption='Representation of a CNN sequential layer model')

st.markdown("#### 1.1 Binary")
with st.expander("Expand for details"):

    st.write('This model uses a multilayer deep learning algorithm to label input images of different formats, on the probability of them showing the presence of Malarya parasites.')
    st.write('The initial dataset included images in .png or .jpg format. It comprised three distinct sets of images, amounting to 1364 images in total (~80,000 cells). Each set was prepared by different researchers: Stefanie Lopes from Brazil, Benoit Malleret from Southeast Asia, and Gabriel Rangel for the time course. The blood smears in the images were stained using Giemsa reagent.')
    st.write('The dataset comprises two categories of uninfected cells, namely red blood cells (RBCs) and leukocytes, as well as four categories of infected cells, including gametocytes, rings, trophozoites, and schizonts. Annotators had the option to label certain cells as "difficult" if they did not clearly belong to any specific cell class. The data exhibited a significant class imbalance, with uninfected RBCs constituting the majority (over 95 percent) of all cells, compared to uninfected leukocytes and infected cells.')
    st.write('Simple Feature Engineering was applied to both the training and testing datasets to classify the images to uninfected, images only showing red blood cells (RBCs) and/or leukocytes, and infected, images showing, in addition, any of the other labels. The resulted classes were inbalanced toward infected, as shown in the figures below')

    st.write('Image data Augmentation was applied on the training dataset to balance the labels, below are the Augmantation parameters:')
    st.markdown("- Zoom Range = 0.2")
    st.markdown("- Brightness Range = (0.8, 1.3)")

    # col11, col22 = st.columns(2)

    # with col11:
    #     st.image('Images/Training_Infection_Dist.png')
    # with col22:
    #     st.image('Images/Augmented_Dist.png')



    st.write('Upon testing on unseen data, the model scores were as following')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

metric1, metric2, metric3 = st.columns(3)
metric1.metric("Accuracy", "72 %")
metric2.metric("Recall", "97 %")
metric3.metric("Precision", "76 %")

st.write('')
st.write("#### 1.2 Classification")
with st.expander("Expand for details"):

    st.write(
        "Our CNN model is trained on a large dataset of thin blood smear samples, which have been labeled "
        "with the corresponding malaria species. The model leverages deep learning techniques to learn "
        "complex patterns and features from the microscopic images of blood smears."
    )


    st.write("""
            Kindly review the metrics and pre-processing fundamental for our multiclass detection model. In this scenario, our primary goal was to accurately determine the specific parasite present when a subject is infected. We aimed to achieve high precision and recall for each parasite class, ensuring accurate identification in every case.
            """)

    st.write("\n\n")

    # st.write("""
    #          To ensure the effectiveness of our multiclass detection model, we carefully reviewed and considered several metrics and pre-processing techniques. These are essential for optimizing the performance and accuracy of the model.
    #          """)

    st.write("###### Initial Dataset Imbalance:")

    st.write("""
            The initial dataset provided for training was unbalanced, which posed a challenge to the overall performance of the model. To address this issue, we implemented a comprehensive pre-processing step focused on balancing the data per class. This involved utilizing advanced data augmentation methodologies to generate synthetic data and increase the representation of minority classes. As a result, the class balance was significantly improved, leading to better training and evaluation outcomes.
            """)


    # image_preBalance = Image.open('./image_dependencies/balancement_initial.png')
    # image_postBalance = Image.open('./image_dependencies/balancement_enhanced.png')
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.image(image_preBalance, caption="Class balance before data augmentation", use_column_width=True, width=600)
    # with col2:
    #     st.image(image_postBalance, caption="Class balance after data augmentation", use_column_width=True, width=600)

st.image(Image.open('./balancing.png') ,caption="Class balance after data augmentation", use_column_width=False, width=800)

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



yolo_logo = Image.open('./image_dependencies/yolo_logo.PNG')

col1, col2 = st.columns([5,1])
with col1:
    st.markdown("### 2. You Only Look Once Model")
with col2:
    st.image(yolo_logo)
######### YOLO model

pr_curve_binary_OF = Image.open('./models/Metrics/metrics_Binary/PR_curve.png')
st.image(pr_curve_binary_OF, use_column_width=False, width=800)
with st.expander("Expand for details"):


    yolo_structure = Image.open('./image_dependencies/yolo_structure.PNG')
    st.image(yolo_structure)

    st.write("""
        YOLO (You Only Look Once) is an advanced object detection algorithm widely used for efficient and real-time detection of multiple objects in images.
        It has garnered significant attention due to its exceptional performance in the field of computer vision.

        The YOLO model was developed with two primary objectives:

        1. Binary Detection: The model's primary objective is to accurately determine the presence or absence of Malaria infection in the subject. By analyzing the image, it provides a reliable assessment of whether the subject is infected with Malaria or not.

        2. Multi-Class Parasite Detection: Furthermore, the YOLO model also possesses the capability to discern different types of Malaria parasites. By leveraging its deep learning architecture, it offers valuable insights into the specific type of Malaria infection.
        """)
    #yolov8n = Image.open('./image_dependencies/YOLOV8n.jpg')
    #st.image(yolov8n)


    st.markdown("#### 2.1 Detection with YOLO Model")

    st.write("""
            Below are the performance metrics for the binary detection model. Our primary focus was to maximize the recall for infection detection to ensure that no individual goes undiagnosed. However, we also aimed for a sufficiently high
            precision to prevent generating psychological distress among uninfected individuals.

            Additionally, we will present the precision curve against the confidence value. This curve will provide a visual representation of how the precision of the model varies at different confidence thresholds, aiding in understanding the trade-off between precision and recall in the detection process.
            """)


    pr_curve_binary = Image.open('./models/Metrics/metrics_Binary/PR_curve.png')
    p_curve_binary = Image.open('./models/Metrics/metrics_Binary/P_curve.png')

    yolom1, yolom2 = st.columns(2)

    with yolom1:
        st.image(pr_curve_binary)
    with yolom2:
        st.image(p_curve_binary)

    st.markdown("#### 2.2 Classify with YOLO Model")

    st.write("""
            Kindly review the metrics for our multiclass detection model. In this scenario, our primary goal was to accurately determine the specific parasite present when a subject is infected. We aimed to achieve high precision and recall for each parasite class, ensuring accurate identification in every case.
            """)


    pr_curve_multiclass = Image.open('./models/Metrics/metrics_Multiclass/PR_curve.png')


    p_curve_multiclass = Image.open('./models/Metrics/metrics_Multiclass/P_curve.png')



    yolom3, yolom4 = st.columns(2)

    with yolom3:
        st.image(pr_curve_multiclass)
    with yolom4:
        st.image(p_curve_multiclass)

    st.markdown("#### Classification Examples")
    #with st.expander("Expand for details"):


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
