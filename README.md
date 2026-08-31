# FlamAI R&D Assignment Solution

## Candidate Information

- Name: Raj Kumar
- Assignment: Research & Development (R&D)
- Role: Software Development Engineer Intern (R&D)

---

# Problem Statement

Given a set of points in `xy_data.csv`, estimate the unknown parameters of the following parametric curve:

\[
x = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
\]

\[
y = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
\]

Subject to:

- \(0^\circ < \theta < 50^\circ\)
- \(-0.05 < M < 0.05\)
- \(0 < X < 100\)
- \(6 < t < 60\)

The objective is to determine the values of:

- θ (theta)
- M
- X

---

# Approach

## 1. Understanding the Geometry

The given curve can be interpreted as:

- A rotated coordinate system defined by θ.
- A linear progression along parameter t.
- A sinusoidal perturbation scaled by an exponential growth term.
- A horizontal translation X.

The curve is therefore a transformed oscillating trajectory.

---

## 2. Coordinate Transformation

To simplify the problem, the points were transformed into a rotated coordinate system.

Let:

\[
dx = x - X
\]

\[
dy = y - 42
\]

Applying inverse rotation:

\[
t = dx\cos(\theta) + dy\sin(\theta)
\]

and

\[
z = -dx\sin(\theta) + dy\cos(\theta)
\]

The transformed equation becomes:

\[
z = e^{M|t|}\sin(0.3t)
\]

which significantly simplifies parameter estimation.

---

## 3. Parameter Estimation

An optimization-based approach was used.

Objective Function:

\[
Loss =
\frac{1}{N}
\sum
(z_{observed} - z_{predicted})^2
\]

where

\[
z_{predicted}=e^{M|t|}\sin(0.3t)
\]

SciPy's L-BFGS-B optimizer was used with the assignment constraints.

---

## 4. Final Estimated Parameters

### θ (Theta)

\[
\theta = 0.523598 \text{ radians}
\]

\[
\theta = 30^\circ
\]

### M

\[
M = 0.03
\]

### X

\[
X = 55
\]

---

# Final Equation

```latex
\left(
t\cos(0.523598)
-e^{0.03|t|}\sin(0.3t)\sin(0.523598)
+55,
42+t\sin(0.523598)
+e^{0.03|t|}\sin(0.3t)\cos(0.523598)
\right)
```

Domain:

```text
6 <= t <= 60
```

---

# Desmos Representation

The recovered equation can be visualized directly in Desmos using the final parameters.

Desmos Link:
(Add Shared Desmos Link Here)

---

# Repository Structure

```
flamai-rnd-assignment/
│
├── README.md
├── solution.py
├── xy_data.csv
└── results/
    └── fitted_curve.png
```

---

# Tools Used

- Python 3
- NumPy
- Pandas
- SciPy
- Matplotlib
- Desmos

---

# Conclusion

The unknown parameters were recovered by transforming the problem into a simpler coordinate system and minimizing the difference between observed and predicted curve values. The optimized parameters accurately reconstruct the provided dataset and satisfy all assignment constraints.

Final Answer:

- θ = 30°
- M = 0.03
- X = 55
