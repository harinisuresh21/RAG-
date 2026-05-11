# Day 4 — Similarity Search (Cosine Similarity)

## Objective

By the end of this lesson, you will:
- Understand how similarity between vectors is calculated
- Learn cosine similarity
- See how retrieval works in RAG
- Implement similarity search in Python

---

## 1. Why Similarity Matters

In RAG, we need to answer:

How do we find the most relevant document for a query?

We cannot compare raw text efficiently.

Instead:
- Convert text → embeddings
- Compare embeddings using similarity

---

## 2. What is Similarity?

Similarity measures how close two vectors are.

Higher similarity → more relevant  
Lower similarity → less relevant  

---

## 3. Cosine Similarity

Cosine similarity measures the angle between two vectors.

- Value ranges from -1 to 1
- 1 → very similar  
- 0 → unrelated  
- -1 → opposite  

---

## Formula

cos(θ) = (A · B) / (||A|| * ||B||)

Where:
- A · B = dot product
- ||A|| = magnitude of vector A

---

## 4. Why Cosine Similarity is Used

- Works well for high-dimensional vectors
- Focuses on direction, not magnitude
- Standard for semantic search

---

## 5. Example

Query:
"What is artificial intelligence?"

Documents:
- "AI is the simulation of human intelligence"
- "Cooking pasta recipe"

Result:
- AI document → high similarity  
- Cooking document → low similarity  

---

## 6. Role in RAG

Cosine similarity is used to:
- Compare query embedding with document embeddings
- Rank documents
- Retrieve top-k results

---

## 7. Workflow

1. Convert query to embedding  
2. Compare with all document embeddings  
3. Compute similarity scores  
4. Sort results  
5. Select top-k documents  

---

## 8. Python Implementation

Run the file:
python similarity_demo.py


---

## 9. Expected Output

You will see:
- Similarity scores between sentences
- Higher score = more similar

---

## 10. Key Insight

Similarity search is the core of retrieval.

Without it:
- RAG cannot find relevant data
- System becomes ineffective

---

## 11. Common Mistakes

### Using raw text comparison
Must use embeddings

---

### Ignoring normalization
Vectors should be comparable

---

### Choosing wrong similarity metric
Cosine similarity works best for most NLP tasks

---

## 12. Interview Questions

1. What is cosine similarity?
2. Why is cosine similarity used in RAG?
3. What happens if similarity is calculated incorrectly?
4. Difference between cosine similarity and Euclidean distance?

---

## Next Step

Day 5: Vector Databases (FAISS)
