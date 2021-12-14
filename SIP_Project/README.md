# SIP Project
## Cartoonify an image 

In this project, we are cartoony an image and image to image translation using different algorithms. First, we convert an image (Image of my face) to a cartoon image using different algorithms. In the output, we will get a cartoon image of an input given image.

Second, we are applying style transfer and deep dream methods to an image. Style transfer takes two input images one is a content image (image of a person) and a style image(image of a painting) and blends them together so the output image looks like the content image, but “painted” in the style of the style reference image. Deep Dream takes an input image and visualizes the patterns learned by a neural network in the given image.

Third, Image to image translation takes two images as an input. It aims to transfer images from a source domain to a target domain while preserving the content representations.
## Website
### https://share.streamlit.io/kirankhanna721/sip_project/main/app.py
### Tools we used to develop a website 
opencv , different ml models , Gan  and streamlit (For web development)
#### The main file to run is app.py , We can run our project by typing
### streamlit run app.py
#### In terminal or command prompt .

## Models 
Cartoonify ,
Style transfer ,
Deep dream and 
Image to Image translation different models using different applications 
## Files 
style.py is for style transfer ,
ca.py is for cartoonify ,
deep.py is for deep dream ,
pix2pix.ipynb is for pixel2pixel model implementation
pix2pix.py is for pix2pix(streamlit) implementation
app1.py is for deep dream(streamlit) implementation .
## Photo of our website 
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/s1.jpg)

## Deep Dream
### Input Image 
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/deep.jpg)
### Output Image
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/deep1.jpg)
## Style transfer
### Input(Content Image)
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/dog.jpg)
### Input(Style Image)
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/style.jpg)
### Output Image 
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/style1.jpg)

## Cartoonify Image
### Input Image
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/cartoon.jpg)
### Output Images using different methods
### Pencil Sketch
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/ca1.jpg)
### Detail Enhancement
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/ca2.jpg)
### Bilateral Filter
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/ca3.jpg)
### White Box
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/ca4.jpg)
## Pix2Pix
### Input Image
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/pix.jpg)
### Output Image
![image](https://github.com/KiranKhanna721/SIP_Project/blob/main/images/pix1.jpg)
