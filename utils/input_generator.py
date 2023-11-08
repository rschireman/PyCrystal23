from ase.io import read, write
import streamlit as st


def get_cell_and_coordinates(structure_files: 'str'):
    for uploaded_file in structure_files:
        st.write("Filename: ", uploaded_file.name)
        file_bytes = uploaded_file.getvalue()
        with open(uploaded_file.name, 'wb') as f: 
            f.write(file_bytes)
        if uploaded_file.name.endswith('xyz'):
            pos = read(uploaded_file.name).get_positions()
            st.warning('XYZ file detected, INPUT file will assume gas-phase calculation', icon="‼️")
        else:
            structure = read(uploaded_file.name)
            positions = structure.get_scaled_positions()    
            cell = structure.get_cell_lengths_and_angles()
        
        return positions, cell

