# R&D Assignment Report

## Overview

This report presents the methodology used to estimate the unknown parameters of the provided parametric curve from the supplied dataset (`xy_data.csv`).

The objective was to determine the values of:

- θ (rotation angle)
- M (exponential growth coefficient)
- X (horizontal translation)

for the curve:

\[
x=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
\]

\[
y=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
\]

subject to the constraints:

- \(0^\circ < \theta < 50^\circ\)
- \(-0.05 < M < 0.05\)
- \(0 < X < 100\)
- \(6 < t < 60\)

---

# Methodology

## Step 1: Visual Inspection

The provided dataset contains a smooth oscillatory curve.

Initial observations suggested:

- A dominant linear trend.
- A periodic sinusoidal component.
- Increasing oscillation magnitude as the parameter increases.
- A global rotation and translation.

These observations matched the structure of the provided parametric equation.

---

## Step 2: Geometric Interpretation

The equation can be interpreted as a rotated coordinate system.

Let:

\[
dx=x-X
\]

\[
dy=y-42
\]

Applying inverse rotation gives:

\[
t=dx\cos(\theta)+dy\sin(\theta)
\]

and

\[
z=-dx\sin(\theta)+dy\cos(\theta)
\]

Substituting into the original equation yields:

\[
z=e^{M|t|}\sin(0.3t)
\]

This transformation separates the oscillatory component from the global rotation and translation.

---

## Step 3: Optimization

A numerical optimization approach was used.

For each candidate set of parameters:

\[
(\theta,M,X)
\]

the transformed coordinates were computed and compared against:

\[
e^{M|t|}\sin(0.3t)
\]

The objective function was defined as:

\[
MSE=
\frac{1}{N}
\sum_{i=1}^{N}
(z_i-z_{predicted,i})^2
\]

where:

\[
z_{predicted}=e^{M|t|}\sin(0.3t)
\]

The optimization searched within the parameter bounds provided in the assignment.

---

# Estimated Parameters

The optimization converged to:

| Parameter | Value |
|------------|---------|
| θ | 0.523598 rad |
| θ | 30° |
| M | 0.03 |
| X | 55 |

These values satisfy all assignment constraints.

---

# Reconstructed Curve

Substituting the recovered parameters:

\[
x=t\cos(0.523598)-e^{0.03|t|}\sin(0.3t)\sin(0.523598)+55
\]

\[
y=42+t\sin(0.523598)+e^{0.03|t|}\sin(0.3t)\cos(0.523598)
\]

for:

\[
6 \le t \le 60
\]

produces a curve that closely matches the supplied dataset.

---

# Validation

The reconstructed curve was compared against the provided points.

Validation steps:

1. Load dataset.
2. Estimate parameters.
3. Generate reconstructed curve.
4. Compute mean squared error.
5. Overlay reconstructed curve and original points.

The fitted curve aligned with the supplied data, indicating successful parameter recovery.

---

# Tools Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Desmos

---

# Challenges

The main challenge was that the parameter \(t\) was not explicitly provided in the dataset.

This was addressed by exploiting the rotational structure of the curve and transforming the coordinates into a form where the oscillatory component could be isolated and directly modeled.

---

# Conclusion

The unknown parameters of the curve were successfully recovered through geometric transformation and numerical optimization.

Final estimated values:

- θ = 30°
- M = 0.03
- X = 55

These parameters reconstruct the provided dataset while satisfying all assignment constraints.
