# PyCRYSTAL23

PyCRYSTAL23 is a user-friendly Python tool designed to help generate CRYSTAL23 input files with ease. Whether you're a seasoned materials scientist or just starting with CRYSTAL23, this tool provides a simple and intuitive interface, letting you focus on the science. Importatnly, it can automatically detect the symmetry in your crystal structure file (or any file read by the ASE that supports lattice information).

Symmetry detection in crystal structures is a crucial aspect of crystallography that involves identifying the symmetry elements and operations that define the spatial arrangement of atoms within a crystal. The process begins with the collection of structural data, typically obtained from X-ray diffraction experiments, which provide detailed information about atomic positions within the unit cell. This data is then used to create a crystal object in software that can be exploited to simplify calculations.


### Symmetry Operations

1. **Rotation**: A rotation operation can be described by an angle \(\theta\) around an axis. For example, a rotation by \(\theta\) about the \(z\)-axis is represented by the rotation matrix:
   \[
   R_z(\theta) = \begin{pmatrix}
   \cos\theta & -\sin\theta & 0 \\
   \sin\theta & \cos\theta & 0 \\
   0 & 0 & 1
   \end{pmatrix}
   \]

2. **Reflection**: A reflection across a plane, such as the \(xy\)-plane, can be represented by the matrix:
   \[
   M_{xy} = \begin{pmatrix}
   1 & 0 & 0 \\
   0 & 1 & 0 \\
   0 & 0 & -1
   \end{pmatrix}
   \]

3. **Inversion**: An inversion operation through a point (usually the origin) is given by:
   \[
   I = \begin{pmatrix}
   -1 & 0 & 0 \\
   0 & -1 & 0 \\
   0 & 0 & -1
   \end{pmatrix}
   \]

4. **Translation**: A translation operation moves every point by a fixed vector \(\mathbf{t} = (t_x, t_y, t_z)\), described by the translation vector:
   \[
   \mathbf{T} = \begin{pmatrix}
   t_x \\
   t_y \\
   t_z
   \end{pmatrix}
   \]

## Demo

Check out the demo, hosted via the Streamlit Cloud. Note: Finding symmetry with large structures (> 30 atoms) will result in an error.

https://pycrystal23-irahbptihfxaezi4c3qraj.streamlit.app

## Features

- **Intuitive Interface:** Easy-to-use interface for generating CRYSTAL23 input files.
- **User-Friendly:** Designed for both experienced materials scientists and beginners.
- **Efficient:** Streamlines the process of creating input files, saving you time and effort.

## Technical Design

[![](https://app.eraser.io/workspace/S41RIQHXRUOeDY5Dmbbc/preview?elements=8lZ_Xrc_TzNsYhMjGmMLAA&type=embed)](https://app.eraser.io/workspace/S41RIQHXRUOeDY5Dmbbc?elements=8lZ_Xrc_TzNsYhMjGmMLAA)