"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1
  2B: g(x) = x**4 - 3*x**2 + x + 5
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

def d2f(x):
    return 2.0

x0 = 0.0
lr = 0.1
x = x0

for _ in range(10000):
    step = lr * df(x)
    x = x - step

    if abs(step) < 1e-8:
        break

print("2A Gradient descent:", x)

x_newton = newton(df, x0, fprime=d2f)

print("2A Newton:", x_newton)

result = minimize(f, x0, method="SLSQP")

print("2A SLSQP:", result.x[0])

# ---------- 2B: harder landscape ----------
def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def d2g(x):
    return 12*x**2 - 6

print("\n2B from x0=0")

x0 = 0.0
lr = 0.1
x = x0

for _ in range(10000):
    step = lr * dg(x)
    x = x - step

    if abs(step) < 1e-8:
        break

print("Gradient descent:", x)

x_newton = newton(dg, x0, fprime=d2g)

print("Newton:", x_newton)
print("g'' at Newton result:", d2g(x_newton))

result = minimize(g, x0, method="SLSQP")

print("SLSQP:", result.x[0])

print("\n2B from x0=2")

x0 = 2.0
lr = 0.1
x = x0

for _ in range(10000):
    step = lr * dg(x)
    x = x - step

    if abs(step) < 1e-8:
        break

print("Gradient descent:", x)

x_newton = newton(dg, x0, fprime=d2g)

print("Newton:", x_newton)
print("g'' at Newton result:", d2g(x_newton))

result = minimize(g, x0, method="SLSQP")

print("SLSQP:", result.x[0])