from sentence_transformers import SentenceTransformer
import numpy as np
import faiss


def main():
    # -----------------------------
    # 1. Load embedding model
    # -----------------------------
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # -----------------------------
    # 2. Sample documents
    # -----------------------------
    documents = [
        "Artificial intelligence is the future of technology",
        "Machine learning is a subset of AI",
        "Deep learning uses neural networks",
        "Cooking pasta requires boiling water",
        "Data science involves statistics and programming"
    ]

    # -----------------------------
    # 3. Convert documents → embeddings
    # -----------------------------
    doc_embeddings = model.encode(documents)

    # Convert to float32 (required by FAISS)
    doc_embeddings = np.array(doc_embeddings).astype("float32")

    # -----------------------------
    # 4. Create FAISS index
    # -----------------------------
    dimension = doc_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Add vectors to index
    index.add(doc_embeddings)

    print(f"Total vectors in index: {index.ntotal}\n")

    # -----------------------------
    # 5. Query
    # -----------------------------
    query = "What is artificial intelligence?"
    query_embedding = model.encode([query]).astype("float32")

    # -----------------------------
    # 6. Search top-k results
    # -----------------------------
    k = 3
    distances, indices = index.search(query_embedding, k)

    # -----------------------------
    # 7. Display results
    # -----------------------------
    print(f"Query: {query}\n")
    print("Top Results:\n")

    for rank, idx in enumerate(indices[0]):
        print(f"{rank + 1}. {documents[idx]}")
        print(f"   Distance Score: {distances[0][rank]:.4f}\n")


if __name__ == "__main__":
    main()
