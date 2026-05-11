from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample sentences
sentences = [
    "What is artificial intelligence?",
    "Explain machine learning",
    "How to cook pasta"
]

# Convert sentences to embeddings
embeddings = model.encode(sentences)

# Define a query
query = "What is AI?"

# Convert query to embedding
query_embedding = model.encode([query])

# Compute similarity
similarities = cosine_similarity(query_embedding, embeddings)

# Print results
print(f"Query: {query}\n")

for i, score in enumerate(similarities[0]):
    print(f"Sentence: {sentences[i]}")
    print(f"Similarity Score: {score:.4f}\n")

# Sort results
print("Top Match:\n")
top_index = similarities[0].argmax()
print(sentences[top_index])
