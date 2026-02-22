# Simple Linear Regression — From Scratch (Math Intuition)

## 1. Problem Statement

Given a dataset of paired observations:

\[
(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)
\]

we want to model the relationship between `x` (independent variable) and `y` (dependent variable) using a straight line.

Our hypothesis:
$$\hat{y} = mx + b$$

Where:

- \( m \) → slope  
- \( b \) → intercept  
- $\hat{y}$ → predicted value  

---

## 2. What Does “Best Fit” Mean?

There are infinitely many possible lines.

We need a definition of *best*.

For each data point:

$$ \text{residual}_i = y_i - \hat{y}_i $$

Residual = actual value − predicted value.

We want these residuals to be as small as possible.

---

## 3. Why Not Minimize Sum of Errors?

If we minimize:

$$ \sum (y_i - \hat{y}_i) $$

positive and negative errors cancel out.

This does not give a meaningful solution.

---

## 4. Least Squares Principle

To avoid cancellation, we square the residuals.

Objective function:

$$J(m, b) = \sum_{i=1}^{n} (y_i - (mx_i + b))^2$$

We choose \( m \) and \( b \) that minimize this function.

This is called **Ordinary Least Squares (OLS)**.

---

## 5. Why Squared Error?

1. Removes sign issue  
2. Penalizes large errors more  
3. Creates a smooth quadratic function  
4. Guarantees a single global minimum  

The loss surface is bowl-shaped (convex).

---

## 6. Solving for Optimal Parameters

We minimize the loss by:

$$ \frac{\partial J}{\partial m} = 0 $$

$$\frac{\partial J}{\partial b} = 0 $$

Solving these equations gives:

$$ m = \frac{\text{Cov}(x, y)}{\text{Var}(x)} $$

$$ b = \bar{y} - m\bar{x} $$

---

## 7. Interpretation of the Slope

$$ m = \frac{\text{Cov}(x, y)}{\text{Var}(x)} $$

- Covariance measures how x and y move together.
- Variance measures how x spreads by itself.

If covariance is:
- Positive → positive slope
- Negative → negative slope
- Zero → flat line

Slope measures **how strongly y changes per unit change in x**.

---

## 8. Important Geometric Insight

The regression line:

- Always passes through $(\bar{x}, \bar{y})$
- Minimizes vertical squared distances
- Makes residuals orthogonal to x

Mathematically:

$$ \sum x_i (y_i - \hat{y}_i) = 0 $$

This orthogonality condition is the core of regression.

---

## 9. Relation to Correlation

The slope can also be written as:

$$m = r \frac{\sigma_y}{\sigma_x}$$

Where:
-  $r$ = correlation coefficient
-  $\sigma_x$ = standard deviation of x
- $\sigma_y$ = standard deviation of y

Regression is correlation scaled by units.

---

## 10. Statistical Interpretation

We assume:

$$y = mx + b + \epsilon$$

Where:
- $\epsilon$ = noise
- $E[\epsilon] = 0$
- Errors are independent
- Constant variance (homoscedasticity)

Under Gaussian noise, least squares is also the **Maximum Likelihood Estimator**.

---

## 11. Conceptual Decomposition

$$y = \text{explained part} + \text{unexplained part}$$


Explained part → linear relationship  
Unexplained part → residual noise  

Least squares ensures residuals are orthogonal to the feature space.

---

## 12. Why Simple Linear Regression Matters

- Foundation of all linear models  
- Base case of multivariate regression  
- Core idea behind projection in linear algebra  
- Building block for deep learning (linear layer)  

---

## 13. Summary

Simple Linear Regression:

- Finds the best straight line
- Minimizes squared residuals
- Has closed-form solution
- Connects geometry, probability, and linear algebra

It is the first true example of optimization in machine learning.