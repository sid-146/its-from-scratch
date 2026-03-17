# BM25 – Introduction and Intuition

## 1. What is BM25

- **BM25 (Best Matching 25)** is a ranking algorithm used in **information retrieval systems** to measure how relevant a document is to a search query.
- It is commonly used in **search engines** and **document retrieval systems**.
- BM25 belongs to the family of **bag-of-words retrieval models**, meaning that:
    - The order of words is ignored.
    - Only word frequencies and document statistics are considered.

- BM25 improves upon earlier methods such as **TF-IDF** by introducing:
    - **Term frequency saturation**
    - **Document length normalization**

- The algorithm assigns a **relevance score** between a query and each document in the corpus.
- Documents with **higher BM25 scores** are considered **more relevant to the query**.

---

## 2. Why BM25 is Needed

- Traditional TF-IDF has several limitations:
    - It assumes that **term frequency grows linearly with importance**.
    - It does **not properly normalize document length**.
    - Very long documents may receive **unfairly high scores**.

- BM25 addresses these problems by:
    - Limiting the influence of very frequent terms.
    - Adjusting scores based on document length.
    - Using tunable parameters to balance these effects.

---

## 3. Core Idea of BM25

BM25 estimates **how relevant a document is to a query** by considering three main signals:

### Term Frequency (TF)

- Measures how many times a query word appears in a document.
- A word appearing multiple times usually indicates higher relevance.
- However, repeating a word **too many times should not increase relevance indefinitely**.
- BM25 uses **frequency saturation** to limit this effect.

---

### Inverse Document Frequency (IDF)

- Measures how **rare a word is across all documents**.
- Words appearing in many documents are less informative.
- Rare words are more useful for identifying relevant documents.

Examples:

| Word        | Frequency in Corpus | Importance |
| ----------- | ------------------- | ---------- |
| the         | very high           | very low   |
| machine     | moderate            | medium     |
| transformer | rare                | high       |

---

### Document Length Normalization

- Long documents naturally contain more words.
- Without normalization, long documents might get **higher scores simply due to length**.
- BM25 adjusts the score based on how long the document is compared to the **average document length**.

---

## 4. Intuition Behind the BM25 Scoring Process

The BM25 ranking process can be understood as the following sequence:

1. **Break the query into words.**
2. **Check each word in every document.**
3. **Compute how important that word is in that document.**
4. **Adjust the score based on:**
    - how many times the word appears
    - how rare the word is
    - how long the document is

5. **Sum the scores of all query terms** to produce the final document score.

---

## 5. Why BM25 Became the Standard

- BM25 performs well in **large-scale text retrieval tasks**.
- It requires **no training data**.
- It is computationally efficient.
- It consistently outperforms simple TF-IDF in ranking quality.

Because of this, BM25 is widely used in systems such as:

- **Elasticsearch**
- **Apache Lucene**
- **OpenSearch**
- **Search engines in RAG pipelines**

---

## 6. High-Level Example

Suppose the query is:

```
machine learning model
```

Three documents exist:

| Document | Text                             |
| -------- | -------------------------------- |
| D1       | machine learning improves models |
| D2       | deep learning neural networks    |
| D3       | machine learning model training  |

BM25 evaluates:

- how often **machine**, **learning**, and **model** appear
- how rare these words are
- how long each document is

The final ranking might be:

| Document | BM25 Score | Rank |
| -------- | ---------- | ---- |
| D3       | highest    | 1    |
| D1       | medium     | 2    |
| D2       | lowest     | 3    |

---

## 7. Key Characteristics of BM25

- BM25 is a **probabilistic ranking function**.
- It assumes that **relevant documents share terms with the query**.
- It treats documents as **independent units**.
- It uses **two tunable parameters** to control scoring behavior.

---

## 8. Where BM25 is Used Today

BM25 is used in many modern systems:

### Search Engines

- It ranks webpages based on query relevance.

### Document Retrieval

- It retrieves relevant research papers or articles.

### Question Answering Systems

- It finds candidate documents before an LLM generates answers.

### Retrieval-Augmented Generation (RAG)

- BM25 acts as a **sparse retriever** for fetching documents before passing them to an LLM.
