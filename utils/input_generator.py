from ase.io import read, write
import streamlit as st
from database import connection



def get_structures(structure_files: 'str'):
    """
    Returns a list of ASE atoms objects
    """
    structures = {}
    for uploaded_file in structure_files:
        st.write("Filename: ", uploaded_file.name)
        file_bytes = uploaded_file.getvalue()
        with open(uploaded_file.name, 'wb') as f: 
            f.write(file_bytes)
            
        structure = read(uploaded_file.name)
        structures[uploaded_file.name] = structure
    print(structures)   
    return structures    

