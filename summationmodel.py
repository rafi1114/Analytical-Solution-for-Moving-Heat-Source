## Importing python libraries

import numpy as np
import matplotlib.pyplot as plt


### Please set value of timestep here!!
### Demo values used in paper - 3e-4, 2e-4, 5e-5 

dt = 5e-5                   # reasonable value starts appearing and converges from 1e-4 and smaller timesteps (Rafi)

# Setting up constants for simulation
Q = 600                     # Ebeam Watts
eta = 0.83                   # Absorption efficiency
k = 11.4                    # Thermal conductivity (W/mK)
rho = 8192                  # Density
c = 435                     # Specific heat capacity (J/kgK)
a = k / (rho * c)           # Thermal diffusivity

# In meters
sigma_x = 0.00025            # ebeam size (assumed)
sigma_y = 0.00025           
sigma_z = 0.00025            
T0 = 1273                   # Initial preheat temperature (K)

# Setting up grid for simulation
x = np.linspace(-0.01, 0.0, 100)  
y = np.linspace(-0.004, 0.004, 40)  
X, Y = np.meshgrid(x, y)    # Creating the grid
Z = 0                       # For 2D
T = np.zeros_like(X) + T0   # Temperature distribution with preheated temp

# Ebeam coordinate
x_source = -0.01  
y_source = 0.00  
z_source = 0.0  


# Time parameters
t_final = 0.005                # Simulate up to this point in time (s)    
time_steps = int(t_final / dt) #Number of timesteps in the simulation

# Function to calculate temperature difference
def delT(x_rel, y_rel, z_rel, t_prime, t):
    phi_x = 12*a*(t - t_prime) + sigma_x**2
    phi_y = 12*a*(t - t_prime) + sigma_y**2
    phi_z = 12*a*(t - t_prime) + sigma_z**2
    exp_term = np.exp(-3 * (x_rel**2 / phi_x + y_rel**2 / phi_y + z_rel**2 / phi_z))
    return (2 * eta * Q) / (rho * c * (np.pi / 3)**(3/2)) * (1 / np.sqrt(phi_x * phi_y * phi_z)) * exp_term * dt

# Main loop
for t in range(1, time_steps):
    current_time = t * dt
    x_source += 0.01/time_steps  # Move heat source per time step
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            x_rel = X[i, j] - x_source
            y_rel = Y[i, j] - y_source
            z_rel = Z - z_source
            T_diff = delT(x_rel, y_rel, z_rel, current_time, t_final)
            T[i, j] += T_diff  

    print(f"Timestep: {t}/{time_steps}")

print("Max Temperature is: ", np.max(T))
plt.figure(figsize=(10, 4))
plt.contourf(X, Y, T, levels=200, cmap='bwr')
plt.colorbar(label='Temperature (K)')
plt.title(f'Temperature Distribution for Timestep = {dt}')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
