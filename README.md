# its-from-scratch

A rigorously structured repository implementing Machine Learning, Deep Learning, Statistics, and Optimization algorithms **from scratch**, with emphasis on mathematical foundations, derivations, and algorithmic clarity.

This project prioritizes **theory-first understanding** over framework abstraction.

---

## Objective

Modern ML development often relies heavily on high-level libraries such as `scikit-learn`, `PyTorch`, and `TensorFlow`. While powerful, these abstractions can obscure the mathematical mechanisms driving the algorithms.

This repository focuses on:

- Deriving algorithms from first principles
- Understanding optimization dynamics
- Interpreting loss functions geometrically
- Connecting linear algebra and probability theory to implementation
- Translating mathematical derivations into clean, minimal code

The primary goal is **deep conceptual clarity**.

---

## Guiding Principles

- Derivation before implementation
- Matrix-form representations wherever applicable
- Minimal external dependencies
- No black-box API calls
- Clear separation between:
  - Intuition
  - Mathematical formulation
  - Optimization logic
  - Final implementation

---

## Repository Structure

```
its-from-scratch/
│
├── supervised_learning/
│ ├── linear_regression/
│ │ ├── intuition.md
│ │ ├── derivation.md
│ │ └── implementation.py
│ │
│ ├── logistic_regression/
│ │
│ ├── knn/
│ │
│ └── decision_tree/
│
├── neural_networks/
│ ├── perceptron/
│ ├── mlp/
│ └── backpropagation/
│
├── optimization/
│ ├── gradient_descent/
│ ├── momentum/
│ ├── rmsprop/
│ └── adam/
│
├── probability_statistics/
│ ├── mle/
│ ├── map/
│ ├── entropy/
│ └── kl_divergence/
│
└── notes/
```


Each algorithm directory typically contains:

- `intuition.md` — conceptual explanation
- `derivation.md` — mathematical formulation and proof
- `implementation.py` — minimal implementation using NumPy only

---

## Implemented / Planned Algorithms

### Supervised Learning
- Linear Regression (Normal Equation + Gradient Descent)
- Logistic Regression
- K-Nearest Neighbors
- Naive Bayes
- Decision Trees
- Random Forest (from tree ensembles)
- Support Vector Machine (primal intuition)

### Optimization Algorithms
- Batch Gradient Descent
- Stochastic Gradient Descent
- Mini-batch Gradient Descent
- Momentum
- RMSProp
- Adam (derived from exponential moving averages)

### Neural Networks
- Perceptron
- Multi-Layer Perceptron
- Backpropagation (full chain-rule derivation)
- Activation Functions and their gradients
- Regularization (L1, L2)
- Dropout (theoretical explanation)

### Linear Algebra & Dimensionality Reduction
- PCA (Eigenvalue decomposition approach)
- Singular Value Decomposition (SVD)
- Covariance matrix derivations

### Probability & Information Theory
- Maximum Likelihood Estimation
- Maximum A Posteriori Estimation
- Entropy
- Cross-Entropy
- KL Divergence
- Bias–Variance Decomposition

### Advanced Topics (Planned)
- Attention Mechanism (matrix-level interpretation)
- Transformer components from scratch
- GAN formulation
- Reinforcement Learning fundamentals

---

## Mathematical Emphasis

All derivations prioritize:

- Vectorized notation
- Gradient computation via matrix calculus
- Geometric interpretation of optimization
- Convexity analysis where applicable
- Loss surface intuition

Where relevant, we connect:
- MLE ↔ Cross-Entropy
- Regularization ↔ Bayesian priors
- Gradient Descent ↔ Taylor expansion
- PCA ↔ Variance maximization

---

## Recommended Learning Path

1. Linear Regression
2. Gradient Descent
3. Logistic Regression
4. Bias–Variance Decomposition
5. Neural Networks
6. Optimization Variants (Momentum, Adam)
7. PCA & SVD
8. Advanced Architectures

---

## Target Audience

- Machine Learning Engineers
- Data Scientists
- Interview Preparation (ML/DL roles)
- Students seeking theoretical clarity
- Practitioners transitioning from library usage to algorithmic depth

---

## Contribution Guidelines

Contributions are welcome under the following principles:

- Emphasize derivation clarity
- Avoid high-level ML frameworks
- Keep implementations minimal
- Include mathematical explanations
- Maintain consistent notation across modules

---

## Long-Term Vision

- Complete coverage of foundational ML algorithms
- Unified mathematical notation across the repository
- Interview-ready theoretical explanations
- Expansion into modern architectures with first-principles derivations

---

> Frameworks improve productivity.  
> Mathematics builds mastery.
