import streamlit as st
import app1
import style
import ca
import pix2pix

PAGES = {
    "Deep Dream": app1 ,
    "Style Transfer": style,
    "Cartoonization" : ca ,
    "Pix2Pix" : pix2pix
}
st.sidebar.title('SIP Project ')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()