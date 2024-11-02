import numpy as np
import matplotlib.pyplot as plt

# number of random walks to plot and number of steps each
n_repetitions = 5
n_steps = 100
# parameters of the random walk
p = 0.53
q = 1.0 - p

# open a figure for plitting
plt.figure()

# generate and plot several trajectories
for i in range(n_repetitions):
	trajectory = [0]
	for j in range(100):
		right_or_left = 1 if np.random.random()<p else -1
		trajectory.append(trajectory[-1] + right_or_left)
	plt.plot(trajectory)

# label the axis
plt.xlabel('steps', fontsize=16)
plt.ylabel('position', fontsize=16)
plt.tick_params(labelsize=12)
