# BM25 – Worked Numerical Example

This section demonstrates a **complete step-by-step BM25 calculation** using a small dataset.
The goal is to make the computation **fully transparent and intuitive**.

---

## 1. Problem Setup

### Query

```id="q1ex"
machine learning
```

---

### Documents

| Document | Text                              |
| -------- | --------------------------------- |
| D1       | machine learning is fun           |
| D2       | machine learning machine learning |
| D3       | deep learning models              |

---

## 2. Step 1 — Preprocessing

### Tokenization

| Document | Tokens                               |
| -------- | ------------------------------------ |
| D1       | machine, learning, is, fun           |
| D2       | machine, learning, machine, learning |
| D3       | deep, learning, models               |

---

### Document Lengths

| Document | Length of $d$ |
| -------- | ------------- |
| D1       | 4             |
| D2       | 4             |
| D3       | 3             |

---

### Average Document Length

<!-- genui{"math_block_widget_always_prefetch_v2": {"content": "avgdl = \frac{4 + 4 + 3}{3} = 3.67"}} -->

$$
avgdl = \frac{4+4+3}{3} = 3.67
$$

---

## 3. Step 2 — Term Frequencies

We only consider query terms: **machine** and **learning**

| Document | f(machine, d) | f(learning, d) |
| -------- | ------------- | -------------- |
| D1       | 1             | 1              |
| D2       | 2             | 2              |
| D3       | 0             | 1              |

---

## 4. Step 3 — Document Frequencies

| Term     | Documents Containing Term (n_t) |
| -------- | ------------------------------- |
| machine  | 2 (D1, D2)                      |
| learning | 3 (D1, D2, D3)                  |

---

## 5. Step 4 — Compute IDF

Using BM25 IDF:

$$
IDF(t) = \log \left( \frac{N - n_t + 0.5}{n_t + 0.5} + 1 \right)
$$

Where (N = 3)

---

### IDF(machine)

<!--
genui{"math_block_widget_always_prefetch_v2": {"content": "IDF(machine) = \log\left(\frac{3 - 2 + 0.5}{2 + 0.5} + 1\right) \approx 0.47"}} -->

$$
IDF(machine) = log\left( \frac{3 - 2 + 0.5}{2 + 0.5} + 1\right) \approx 0.47
$$

---

### IDF(learning)

$$
IDF(learning) = og\left( \frac{3 - 3 + 0.5}{3 + 0.5} + 1\right) \approx 0.13
$$

---

### Intuition

- **machine** is rarer → higher importance
- **learning** appears everywhere → lower importance

---

## 6. Step 5 — Choose Parameters

We use standard values:

- (k_1 = 1.5)
- (b = 0.75)

---

## 7. Step 6 — Compute Normalization Factor

$$
Norm(d) = 1 - b + b \cdot \frac{|d|}{avgdl}
$$

---

### Compute for Each Document

- **D1:**

    $$
    1 - 0.75 + 0.75 \cdot \frac{4}{3.67} \approx 1.07
    $$

- **D2:**
  same as D1 → **1.07**

- **D3:**
    $$
    1 - 0.75 + 0.75 \cdot \frac{3}{3.67} \approx 0.86
    $$

---

## 8. Step 7 — Compute BM25 Term Scores

Formula:

$$
Score = IDF \cdot \frac{f(t,d)(k_1 + 1)}{f(t,d) + k_1 \cdot Norm(d)}
$$

---

### Document D1

#### machine (f = 1)

$$
Score \approx 0.47 \cdot \frac{1 \cdot 2.5}{1 + 1.5 \cdot 1.07}
\approx 0.47 \cdot 0.96 \approx 0.45
$$

#### learning (f = 1)

$$
Score \approx 0.13 \cdot 0.96 \approx 0.12
$$

**Total D1 Score ≈ 0.57**

---

### Document D2

#### machine (f = 2)

$$
Score \approx 0.47 \cdot \frac{2 \cdot 2.5}{2 + 1.5 \cdot 1.07}
\approx 0.47 \cdot 1.39 \approx 0.65
$$

#### learning (f = 2)

$$
Score \approx 0.13 \cdot 1.39 \approx 0.18
$$

**Total D2 Score ≈ 0.83**

---

### Document D3

#### machine (f = 0)

- No contribution → **0**

#### learning (f = 1)

$$
Score \approx 0.13 \cdot \frac{2.5}{1 + 1.5 \cdot 0.86}
\approx 0.13 \cdot 1.09 \approx 0.14
$$

**Total D3 Score ≈ 0.14**

---

## 9. Final Ranking

| Document | Score | Rank |
| -------- | ----- | ---- |
| D2       | 0.83  | 1    |
| D1       | 0.57  | 2    |
| D3       | 0.14  | 3    |

---

## 10. Interpretation of Results

- **D2 ranks highest** because:
    - It contains both terms multiple times.
    - Term frequency increases relevance but saturates.

- **D1 ranks second**:
    - Contains both terms once.
    - Still relevant but less strong.

- **D3 ranks lowest**:
    - Missing the word **machine**
    - Contains only a common term (**learning**)

---

## 11. Key Observations

- Rare terms (**machine**) contribute more than common terms (**learning**).
- Increasing term frequency improves score but with **diminishing returns**.
- Document length normalization slightly adjusts scores but does not dominate.

---

## 12. Takeaway

This example shows:

- BM25 is a **balanced scoring function**.
- It combines:
    - rarity (IDF)
    - presence (TF)
    - fairness (length normalization)

- The final ranking aligns well with **human intuition of relevance**.
