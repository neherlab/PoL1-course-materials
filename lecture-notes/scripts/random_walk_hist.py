import numpy as np
import matplotlib.pyplot as plt

# number of random walks to plot and number of steps each
n_repetitions = 1000
n_steps = 100
# parameters of the random walk
p = 0.53
q = 1.0 - p

all_traj = []
# generate and plot several trajectories
for i in range(n_repetitions):
	trajectory = [0]
	for j in range(100):
		right_or_left = 1 if np.random.random()<p else -1
		trajectory.append(trajectory[-1] + right_or_left)
	all_traj.append(trajectory)

# open a figure for plitting
plt.figure()
# plot a histogram
all_traj = np.array(all_traj)
for t in [100, 30, 10]:
	plt.hist(all_traj[:,t], label=f"$n={t}$ steps",
			 alpha=0.5, bins=np.arange(-30,50,2))

plt.xlabel('position', fontsize=16)
plt.tick_params(labelsize=12)
plt.legend(fontsize=12, loc=2)
plt.xlim(-30, 30)
plt.savefig('figures/random_walk_histogram.pdf')