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
