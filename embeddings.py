from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample texts
sentences = [
    "What is artificial intelligence?",
    "Explain machine learning",
    "How to cook pasta"
]

# Convert to embeddings
embeddings = model.encode(sentences)

# Print embeddings
print("Embeddings:\n")
for i, emb in enumerate(embeddings):
    print(f"Sentence: {sentences[i]}")
    print(f"Vector length: {len(emb)}\n")

# Compare similarity
print("Similarity Matrix:\n")
similarity = cosine_similarity(embeddings)
print(similarity)
