import numpy as np
import matplotlib.pyplot as plt

"""
This file is a simple version of the experiment.
It includes the basic parameter setup, logic and calculation.
"""

# Configuration data
L = 100  # Reservoir length (in meter)
nx = 21  # Number of grid points
T0 = 200  # Reservoir temperature (in celsius)
T_inj = 60  # Injection temperature (in celsius)
alpha = 9 * (10 ** -7)  # Thermal diffusivity
v = 1.5 * (10 ** -5)  # Flow velocity

dt = 86400  # in seconds
dx = L / (nx - 1)
time_step = 1  # in days
simTime = 365 * time_step  # Total time duration

# initialization
T = [T0] * nx  # initial condition
T[0] = T_inj  # left boundary condition
T[-1] = T[-2]  # right boundary condition
T_outlet = [T[-1]]  # record the outlet temperature

# Update temperature
for curTime in range(1, simTime+1, time_step):
    T_new = [0] * nx  # re-initialize T_new list every time step
    T_new[0] = T_inj  # set left boundary condition

    # Update T_new using the formula
    for i in range(1, nx - 1):
        T_new[i] = T[i] + dt * (alpha * (T[i + 1] - 2.0 * T[i] + T[i - 1]) / dx ** 2 - v * (T[i] - T[i - 1]) / dx)

    T_new[-1] = T_new[-2]  # set right boundary condition
    T_outlet.append(T_new[-1])  # record the outlet temperature at the current time step
    T = T_new.copy()  # Update T as the input for the next time step

# Plot for output
plt.plot(np.arange(0, simTime+1, time_step), T_outlet, label='Outlet Temp VS. Days')
plt.xlim(0, simTime)
plt.xlabel('Time (days)')
plt.ylabel('Outlet Temperature (celsius)')
plt.title('1D Heat Transport')
plt.grid()
plt.legend()
plt.show()
