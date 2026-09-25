# CSPC — Computer Science for Physics and Chemistry

My coursework repository for the course. Each practical lives under `PW<n>/Lab <X>/`.

## Setup

Create and activate the environment for a given lab:

conda env create -f "PW<n>/Lab <X>/environment.yml"
conda activate cspc

Run the tests for a lab from inside its folder:
cd "PW<n>/Lab <X>"
pytest -v

---

## PW1 — Lab A: Reproducible Foundations

**What I built:**

- A radioactive decay simulation (pure-Python loop and NumPy vectorised versions), a test suite verifying its behavior, and a speed comparison between the two implementations.

**Speed comparison (loop vs NumPy):**

| version | time (s) |
|---------|----------|
| pure-Python loop | 3.9674 |
| NumPy (vectorised) | 0.0004 |

- Speed-up: **10424.03× in this run**

**Tests:** 3/3 passing

**Conclusion:**

- The NumPy implementation is much faster than the pure-Python loop because it processes all atoms at once with vectorized operations instead of looping over each one individually in Python. Working through this lab reinforced how much overhead per-element Python loops add compared to array-based NumPy operations.

## PW1 — Lab B: Data, Plotting, and Automation

**What I built:**

* Read the observed radioactive decay data from `decay_observed.csv`.
* Compared the observed data with the analytical exponential decay law using `N0` equal to the first observed value and `λ = 0.3`.
* Created a 1×2 figure with shared x and y axes:

  * Left: scatter plot of the observed data.
  * Right: analytical exponential decay curve.
* Saved the generated figure as `figure.png`.

**Snakemake automation:**

* Created a `Snakefile` that uses `decay_observed.csv` as input and `figure.png` as output.
* Snakemake runs `plot.py` automatically when `figure.png` is missing or needs to be regenerated.
* When the output is already up to date, Snakemake correctly reports that nothing needs to be done.

**Conclusion:**

* The observed data shows the expected decreasing decay behavior, while the analytical model provides a smooth exponential curve for comparison.
* Snakemake makes the plotting workflow reproducible by automatically generating the figure from the input data.

## PW2 — Lab A: Motion from Tracking Data

**What I built:**

* Loaded noisy free-fall position measurements from `freefall.csv`.
* Used `np.gradient` to calculate velocity from position and acceleration from velocity.
* Mean acceleration: **-8.5797 m/s²**.
* Acceleration standard deviation: **28.7161 m/s²**.
* Integrated the noisy acceleration to recover velocity and then position.
* The largest difference between the recovered position and the original position was **0.7846 m**, which is within the expected 1 m range.
* Created `motion.png` containing position, velocity, and acceleration versus time, with the true `-9.81 m/s²` acceleration marked on the acceleration plot.

**Why is acceleration noisy?**

The original position measurements contain measurement noise. Differentiation amplifies this noise, and taking the derivative twice makes the acceleration much noisier than the original position data. This is why the acceleration has a large standard deviation even though the position data looks relatively smooth.

**What happened when integrating back?**

Integrating the noisy acceleration back to velocity and then position reduces the effect of the random high-frequency noise. The recovered position was close to the original measurements, with a maximum difference of only **0.7846 m**.

**Conclusion:**

This lab demonstrates that numerical differentiation is very sensitive to measurement noise, while integration can recover a smooth quantity from noisy derivative data.

### PW2 — Lab A Bonus: 2D Trajectory

**What I built:**

* Loaded the 2D tracking data from `trajectory.csv`, containing time, x-position, and y-position.
* Plotted the object's trajectory by plotting `x` against `y`.
* Used `np.gradient` to calculate the velocity components:
  * `vx = dx/dt`
  * `vy = dy/dt`
* Calculated the speed using `sqrt(vx² + vy²)`.
* Created `trajectory.png` showing the object's path.
* Created `speed.png` showing speed versus time.

**Results:**

* Minimum speed: **7.6690 m/s**
* Maximum speed: **38.6930 m/s**

**Conclusion:**

The trajectory data shows a looping, butterfly-shaped path. The speed changes over time as the object's motion changes along the x and y directions.
