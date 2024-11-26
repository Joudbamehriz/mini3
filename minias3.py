# -*- coding: utf-8 -*-
"""
@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_particles = 500  
num_steps = 1000  
snapshots = [10, 100, 500, 1000]  

x_positions = np.zeros(num_particles)
y_positions = np.zeros(num_particles)
trajectory_x = []
trajectory_y = []

for step in range(1, num_steps + 1):
    dx = np.random.choice([-1, 1], num_particles)  
    dy = np.random.choice([-1, 1], num_particles)
    x_positions += dx
    y_positions += dy
    if step in snapshots:
        trajectory_x.append(x_positions.copy())
        trajectory_y.append(y_positions.copy())

fig, axes = plt.subplots(1, len(snapshots), figsize=(18, 4), sharex=True, sharey=True)
for idx, snapshot in enumerate(snapshots):
    ax = axes[idx]
    ax.scatter(trajectory_x[idx], trajectory_y[idx], s=5, alpha=0.7)
    ax.set_title(f"Step {snapshot}")
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")

plt.tight_layout()
plt.show()
