from ase.io import read, write
import streamlit as st
from io import StringIO



def get_ase_coordinates(structure_files: 'str'):
    for uploaded_file in structure_files:
        st.write("Filename: ", uploaded_file.name)
        file_bytes = uploaded_file.getvalue()
        with open(uploaded_file.name, 'wb') as f: 
            f.write(file_bytes)
        if uploaded_file.name.endswith('xyz'):
            pos = read(uploaded_file.name).get_positions()
            st.warning('XYZ File detected, INPUT file will assume gas-phase calculation', icon="‼️")
        else:
            pos = read(uploaded_file.name).get_scaled_positions()    
        
        return pos    