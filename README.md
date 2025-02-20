# Black Hole Phase and Charged Black Hole Simulation

## Overview

This project analyzes the thermodynamic phase transitions of charged black holes, specifically focusing on the Reissner-Nordström black hole. The code calculates free energy landscapes and critical points to study phase transitions in black hole thermodynamics.

## Features

- **Free Energy Calculation**: Computes the free energy of a charged black hole using mass, charge, and entropy.
- **Critical Point Solver**: Uses numerical root-finding to determine phase transition points.
- **3D Free Energy Visualization**: Plots the free energy landscape over mass and charge parameters using an interactive 3D plot.
- **Hawking Temperature Analysis**: Computes the temperature of the black hole as a function of mass and charge.
- **Symbolic Computation**: Uses `sympy` for analytical calculations of equilibrium points and derivatives.

## Requirements

Ensure you have the following dependencies installed:

```bash
pip install numpy scipy matplotlib sympy
```

## Running the Simulation

Execute the Python script to compute critical points and generate the free energy landscape plot:

```bash
python black_hole_phase.py
```

## Explanation

- **Black Hole Thermodynamics**: The project models black holes as thermodynamic systems, where mass acts as internal energy and entropy is linked to horizon area.
- **Free Energy Function**: The free energy is given by:
    <img src="https://latex.codecogs.com/svg.latex?\large F = M - \frac{S}{4} - \frac{Q^2}{2M}" />
  where:
  - \(M\) is the mass of the black hole.
  - \(Q\) is the charge.
  - \(S = 4\pi M^2\) is the entropy approximation.
- **Hawking Temperature**: The Hawking temperature is computed as:
   <img src="https://latex.codecogs.com/svg.latex?\large T_H = \frac{1}{4\pi} \left(1 - \frac{Q^2}{M^2}\right)" />
  This helps analyze black hole stability and phase changes.
- **Critical Points**: The solver finds points where the first and second derivatives of free energy vanish, indicating phase transitions.

## Visualization

The script generates:

- A **3D Free Energy Surface**: Displays stability regions based on mass and charge.
- A **Hawking Temperature Contour Plot**: Shows how temperature varies across different black hole configurations.

