import streamlit as st


# set basic page config
st.set_page_config(page_title="PyCRYSTAL23",
                    page_icon='U+269B',
                    layout='centered',
                    initial_sidebar_state='expanded')
from utils import input_generator
from database import connection

if __name__ == "__main__":
    st.title('PyCRYSTAL23')
    st.markdown("""
        PyCRYSTAL23 is a user-friendly Python tool designed to help you generate CRYSTAL23 input files with ease. 
        Whether you're a seasoned materials scientist or just starting with CRYSTAL23, this tool provides a simple and intuitive interface, 
        letting you focus on the science.
        ---
        """, unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Upload Structure Files (any format accepted by the ASE will work, such as XYZ, PD, CIF, etc.)", accept_multiple_files=True)

    
    items = connection.get_data()