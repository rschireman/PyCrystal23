from ase.io import read, write
import streamlit as st
import basis_set_exchange as bse
from database import connection

CALCULATION_TYPES_DEFUALTS = {"Single Point Energy": [''], 
                      "Geometry Optimization": ['OPTGEOM', 'TOLDEG', '0.000010', 'TOLDEX', '0.000040', 'PRINTHESS', 'PRINTFORCES', 'PRINTOPT', 'END'], 
                       "Frequencies": ['FREQCALC', 'INTENS', 'END'], 
                       "Equation of State": ['EOS', 'RANGE', '0.98 1.10 10','TOLDEG', '0.000010', 'TOLDEX', '0.000040', 'END']}

CRYSTAL_DEFAULTS = {'TOLDEE': '8', 'TOLINTEG': '7 7 7 7 14' }


def get_structures(structure_files: 'str'):
    """
    Returns a list of ASE atoms objects from structure file(s)
    """
    structures = {}
    for uploaded_file in structure_files:
        st.write("Filename: ", uploaded_file.name)
        file_bytes = uploaded_file.getvalue()
        with open(uploaded_file.name, 'wb') as f: 
            f.write(file_bytes)
            
        structure = read(uploaded_file.name)
        structures[uploaded_file.name] = structure

    return structures    

def get_formatted_basis_set(basis_set: 'str', ase_structures):
    formatted_basis = connection.query_basis(basis_set, ase_structures)
    return formatted_basis

def get_basis_references(basis_set: 'str', ase_structures):
    return bse.get_references(basis_set, elements=set(ase_structures.get_chemical_symbols()), fmt='bib')


