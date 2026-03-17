## 1. BM25 Scoring Formula

BM25 computes the relevance score between a **query** and a **document**.

The scoring function is:

$$
BM25(q,d) = \sum\_{t \in q} IDF(t) \cdot \frac{f(t,d) (k_1 + 1)}{f(t,d) + k_1 \left(1 - b + b \cdot \frac{|d|}{avgdl}\right)}
$$

Where the score is calculated **for every query term** and then summed.

---

## 2. Meaning of Each Variable

### Query and Document

- **$q$** represents the search query.
- **$d$** represents a document in the corpus.

---

### Query Term

- **$t$** represents a term (word) present in the query.
- BM25 calculates a score contribution for **each query term**.

---

### Term Frequency

- **$f(t, d)$** represents the number of times term **t** appears in document **d**.
- A higher value indicates stronger evidence that the document is relevant.
- However, BM25 **limits the impact of very high frequencies**.

---

### Document Length

- **$|d|$** represents the total number of words in the document.
- This helps normalize scores so that long documents are not unfairly favored.

---

### Average Document Length

- **$avgdl$** represents the average document length across the entire corpus.

- It is calculated as:

$avgdl = \frac{\sum\_{d \in D} |d|}{N}$

Where:

- **D** is the set of all documents.
- **N** is the total number of documents.

---

### Parameter (k_1)

- **k₁** controls the **term frequency saturation**.
- It determines how strongly term frequency influences the score.

Typical range:

```
1.2 ≤ k1 ≤ 2.0
```

Interpretation:

- Small **k₁** → term frequency has weaker influence.
- Large **k₁** → term frequency grows more linearly.

---

### Parameter (b)

- **b** controls **document length normalization**.

Typical range:

```
0 ≤ b ≤ 1
```

Interpretation:

| b value | Meaning                          |
| ------- | -------------------------------- |
| 0       | No document length normalization |
| 1       | Full normalization               |
| 0.75    | Most commonly used value         |

---

## 3. Inverse Document Frequency (IDF)

BM25 uses a modified version of **Inverse Document Frequency**.

$IDF(t) = \log \left( \frac{N - n_t + 0.5}{n_t + 0.5} + 1 \right)$

Where:

- **$N$** = total number of documents
- **$n_t$** = number of documents containing term **t**

---

## 4. Intuition Behind the IDF Formula

- If a word appears in **many documents**, it provides little information.
- If a word appears in **few documents**, it strongly indicates relevance.

Examples:

| Word        | Documents Containing Word | IDF Effect |
| ----------- | ------------------------- | ---------- |
| the         | very many                 | very small |
| learning    | moderate                  | medium     |
| transformer | very few                  | large      |

Thus:

- **Rare terms receive higher weight**.
- **Common terms receive lower weight**.

---

## 5. Term Frequency Saturation

In traditional TF-IDF:

```
Score ∝ term frequency
```

This means repeating a word **100 times** would increase the score significantly.

BM25 corrects this behavior.

The saturation component:

$$
\frac{f(t,d)(k_1 + 1)}{f(t,d) + k_1}
$$

Behavior:

| Term Frequency | Effect              |
| -------------- | ------------------- |
| 1 → 2          | noticeable increase |
| 2 → 5          | smaller increase    |
| 5 → 20         | very small increase |

Thus BM25 ensures:

- Early occurrences of a word matter more.
- Repeated occurrences eventually **saturate**.

---

## 6. Document Length Normalization

The denominator term:

$$
1 - b + b \cdot \frac{|d|}{avgdl}
$$

controls document length influence.

Interpretation:

| Document Length      | Effect          |
| -------------------- | --------------- |
| shorter than average | score increases |
| average length       | neutral         |
| longer than average  | score decreases |

This prevents **long documents from dominating rankings**.

---

## 7. Mathematical Behavior of the Full Formula

The full BM25 equation balances **three signals simultaneously**:

| Component            | Role                                |
| -------------------- | ----------------------------------- |
| IDF                  | measures term importance in corpus  |
| TF saturation        | limits excessive term repetition    |
| length normalization | prevents bias toward long documents |

Final score is the **sum of contributions of all query terms**.

---

## 8. Why BM25 Works Well

BM25 works effectively because:

- It models **term importance probabilistically**.
- It avoids linear growth of term frequency.
- It accounts for differences in document size.
- It requires **only two tunable parameters**.
