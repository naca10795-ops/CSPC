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

| version              | time (s) |
|-----------------------|----------|
| pure-Python loop       | 3.9674   |
| NumPy (vectorised)     | 0.0004   |

Speed-up: 10424.03x faster

**Tests:** all passing? yes

**Conclusion:**
- The NumPy implementation is much faster than the pure-Python loop because it processes all atoms at once with vectorized operations instead of looping over each one individually in Python. Working through this lab reinforced how much overhead per-element Python loops add compared to array-based NumPy operations.