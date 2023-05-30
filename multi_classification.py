import os
import numpy as np
from PIL import Image as img
from skimage.transform import resize
from tensorflow.keras import preprocessing
from tensorflow.keras.models import save_model , load_model


class Image():

    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename


    def to_array(self):
       # current_directory = os.getcwd()
        image_path = os.path.join(current_directory, self.folder, self.filename)
        image = img.open(image_path)
        image_array = np.array(image)
        target_size = (100,100)
        resized_image = image.resize(target_size)
        resized_image_array = preprocessing.image.img_to_array(resized_image)

        resized = resized_image_array.astype(np.float32)
        normalized_resized = resized/255.0

        return normalized_resized


def preproc(file):

    image_array = np.array(file)
    target_size = (100,100)
    resized_image = file.resize(target_size)
    resized_image_array = preprocessing.image.img_to_array(resized_image)
    resized = resized_image_array.astype(np.float32)
    normalized_resized = resized/255.0

    return np.expand_dims(normalized_resized, axis=0)
