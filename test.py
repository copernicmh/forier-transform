import numpy as np

w1 = -0.16
w2 = 0.26
w3 = -0.32
z1 = 0.6
z2 = 0.3
z3 = 0.2
Z_zeta = (z1 * np.cos(w1 * zeta))
''' generate synthetic R (radial distance) 
and Z (vertical height, relative to the horizontal center) 
cylindrical coordinate data

data = np.column_stack([psi_t_col, theta, zetad])
np.savetxt("trajectories.txt", data)
print("Done")