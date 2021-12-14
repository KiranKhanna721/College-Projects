import tensorflow as tf
import os
import numpy as np
import streamlit as st      
from keras.models import load_model             
import cv2  
import matplotlib.pyplot as plt 

def app():  
    model = load_model('pix2.h5')                   
    image = st.file_uploader("Choose an image...", type="jpg")    
    if image is not None:
        IMAGE_SIZE = [256, 256]
        image = tf.image.decode_jpeg(image.read(), channels=3)
        tempimage = image
        img_rows, img_cols, channels = 256, 256, 3
        image = tf.reshape(tf.cast(tf.image.resize(image, (int(img_rows), int(img_cols))), tf.float32) / 127.5 - 1, (1, img_rows, img_cols, channels))
        prediction = model(image, training=False)[0].numpy()
        fig, ax = plt.subplots(1, 2, figsize=(12, 12))
        ax[0].imshow(tempimage)
        ax[1].imshow(prediction * 0.5 + 0.5)
        ax[0].set_title("Input Photo")
        ax[1].set_title("Output Photo")
        ax[0].axis("off")
        ax[1].axis("off")
        st.pyplot(fig)                                                                   
