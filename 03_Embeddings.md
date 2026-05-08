# Day 3 — Embeddings (Text to Vectors)

## Objective

By the end of this lesson, you will:
- Understand what embeddings are
- Learn how text is converted into vectors
- Understand semantic similarity
- Implement embeddings using Python

---

## 1. What are Embeddings?

Embeddings are numerical representations of text.

They convert text into vectors (arrays of numbers) so that machines can understand meaning.

### Example

Text:
"cat" → [0.12, -0.45, 0.88, ...]

"digital marketing" → [0.91, -0.12, 0.33, ...]

## Key Idea

Similar meanings → similar vectors

Example:
- "car" ≈ "vehicle"
- "king" ≈ "queen"
---

## 2. Why Embeddings Matter in RAG

RAG systems use embeddings to:
- Compare user queries with documents
- Find the most relevant information

Without embeddings:
- Only keyword matching is possible
- Semantic understanding is lost

---

## 3. Semantic Similarity

Instead of exact matching, embeddings allow:

Query:
"What is AI?"

Matches:
- "Artificial Intelligence basics"
- "Introduction to machine learning"

Even if words are different, meaning is similar.

---

## 4. How Embeddings Work (Conceptual)

Steps:
1. Input text
2. Model processes text
3. Output = vector (list of numbers)

These vectors exist in high-dimensional space.

---

## 5. Embedding Models

Popular models:
- sentence-transformers (recommended)
- OpenAI embeddings
- HuggingFace models

---

## 6. Python Implementation

We will use `sentence-transformers`.

---
pip install sentence-transformers

### Run the Code
python embedding_demo.py


---

## 7. Output Explanation

You will see:
- Long arrays of numbers
- Each number represents a dimension

Typical size:
- 384 / 768 / 1024 dimensions

---

## 8. Key Insight

Embeddings are the foundation of RAG.

Everything in RAG depends on:
- how well embeddings capture meaning
- how well similarity is computed

---

## 9. Common Mistakes

### Using wrong model
Not all embedding models are good for semantic search

### Ignoring preprocessing
Text cleaning improves results

### Comparing raw text instead of vectors
Similarity must be computed on embeddings

---

## 10. Interview Questions

1. What are embeddings?
2. Why are embeddings important in RAG?
3. How do embeddings help in similarity search?
4. What happens if embeddings are poor quality?

---

## Next Step

Day 4: Similarity Search (Cosine Similarity)


### Install Dependencies
pip install sentence-transformers
