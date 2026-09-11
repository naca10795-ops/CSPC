# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation (pure-Python and NumPy versions), tests verifying its behavior, and a speed comparison between the two implementations.

**Speed comparison (loop vs NumPy):**
- loop  : 3.9674 s
- numpy : 0.0004 s
- speed-up: 10424.03x faster

**Tests:** all passing? yes

**Conclusion:**
- The NumPy implementation is much faster than the pure-Python loop because it uses vectorized numerical operations instead of explicitly processing each atom with a Python loop.