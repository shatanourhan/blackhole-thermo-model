import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import minimize

# Constants in natural units (G = c = hbar = k_B = 1)
G = 1

# Define symbolic variables for analytical calculations
m, q = sp.symbols('m q', real=True, positive=True)

# Free energy function
F = m - q**2 / (2 * m)

# First derivative (∂F/∂m) - Finding equilibrium points
dF_dm = sp.diff(F, m)

# Second derivative (∂²F/∂m²) - Checking stability
d2F_dm2 = sp.diff(dF_dm, m)

# Solve critical points analytically
critical_points = sp.solve([dF_dm], (m, q))

# Convert solutions to numerical values
def find_critical_points():
    return [(sol[0].evalf(), sol[1].evalf()) for sol in critical_points]

# Numerical free energy function
def free_energy(m, q):
    F = np.where(m**2 >= q**2, m - (q**2 / (2 * m)), np.nan)
    return F

# Hawking temperature function (T_H = κ / 2π, where κ is surface gravity)
def hawking_temperature(m, q):
    T = np.where(m**2 >= q**2, (1 / (4 * np.pi)) * (1 - q**2 / m**2), np.nan)
    return T

# Generate free energy landscape
def plot_free_energy():
    m_vals = np.linspace(1, 3, 100)
    q_vals = np.linspace(0, 2, 100)
    M, Q = np.meshgrid(m_vals, q_vals)
    F = free_energy(M, Q)
    
    plt.figure(figsize=(8, 6))
    plt.contourf(M, Q, F, levels=30, cmap='plasma')
    plt.colorbar(label='Free Energy F')
    plt.xlabel('Mass (m)')
    plt.ylabel('Charge (q)')
    plt.title('Free Energy Landscape of a Charged Black Hole')
    
    # Mark critical points
    critical_pts = find_critical_points()
    for cp in critical_pts:
        plt.scatter(cp[0], cp[1], color='red', marker='o', label='Critical Point')
    
    plt.legend()
    plt.show()

# Plot Hawking temperature
def plot_hawking_temperature():
    m_vals = np.linspace(1, 3, 100)
    q_vals = np.linspace(0, 2, 100)
    M, Q = np.meshgrid(m_vals, q_vals)
    T = hawking_temperature(M, Q)
    
    plt.figure(figsize=(8, 6))
    plt.contourf(M, Q, T, levels=30, cmap='inferno')
    plt.colorbar(label='Hawking Temperature T')
    plt.xlabel('Mass (m)')
    plt.ylabel('Charge (q)')
    plt.title('Hawking Temperature of a Charged Black Hole')
    plt.show()

# Run the visualizations
if __name__ == "__main__":
    plot_free_energy()
    plot_hawking_temperature()
