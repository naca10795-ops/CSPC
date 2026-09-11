import time
from decay import simulate, simulate_loop

N0 = 200_000
lam = 0.4
dt = 0.05
steps = 200

start = time.perf_counter()
simulate_loop(N0, lam, dt=dt, steps=steps)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, lam, dt=dt, steps=steps)
numpy_time = time.perf_counter() - start

print(f"Python loop: {loop_time:.4f} seconds")
print(f"NumPy:        {numpy_time:.4f} seconds")

speedup = loop_time / numpy_time
print(f"NumPy is {speedup:.2f}x faster")