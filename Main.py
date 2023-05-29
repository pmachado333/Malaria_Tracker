import streamlit as st

st.set_page_config(page_title='SLB DDS', page_icon='./team_pic/SLB_LOGO.png')

st.sidebar.image('./team_pic/SLB_LOGO.png', width=80)


# Page title
st.title("Detecting Malaria Infections through Deep Learning Approach")

# Team picture
team_picture = st.image("./team_pic/SLB_LOGO.png", use_column_width=True)

# Team description
st.header("Our Team")
st.write("At SLB, we are a dedicated team of experts in the field of deep learning applying the knowledge to medical diagnostics. "
         "With a combined experience of over 15 years, our team brings together diverse backgrounds and expertise "
         "to tackle the challenging problem of detecting malaria infections through thin blood smear samples.")

# Malaria problem worldwide
st.header("The Malaria Problem Worldwide")
st.write("Malaria continues to be a significant global health challenge, affecting millions of people around the world. "
         "It is caused by the Plasmodium parasite and transmitted through the bites of infected mosquitoes. "
         "Early and accurate detection of malaria is crucial for effective treatment and prevention of its spread.")

# How deep learning models work
st.header("How Our Deep Learning Models Work")
st.write("Our team has developed state-of-the-art deep learning models specifically designed to analyze thin blood smear samples "
         "and identify malaria infections. These models employ advanced algorithms and artificial intelligence techniques "
         "to accurately detect the presence of Plasmodium parasites in the samples.")

st.write("By utilizing deep learning, we are able to achieve exceptional levels of accuracy and speed in malaria diagnosis, "
         "reducing the time and resources required for manual examination. Our models have undergone rigorous training and "
         "validation using extensive datasets, ensuring their reliability and effectiveness.")

# Our mission
st.header("Our Mission")
st.write("At SLB, our mission is to make malaria detection more efficient and widely accessible, particularly "
         "in resource-constrained areas. By harnessing the power of deep learning and cutting-edge technology, we aim "
         "to empower healthcare professionals, researchers, and organizations in the fight against malaria.")

st.write("Through our innovative approach, we strive to contribute to the global efforts to eliminate malaria, "
         "improve patient outcomes, and ultimately save lives. Join us in our mission and together, let's make a difference "
         "in the battle against malaria.")
