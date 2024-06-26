from ase.io import read
import streamlit as st
import basis_set_exchange as bse
from pathlib import Path
from crystals import Crystal
from database import connection

class PyCrystal23Input:
    def __init__(self):
        self.CALCULATION_TYPES_DEFAULTS = {
            "Single Point Energy": ['END'],
            "Geometry Optimization": ['OPTGEOM', 'TOLDEG', '0.000010', 'TOLDEX', '0.000040', 'PRINTHESS', 'PRINTFORCES', 'PRINTOPT', 'END', 'END'],
            "Vibrational Frequencies": ['FREQCALC', 'INTENS', 'END', 'END'],
            "Equation of State": ['EOS', 'RANGE', '0.98 1.10 10','TOLDEG', '0.000010', 'TOLDEX', '0.000040', 'END', 'END']
        }

    def get_structures(self, structure_files):
        structures = {}
        for uploaded_file in [structure_files]:
            st.write("Filename:", uploaded_file.name)
            with open(uploaded_file.name, 'wb') as f:
                f.write(uploaded_file.getvalue())
            structure = read(uploaded_file.name)
            structures[uploaded_file.name] = structure
        return structures

    def get_formatted_basis_set(self, basis_set, ase_structures):
        return connection.query_basis(basis_set, ase_structures)

    def get_basis_references(self, basis_set, ase_structures):
        ref_list = []
        for structure in ase_structures.values():
            elements = structure.get_chemical_symbols()
            ref_list.append(bse.get_references(basis_set, elements=elements, fmt='bib'))
        return ' '.join(ref_list).replace("%", "")

    def get_minimal_lattice_parameters(self, spacegroup, lattice):
        """
        Get the minimal lattice parameters based on the spacegroup.

        This function takes a spacegroup number and a lattice parameter list
        as input and returns a modified lattice parameter list with reduced
        parameters based on the spacegroup. It is designed to simplify the lattice
        parameters for crystallographic calculations.

        Parameters:
        spacegroup (int): The spacegroup number to determine the crystal system.
        lattice (list): A list containing the lattice parameters [a, b, c, alpha, beta, gamma].

        Returns:
        list: A modified lattice parameter list based on the spacegroup. The returned
        list may have fewer elements depending on the crystal system.

        Crystal Systems:
        - Monoclinic (spacegroup 3-15): Angles alpha, beta, and gamma are checked for uniqueness.
        - If alpha == gamma and alpha != beta, the 'b' and 'c' lattice parameters are removed.
        - If alpha == beta and alpha != gamma, the 'c' lattice parameter is removed.
        - If beta == gamma and alpha != beta, the 'a' lattice parameter is removed.
        - Orthorhombic (spacegroup 16-75): The 'alpha', 'beta', and 'gamma' angles are ignored.
        - Tetragonal (spacegroup 75-143): The 'b' lattice parameter is removed.
        - Trigonal (spacegroup 143-168): The 'b' lattice parameter is removed.
        - Hexagonal (spacegroup 168-195): The 'b' lattice parameter is removed.
        - Cubic (spacegroup 195-231): Only the 'a' lattice parameter is kept.

        Note:
        - The function modifies the input list 'lattice' and returns the modified list.
        - The lattice parameter angles are in degrees.

        Example:
        spacegroup = 5
        lattice = [5.0, 4.0, 6.0, 90.0, 90.0, 120.0]
        minimal_lattice = get_minimal_lattice_parameters(spacegroup, lattice)
        print(minimal_lattice)
        # Output: [5.0, 6.0, 120.0]
        """
        
        a, b, c, alpha , beta, gamma = lattice

        if spacegroup <=2:
            return lattice

        if spacegroup in range(3,15):
            print("monoclinic")
            # check uniqeness of cell angles -- see CRYSTAL17 pg 20
            if alpha == gamma:
                print("Testing Uniqueness of angles")
                if alpha != beta:
                    print("b unique")
                    del lattice[3]
                    del lattice[5]
            elif alpha == beta:
                print("Testing Uniquness of Angles")
                if alpha != gamma:
                    print("c unique")
                    del lattice[3]
                    del lattice[4]
            elif beta == gamma:
                print("Testing Uniquness of Angles")
                if alpha != beta:
                    print("a unique")
                    del lattice[4]
                    del lattice[5]
            return lattice
        
        elif spacegroup in range(16, 75):
            print("Orthorombic")
            lattice = lattice[0:3]
            return lattice

        elif spacegroup in range(75, 143):
            print("Tetragonal")
            del lattice[1]
            return lattice

        elif spacegroup in range(143,168):
            print("Trigonal")
            del lattice[1]
            return lattice

        elif spacegroup in range(168, 195):
            print("Hexagonal")
            del lattice[1]
            return lattice

        elif spacegroup in range(195, 231):
            print("Cubic")
            lattice = lattice[0]
            return lattice


class PyCrystal23Input:
    def __init__(self):
        self.CALCULATION_TYPES_DEFAULTS = {
            "Single Point Energy": ['END'],
            "Geometry Optimization": ['OPTGEOM', 'TOLDEG', '0.000010', 'TOLDEX', '0.000040', 'PRINTHESS', 'PRINTFORCES', 'PRINTOPT', 'END', 'END'],
            "Vibrational Frequencies": ['FREQCALC', 'INTENS', 'END', 'END'],
            "Equation of State": ['EOS', 'RANGE', '0.98 1.10 10','TOLDEG', '0.000010', 'TOLDEX', '0.000040', 'END', 'END']
        }

    def get_structures(self, structure_files):
        structures = {}
        for uploaded_file in [structure_files]:
            st.write("Filename:", uploaded_file.name)
            with open(uploaded_file.name, 'wb') as f:
                f.write(uploaded_file.getvalue())
            structure = read(uploaded_file.name)
            structures[uploaded_file.name] = structure
        return structures

    def get_formatted_basis_set(self, basis_set, ase_structures):
        return connection.query_basis(basis_set, ase_structures)

    def get_basis_references(self, basis_set, ase_structures):
        ref_list = []
        for structure in ase_structures.values():
            elements = structure.get_chemical_symbols()
            ref_list.append(bse.get_references(basis_set, elements=elements, fmt='bib'))
        return ' '.join(ref_list).replace("%", "")

    def get_minimal_lattice_parameters(self, spacegroup, lattice):
        """
        Get the minimal lattice parameters based on the spacegroup.

        This function takes a spacegroup number and a lattice parameter list
        as input and returns a modified lattice parameter list with reduced
        parameters based on the spacegroup. It is designed to simplify the lattice
        parameters for crystallographic calculations.

        Parameters:
        spacegroup (int): The spacegroup number to determine the crystal system.
        lattice (list): A list containing the lattice parameters [a, b, c, alpha, beta, gamma].

        Returns:
        list: A modified lattice parameter list based on the spacegroup. The returned
        list may have fewer elements depending on the crystal system.

        Crystal Systems:
        - Monoclinic (spacegroup 3-15): Angles alpha, beta, and gamma are checked for uniqueness.
        - If alpha == gamma and alpha != beta, the 'b' and 'c' lattice parameters are removed.
        - If alpha == beta and alpha != gamma, the 'c' lattice parameter is removed.
        - If beta == gamma and alpha != beta, the 'a' lattice parameter is removed.
        - Orthorhombic (spacegroup 16-75): The 'alpha', 'beta', and 'gamma' angles are ignored.
        - Tetragonal (spacegroup 75-143): The 'b' lattice parameter is removed.
        - Trigonal (spacegroup 143-168): The 'b' lattice parameter is removed.
        - Hexagonal (spacegroup 168-195): The 'b' lattice parameter is removed.
        - Cubic (spacegroup 195-231): Only the 'a' lattice parameter is kept.

        Note:
        - The function modifies the input list 'lattice' and returns the modified list.
        - The lattice parameter angles are in degrees.

        Example:
        spacegroup = 5
        lattice = [5.0, 4.0, 6.0, 90.0, 90.0, 120.0]
        minimal_lattice = get_minimal_lattice_parameters(spacegroup, lattice)
        print(minimal_lattice)
        # Output: [5.0, 6.0, 120.0]
        """
        
        a, b, c, alpha , beta, gamma = lattice

        if spacegroup <=2:
            return lattice

        if spacegroup in range(3,15):
            print("monoclinic")
            # check uniqeness of cell angles -- see CRYSTAL17 pg 20
            if alpha == gamma:
                print("Testing Uniqueness of angles")
                if alpha != beta:
                    print("b unique")
                    del lattice[3]
                    del lattice[5]
            elif alpha == beta:
                print("Testing Uniquness of Angles")
                if alpha != gamma:
                    print("c unique")
                    del lattice[3]
                    del lattice[4]
            elif beta == gamma:
                print("Testing Uniquness of Angles")
                if alpha != beta:
                    print("a unique")
                    del lattice[4]
                    del lattice[5]
            return lattice
        
        elif spacegroup in range(16, 75):
            print("Orthorombic")
            lattice = lattice[0:3]
            return lattice

        elif spacegroup in range(75, 143):
            print("Tetragonal")
            del lattice[1]
            return lattice

        elif spacegroup in range(143,168):
            print("Trigonal")
            del lattice[1]
            return lattice

        elif spacegroup in range(168, 195):
            print("Hexagonal")
            del lattice[1]
            return lattice

        elif spacegroup in range(195, 231):
            print("Cubic")
            lattice = lattice[0]
            return lattice


    def write_input(self, input_dict):
        use_symmetry = input_dict['use_symmetry']
        structures = input_dict['structures']
        calc_type = input_dict['calc_type']
        calc_lines = self.CALCULATION_TYPES_DEFAULTS[calc_type]
        formatted_basis = self.get_formatted_basis_set(input_dict['user_basis'], structures)
        
        for filename, structure in structures.items():
            download_filename = f"{Path(filename).stem}_INPUT_{input_dict['user_basis']}_{input_dict['functional']}"
            with open(download_filename, 'w') as f:
                f.write(f"Parameters generated by PyCRYSTAL23: {input_dict['user_basis']}, {input_dict['functional']} \n")
                if structure.get_pbc()[0]:
                    crystal_object = Crystal.from_ase(structure)
                    spacegroup = crystal_object.symmetry()['international_number']
                    cell = structure.get_cell_lengths_and_angles()
                    f.write("CRYSTAL \n0 0 0 \n")
                    if use_symmetry == True:
                        with st.spinner('Calculating Asymmetric Unit ...'):
                            asymmetric_unit = crystal_object.asymmetric_cell()
                            if len(asymmetric_unit) == len(structure):
                                    spacegroup = 1
                        f.write(f"{spacegroup} \n")
                        minimal_lattice = self.get_minimal_lattice_parameters(spacegroup, cell)
                        f.write(' '.join(map(str, minimal_lattice)) + "\n")
                        f.write(f"{len(asymmetric_unit)} \n")
                        for atom in asymmetric_unit:
                            f.write(f"{atom.atomic_number} \t {'   '.join(map(str, atom.coords_fractional))} \n")
                    if use_symmetry == False:
                        f.write("1\n")
                        f.write(' '.join(map(str, cell)) + "\n")
                        f.write(str(len(structure)) + "\n")
                        for atom in crystal_object:
                            f.write(f"{atom.atomic_number}\t {'   '.join(map(str, atom.coords_fractional))} \n")
                    for line in calc_lines:
                        f.write(f"{line} \n")
                    for row in formatted_basis.values():
                        f.write(''.join(row))
                    f.write("99 0\nEND\nDFT \n")
                    f.write(f"{input_dict['functional']}-D \n" if input_dict['dispersion'] else f"{input_dict['functional']} \n")
                    f.write("XLGRID \nEND\n")
                    f.write(f"SHRINK \n{input_dict['shrink']}\n")
                    f.write(f"TOLDEE \n{input_dict['toldee']}\n")
                    f.write(f"TOLINTEG \n{input_dict['tolinteg']}\n")
                    f.write("END")
            with open(download_filename, 'r') as f:
                lines = f.read()
                st.download_button('Download INPUT', data=lines, file_name=download_filename)
            return lines