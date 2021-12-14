import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image
import cv2


def app():                       
    filters = st.sidebar.selectbox("Select filters",("Pencil Sketch","Detail Enhancement","Bilateral Filter","Pencil Edges","White Box"))
    st.write(filters)
    def resize_crop(image):
        h, w, c = np.shape(image)
        if min(h, w) > 720:
            if h > w:
                h, w = int(720*h/w), 720
            else:
                h, w = 720, int(720*w/h)
        image = cv2.resize(image, (w, h),interpolation=cv2.INTER_AREA)
        h, w = (h//8)*8, (w//8)*8
        image = image[:h, :w, :]
        return image
    image = st.file_uploader("Choose an image...", type="jpg") 
    if image is not None:
        image = Image.open(image)
        image = np.array(image)
        if filters == "Pencil Sketch":      
            st.write("Image will be converted into a sketch as if your image has been drawn using a pencil. ")         
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_blur = cv2.GaussianBlur(gray, (25, 25), 0)
            cartoon = cv2.divide(gray, gray_blur, scale=250.0)
            st.image(cartoon)
        elif filters == "Detail Enhancement":                    
            st.write("A cartoon effect by sharpening the image, smoothing the colors, and enhancing the edges. ")
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_blur = cv2.medianBlur(gray, 3)
            edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.detailEnhance(image, sigma_s=5, sigma_r=0.5)
            cartoon = cv2.bitwise_and(color, color, mask=edges) 
            st.image(cartoon)
            
        elif filters == "Bilateral Filter":                
            st.write("smooth the image and the colors while preserving the edge at the same time.")
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_blur = cv2.medianBlur(gray, 3)
            edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.bilateralFilter(image, 5, 50, 5)
            cartoon = cv2.bitwise_and(color, color, mask=edges) 
            st.image(cartoon)
            
        elif filters == "Pencil Edges":                           
            st.write("Pencil Edges filter creates a new image that contains only significant edges and white background. ")
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 25) 
            edges = cv2.Laplacian(gray, -1, ksize=3)
            edges_inv = 255-edges
            dummy, cartoon = cv2.threshold(edges_inv, 170, 255, cv2.THRESH_BINARY)
            st.image(cartoon)
            
        else:   
            interpreter = tf.lite.Interpreter(model_path="cartoon_gan.tflite")
            interpreter.allocate_tensors()
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()
            input_shape = input_details[0]['shape']
            image = cv2.resize(image, (256, 256),interpolation=cv2.INTER_CUBIC)
            image = image.astype(np.float32)/127.5 - 1
            image = image.reshape(input_shape)
            interpreter.set_tensor(input_details[0]['index'], image)
            interpreter.invoke()
            output = interpreter.get_tensor(output_details[0]['index'])
            output = (np.squeeze(output)+1)*127.5
            output = np.clip(output, 0, 255)
            cv2.imwrite('image.jpg',output)
            st.image('image.jpg')
            
        