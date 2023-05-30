import streamlit as st


st.sidebar.title('Website Navigation')
nav_option = st.sidebar.radio('Go to:', ('Tha Malarya Detection CNN Binary Model', 'About CNN'))



if nav_option == 'Tha Malarya Detection CNN Binary Model':
    st.title('Tha Malarya Detection CNN Binary Model')
    st.write('This model uses a multilayer deep learning algorithm to label input images of different formats, on the probability of them showing the presence of Malarya parasites.')
    st.write('The initial dataset included images in .png or .jpg format. It comprised three distinct sets of images, amounting to 1364 images in total (~80,000 cells). Each set was prepared by different researchers: Stefanie Lopes from Brazil, Benoit Malleret from Southeast Asia, and Gabriel Rangel for the time course. The blood smears in the images were stained using Giemsa reagent.')
    st.write('The dataset comprises two categories of uninfected cells, namely red blood cells (RBCs) and leukocytes, as well as four categories of infected cells, including gametocytes, rings, trophozoites, and schizonts. Annotators had the option to label certain cells as "difficult" if they did not clearly belong to any specific cell class. The data exhibited a significant class imbalance, with uninfected RBCs constituting the majority (over 95 percent) of all cells, compared to uninfected leukocytes and infected cells.')
    st.write('Simple Feature Engineering was applied to both the training and testing datasets to classify the images to uninfected, images only showing red blood cells (RBCs) and/or leukocytes, and infected, images showing, in addition, any of the other labels. The resulted classes were inbalanced toward infected, as shown in the figures below')
    st.image('./Training_Infection_Dist.png')
    st.write('Image data Augmentation was appled on the training dataset to balance the labels, below are the Augmantation parameters:')
    st.markdown("- Zoom Range = 0.2")
    st.markdown("- Brightness Range = (0.8, 1.3)")

    st.write('Below is an example of an image of the minority class before and after the Augmentation process, showing a random change of brightness and zoom factor:')
    # Load your images
    image1 = './original_image.png'
    image2 = './augmented_image.png'

    # Create two columns for displaying images side by side
    col1, col2 = st.columns(2)

    # Display ima   ge1 in the first column
    with col1:
        st.image(image1, caption='Original Image', use_column_width=True)

    # Display image2 in the second column
    with col2:
        st.image(image2, caption='Augimanted Image', use_column_width=True)

    st.write('Good training data balance was achieved as a result of the data, below is a distribution of the Augmentated image dataset:')
    st.image('./Augmented_Dist.png')

    st.write('Below are the attributes of the different layers of the CNN model, as well as the total number of trainable and non-trainable parameters')
    st.image('./Model Parameters.png')






elif nav_option == 'About CNN':
    st.title('About CNN')
    st.write('CNN (Convolutional Neural Network) is a powerful deep learning method widely used in computer vision tasks, such as image classification, object detection, and image segmentation. Inspired by the biological structure of the visual cortex in animals, CNNs are designed to automatically learn hierarchical representations from input data.')
    st.write('Unlike traditional neural networks, CNNs leverage convolutional layers that apply filters to input data, enabling them to capture local patterns and spatial relationships. This convolutional operation allows CNNs to effectively extract meaningful features from images, making them highly adept at handling visual data.')
    st.write("CNNs consist of multiple layers, including convolutional layers, pooling layers, and fully connected layers. Convolutional layers perform feature extraction by applying convolutional filters to the input, producing feature maps that highlight relevant patterns. Pooling layers reduce the spatial dimensions of the feature maps, enhancing computational efficiency and providing some degree of translation invariance. The fully connected layers, located at the end of the network, are responsible for making predictions based on the learned features.")
    st.write("One of the key advantages of CNNs is their ability to learn directly from raw pixel data, eliminating the need for hand-engineered features. By training on large datasets, CNNs can automatically learn discriminative features and generalize well to unseen images. This makes them invaluable in a variety of applications, including image recognition, medical imaging, autonomous driving, and more.")
    st.write("In recent years, CNNs have achieved remarkable breakthroughs, often surpassing human-level performance in challenging visual tasks. Their success can be attributed to advancements in deep learning algorithms, availability of large-scale annotated datasets, and the availability of high-performance computing resources.")





st.subheader('')
