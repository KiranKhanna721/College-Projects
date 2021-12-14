import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import streamlit as st
import ut
from ut import load_img, transform_img, tensor_to_image, imshow
import os
from PIL import Image
import tensorflow_hub as hub
import cv2

def app(): 
    os.environ['CUDA_VISIBLE_DEVICES'] = ""
    os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    @st.cache
    def load_model():
        hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
        return hub_model
    content_image = st.file_uploader("Choose an Content image...", type="jpg") 
    if content_image is not None:        
        style_image = st.file_uploader("Choose an Style image...", type="jpg") 
        if style_image is not None:
            content_image = content_image.read()
            content_image = transform_img(content_image)
            style_image = style_image.read()
            style_image = transform_img(style_image)
            model = load_model()
            stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
            final_image = tensor_to_image(stylized_image)
            st.image(final_image)
            
        