"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure: left = observed data, right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: read the data
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# TODO 2: analytical decay curve
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: make 1x2 subplot with shared x and y axes
fig, axes = plt.subplots(1, 2, sharex=True, sharey=True)

axes[0].scatter(t, observed)
axes[0].set_title("Observed data")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Count")

axes[1].plot(t, analytical)
axes[1].set_title("Analytical")
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Count")

plt.tight_layout()

# TODO 4: save the figure
plt.savefig("figure.png")
