import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Constants (setting G = c = hbar = k_B = 1 for natural units)
G = 1  # Gravitational constant

# Define Free Energy for Reissner-Nordström Black Hole
def free_energy(mass, charge, entropy):
    """Compute the free energy of a charged black hole."""
    return mass - entropy / 4 - charge**2 / (2 * mass)

# Compute critical points
def critical_point_solver():
    """Find critical points where phase transitions occur."""
    def equations(vars):
        mass, entropy, charge = vars
        eq1 = mass - entropy / 4 - charge**2 / (2 * mass)  # Free energy
        eq2 = 1 - 1 / (4 * mass) - charge**2 / (2 * mass**2)  # dF/dM = 0
        eq3 = -1 / (4 * mass**2) + charge**2 / (mass**3)  # d²F/dM² = 0
        return [eq1, eq2, eq3]
    
    initial_guess = [1.0, 1.0, 0.5]
    sol = opt.root(equations, initial_guess, method='hybr') 
    if sol.success:
        return sol.x
    else:
        raise ValueError("Critical point solver did not converge.")

# Plot Free Energy Landscape
def plot_free_energy():
    masses = np.linspace(1, 5, 200)  
    charges = np.linspace(0, 1, 200)  
    M, Q = np.meshgrid(masses, charges)
    S = 4 * np.pi * M**2  # Entropy approximation
    F = free_energy(M, Q, S)
    
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')  
    ax.plot_surface(M, Q, F, cmap='plasma', edgecolor='k', alpha=0.8)  
    ax.set_xlabel('Mass M')
    ax.set_ylabel('Charge Q')
    ax.set_zlabel('Free Energy F')
    ax.set_title("Black Hole Free Energy Phase Surface")
    plt.show()

# Run calculations
try:
    critical_point = critical_point_solver()
    print("Critical Point (Mass, Entropy, Charge):", critical_point)
    plot_free_energy()
except ValueError as e:
    print("Error:", e)
