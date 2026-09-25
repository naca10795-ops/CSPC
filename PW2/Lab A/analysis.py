import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)

t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

print("Mean acceleration:", a.mean())
print("Acceleration standard deviation:", a.std())

v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

largest_difference = np.max(np.abs(y_recovered - y))
print("Largest position difference:", largest_difference)

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 8))

# Position
axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")
axes[0].set_title("Position vs Time")

# Velocity
axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")
axes[1].set_title("Velocity vs Time")

# Acceleration
axes[2].plot(t, a)
axes[2].axhline(-9.81, linestyle="--", label="True -9.81 m/s²")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].set_xlabel("Time (s)")
axes[2].set_title("Acceleration vs Time")
axes[2].legend()

plt.tight_layout()
plt.savefig("motion.png")