import streamlit as st

# set basic page config
st.set_page_config(page_title="PyCRYSTAL23",
                    page_icon='U+269B',
                    layout='wide',
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
    # st.sidebar.write("Basis Set Name")
    basis_set = st.sidebar.selectbox("Basis Set", ('B3LYP', 'PBE', 'PBE0', 'BLYP', 
                                                   'PBESOL'))
    st.sidebar.write("XC Functional")
    st.sidebar.write("Calculation Type (select one)")
    uploaded_files = st.file_uploader("Upload Structure Files (any format accepted by the ASE will work, such as XYZ, PD, CIF, etc.)", accept_multiple_files=True)
    BASIS_SET = '6-31G(d,p)'
    structures = input_generator.get_structures(uploaded_files)
    formatted_basis = connection.query_basis(BASIS_SET, structures)
    print(formatted_basis)