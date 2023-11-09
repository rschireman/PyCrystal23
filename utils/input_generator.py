from ase.io import read, write
import streamlit as st
from database import connection



def get_structures(structure_files: 'str'):
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
        # if uploaded_file.name.endswith('xyz'):
        #     st.warning('XYZ file detected, INPUT file will assume gas-phase calculation', icon="‼️")
        #     structure = read(uploaded_file.name)
        #     symbols = structure.get_chemical_symbols()
        #     positions = structure.get_scaled_positions() 
        #     return symbols, positions
        # else:
        #     structure = read(uploaded_file.name)
        #     symbols = structure.get_chemical_symbols()
        #     positions = structure.get_scaled_positions()    
        #     cell = structure.get_cell_lengths_and_angles()
        #     return symbols, positions, cell

