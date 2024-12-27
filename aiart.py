import time
from tensorflow import keras
import keras_cv
import matplotlib.pyplot as plt

from PIL import Image

model = keras_cv.models.StableDiffusion(img_width =512,img_height= 512)

prompt = input("Enter the text: ")
images = model.text_to_image(prompt, batch_size=3) # 3 images will be generated

def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")

plot_images(images)