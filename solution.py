import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Load data
df = pd.read_csv("xy_data.csv")

x = df["x"].values
y = df["y"].values


def objective(params):
    theta, M, X = params

    dx = x - X
    dy = y - 42

    # Rotate coordinates
    t = dx * np.cos(theta) + dy * np.sin(theta)

    observed = -dx * np.sin(theta) + dy * np.cos(theta)

    predicted = np.exp(M * np.abs(t)) * np.sin(0.3 * t)

    return np.mean((observed - predicted) ** 2)


bounds = [
    (0.0, np.deg2rad(50)),  # theta
    (-0.05, 0.05),          # M
    (0.0, 100.0)            # X
]

initial_guess = [
    np.deg2rad(25),
    0.01,
    50
]

result = minimize(
    objective,
    initial_guess,
    bounds=bounds,
    method="L-BFGS-B"
)

theta, M, X = result.x

print("\nRecovered Parameters")
print("-" * 30)
print(f"Theta (radians): {theta:.10f}")
print(f"Theta (degrees): {np.degrees(theta):.6f}")
print(f"M: {M:.10f}")
print(f"X: {X:.10f}")
print(f"MSE: {result.fun:.12e}")
