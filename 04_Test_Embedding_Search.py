import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
 
# Load the index from disk
index = faiss.read_index('faiss_embeddings.index')
 
# Initialize a SentenceTransformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
 
# Define the query text
query_text = 'How do I train an Alpaca?'
 
# Get the embedding for the query text using the model
query_embedding = model.encode(query_text).reshape(1, -1)
 
# Use the index to find the nearest neighbors to the query embedding
k = 5 # number of nearest neighbors to retrieve
distances, indices = index.search(query_embedding, k)
 
# Retrieve the corresponding documents based on the indices returned by FAISS
dir_path = 'data/split_files'
results = []
for i in range(k):
    file_name = os.listdir(dir_path)[indices[0][i]]
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'r') as f:
        text = f.read()
    results.append((file_name, text, distances[0][i]))
 
# Sort the results by rank
results = sorted(results, key=lambda x: x[2])
 
# Print the best ranked result
print(results[0])
