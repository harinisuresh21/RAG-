# RAG From Scratch 

A structured, hands-on course to learn **Retrieval-Augmented Generation (RAG)** from fundamentals to real-world applications.

This repository is designed as a step-by-step learning path covering:
- Core concepts
- Implementation details
- Advanced retrieval techniques
- Real-world projects

---

## Overview

Retrieval-Augmented Generation (RAG) is a system design pattern that combines:
- Information retrieval
- Large Language Models (LLMs)

Instead of relying only on model memory, RAG systems:
1. Retrieve relevant data
2. Inject it into prompts
3. Generate grounded responses

This approach reduces hallucination and enables working with:
- private data
- dynamic knowledge
- large document collections

---

## What You Will Learn

### Foundations
- How LLMs work (tokens, prompts, context)
- Limitations of LLMs
- Introduction to RAG architecture

### Core Components
- Embeddings
- Vector databases
- Similarity search
- Data ingestion pipelines

### RAG Pipeline
- Query → Retrieval → Generation
- Prompt construction
- Context optimization

### Advanced RAG
- Chunking strategies
- Semantic chunking
- Conversational RAG
- Multi-query retrieval
- Hybrid search
- Reranking techniques

### Projects
- Document-based chatbot
- Resume analyzer
- Knowledge base assistant

---

## Repository Structure
rag-course/
│
├── 01_basics/
│ ├── day1_intro.md
│ ├── day2_llm_basics.md
│
├── 02_embeddings/
│ ├── day3_embeddings.md
│ ├── embedding_demo.py
│
├── 03_vector_db/
├── 04_rag_pipeline/
├── 05_advanced_rag/
├── 06_projects/
│
├── utils/
├── requirements.txt
└── README.md

---

## Course Roadmap (15 Days)

### Week 1 — Foundations
- Day 1: Introduction to RAG  
- Day 2: How LLMs Work  
- Day 3: Embeddings  
- Day 4: Similarity Search  
- Day 5: Vector Databases (FAISS)  
- Day 6: Data Ingestion Pipeline  
- Day 7: First RAG Application  

---

### Week 2 — Improving Retrieval
- Day 8: Frameworks (LangChain / LlamaIndex)  
- Day 9: Prompt Engineering  
- Day 10: Handling Hallucination  
- Day 11: Advanced Retrieval  
- Day 12: Hybrid Search  
- Day 13: Reranking  

---

### Week 3 — Applications
- Day 14: Build Final Project  
- Day 15: UI + Deployment + Optimization  

---

## Getting Started

### 1. Clone the repository
git clone https://github.com/your-username/rag-course.git

cd rag-course

---

### 2. Install dependencies
pip install -r requirements.txt

---

### 3. Run example (Embeddings)
python 02_embeddings/embedding_demo.py

---

## Requirements

- Python 3.9+
- sentence-transformers
- scikit-learn
- faiss (for later modules)
- optional: LangChain / LlamaIndex

---

## Key Concepts Covered

- Embeddings and vector similarity
- Cosine similarity and nearest neighbor search
- Chunking strategies for long documents
- Retrieval optimization techniques
- Prompt engineering for grounded responses
- Trade-offs in RAG system design

---

## Learning Approach

This repository follows a structured approach:

- Each day contains:
  - Concept explanation
  - Code implementation
  - Practical insights

- Focus is on:
  - Understanding over memorization
  - System design thinking
  - Real-world applicability

---

## Common Mistakes in RAG

- Over-relying on the LLM instead of improving retrieval
- Poor chunking strategies
- Ignoring context window limitations
- Using low-quality embeddings
- Not evaluating retrieval quality

---

## Key Insight

RAG performance depends more on:
- Retrieval quality
- Chunking strategy
- Ranking methods

than on the LLM itself.

---

## Future Improvements

- Add evaluation metrics
- Add benchmarking for retrieval quality
- Add API-based deployment (Flask/FastAPI)
- Add UI using Streamlit
- Add real-world datasets

---

## License

This project is open-source and available for learning and educational purposes.

---

## Contributions

Contributions are welcome. You can:
- Improve explanations
- Add examples
- Extend projects

---

## Author

Created as a structured learning resource for mastering RAG systems from scratch.
