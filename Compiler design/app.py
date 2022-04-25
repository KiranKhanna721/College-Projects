import numpy as np
import streamlit as st
import inter
import lexana
PAGES = {
    'Intermediate code generator':inter,
    'Lexical Analyzer':lexana
}

st.sidebar.title('Compiler Design')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()