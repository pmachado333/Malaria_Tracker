import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array


class Binary_Model():

#    def __init__(self, image_path):
#        self.image_path = image_path



# a function that loads and converts the image to numpy array

    def load_and_preprocess_image(self, image_path):

        image = load_img(image_path, target_size=(250,250))

        image_array = img_to_array(image)

        preprocessed_image = tf.keras.applications.resnet50.preprocess_input(image_array)

        return preprocessed_image

 # a function that min-max scales and converts the image to tensor

    def normalize_image(self, image):

        min_val = np.min(image)
        max_val = np.max(image)


        # Perform min-max normalization
        normalized_image = (image - min_val) / (max_val - min_val)

        return tf.convert_to_tensor(normalized_image)


# a function that loads the model

    def load_model(self):

        model_path = os.path.join('Models', '3rd_balanced_model.h5')

        model = tf.keras.models.load_model(model_path)

        return model

# a function that runs the model on the normalized image and return the result

    def run_model(self, path):

        image = self.load_and_preprocess_image(path)

        normalized_image = self.normalize_image(image)

        model = self.load_model()

        expanded_image = np.expand_dims(normalized_image, axis=0)

        result = model.predict(expanded_image)

        return result

img_dircetory = os.path.join('Data', 'Binary_model', 'Images', 'malaria', 'images', '3dcd4f1b-ce43-4a34-b1ed-076bb42963b1.png')


result = Binary_Model().run_model(img_dircetory)
