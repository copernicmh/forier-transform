import numpy as np

iota = 0.42
num_turns = 80
num_points = 2000
psi_t = 0.16  # r = 0.4

zeta_continuous = np.linspace(0, num_turns * 2 * np.pi, num_points)
zeta_wrapped = zeta_continuous % (2 * np.pi)
theta = (iota * zeta_continuous) % (2 * np.pi)  # now advances at 0.42x rate
psi_t_col = np.full(num_points, psi_t)

header = """# psi_t theta zeta
# This file contains simple synthetic trajectory data with three whitespace-separated columns:
#   psi_t (toroidal flux; set psi_t = r**2 to choose radius r),
#   theta (poloidal angle, radians),
#   zeta (toroidal angle, radians).
# iota = 0.42, num_turns = 80, num_points = 2000, r = 0.40 (psi_t = 0.16)"""

data = np.column_stack([psi_t_col, theta, zeta_wrapped])
np.savetxt("trajectory_r=0.40_corrected.txt", data, fmt="%.6f", header=header, comments="")
print("Done")