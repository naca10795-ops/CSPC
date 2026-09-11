# CSPC - Computer Science for Physics and Chemistry

## PW1 Lab A

### Automated tests

All 3 tests pass:

- `test_starts_at_N0`
- `test_rejects_negative_rate`
- `test_matches_law`

### Speed comparison

For a simulation of 200,000 atoms:

- Python loop: 3.9674 seconds
- NumPy: 0.0004 seconds
- Speed-up: 10424.03x

### Conclusion

The NumPy implementation is much faster than the pure-Python loop because it uses vectorized numerical operations instead of explicitly processing each atom with a Python loop.