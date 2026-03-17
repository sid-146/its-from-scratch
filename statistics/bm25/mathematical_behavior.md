<!-- Todo: Compare mathematical intuition and behavior and merge -->

# BM25 – Mathematical Intuition and Behavior

This section builds **deep intuition** about how BM25 behaves mathematically and why it performs better than TF-IDF.

---

## 1. Term Frequency Saturation Behavior

BM25 does not allow term frequency to grow linearly. Instead, it follows a **saturating curve**.

### Core Idea

- The contribution of a term increases **quickly at first**.
- After a few occurrences, additional repetitions add **very little value**.
- This reflects real-world intuition:
    - Seeing a word **2–3 times** is enough to confirm relevance.
    - Seeing it **50 times does not make it 25× more relevant**.

---

### Mathematical Representation

$$
BM25(q,d) = \sum\_{t \in q} IDF(t) \cdot \frac{f(t,d) (k_1 + 1)}{f(t,d) + k_1 \left(1 - b + b \cdot \frac{|d|}{avgdl}\right)}
$$

---

### Behavior Analysis

- When **f(t, d) is small**:
    - The numerator grows faster than the denominator.
    - Score increases significantly.

- When **f(t, d) is large**:
    - Denominator dominates.
    - Growth slows down (saturation effect).

---

### Intuition Table

| Term Frequency | BM25 Contribution |
| -------------- | ----------------- |
| 1              | significant       |
| 2              | strong increase   |
| 5              | moderate increase |
| 20             | almost constant   |

---

## 2. Effect of Parameter ($k_1$)

- **k₁ controls how fast saturation happens**

### Interpretation

| k₁ Value    | Behavior          |
| ----------- | ----------------- |
| small (≈1)  | fast saturation   |
| large (≈2+) | slower saturation |

---

### Intuition

- Low **$k_1$**:
    - Even a few occurrences are enough.
    - Prevents keyword stuffing.

- High **$k_1$**:
    - Allows term frequency to matter more.
    - Useful when repetition is meaningful.

---

## 3. Document Length Normalization Intuition

BM25 adjusts scores based on document length using:

$$
Norm = 1 - b + b \cdot \frac {|d|}{avgdl}
$$

---

### Why This is Needed

- Longer documents naturally contain more words.
- Without normalization:
    - Longer documents would rank higher unfairly.

---

### Behavior

| Document Type    | Effect    |
| ---------------- | --------- |
| shorter than avg | boosted   |
| equal to avg     | neutral   |
| longer than avg  | penalized |

---

### Intuition

- If a term appears **3 times in a short document**, it is more important.
- If the same term appears **3 times in a very long document**, it is less significant.

---

## 4. Effect of Parameter (b)

- **b controls how strongly document length affects the score**

### Interpretation

| b Value | Behavior               |
| ------- | ---------------------- |
| 0       | ignore document length |
| 1       | full normalization     |
| 0.75    | balanced (default)     |

---

### Intuition

- Low **b**:
    - Treats all documents equally regardless of length.

- High **b**:
    - Strongly penalizes long documents.

---

## 5. Combined Effect (TF + Length + IDF)

BM25 combines three ideas:

### Step-by-step effect

- A term contributes more if:
    - It appears in the document (**TF**)
    - It is rare in the corpus (**IDF**)
    - The document is not too long (**Normalization**)

---

## 6. Comparison with TF-IDF (Mathematical View)

### TF-IDF


$$
Score \propto TF \times IDF
$$

Problems:

- TF grows **linearly**
- No length normalization
- Long documents get higher scores

---

### BM25 Improvement

| Issue       | TF-IDF  | BM25 Fix        |
| ----------- | ------- | --------------- |
| TF growth   | linear  | saturating      |
| doc length  | ignored | normalized      |
| flexibility | none    | tunable (k₁, b) |

---

## 7. Visual Intuition (Conceptual)

Think of BM25 scoring as:

- **IDF → importance weight**
- **TF → evidence strength**
- **Normalization → fairness adjustment**

Final score:

```
Relevance = Importance × Adjusted Evidence
```

---

## 8. Why BM25 Produces Better Rankings

BM25 ranks documents better because:

- It avoids **overweighting repeated terms**.
- It avoids **bias toward long documents**.
- It balances **local relevance (TF)** and **global importance (IDF)**.
- It introduces **controlled flexibility via parameters**.

---

## 9. Edge Case Intuition

### Case 1: Very Common Words

- IDF becomes very small.
- Contribution to score is negligible.

---

### Case 2: Rare Words

- IDF becomes large.
- Even a single occurrence can strongly boost ranking.

---

### Case 3: Very Long Documents

- Length normalization reduces score.
- Prevents domination by large documents.

---

### Case 4: Query with Multiple Terms

- Scores are summed.
- Documents matching **more query terms** rank higher.

---

## 10. Mental Model Summary

You can think of BM25 as:

- **Step 1:** Is the word important globally? (IDF)
- **Step 2:** Does the document contain it enough? (TF saturation)
- **Step 3:** Is the document reasonably sized? (Normalization)
