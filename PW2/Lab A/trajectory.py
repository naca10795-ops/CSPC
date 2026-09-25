import numpy as np
import matplotlib.pyplot as plt

# Read trajectory data
data = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)

t = data[:, 0]
x = data[:, 1]
y = data[:, 2]

# Calculate velocity components
vx = np.gradient(x, t)
vy = np.gradient(y, t)

# Calculate speed
speed = np.sqrt(vx**2 + vy**2)

# Plot trajectory
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Object Trajectory")
plt.grid()
plt.tight_layout()
plt.savefig("trajectory.png")
plt.close()

# Plot speed versus time
plt.figure(figsize=(8, 6))
plt.plot(t, speed)
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Speed vs Time")
plt.grid()
plt.tight_layout()
plt.savefig("speed.png")
plt.close()

print("Maximum speed:", speed.max(), "m/s")
print("Minimum speed:", speed.min(), "m/s")
