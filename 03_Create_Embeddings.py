import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
 
# Initialize a FAISS index with 384-dimensional embeddings
index = faiss.IndexFlatL2(384)
 
# Initialize a SentenceTransformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
 
# Define the directory containing the .md files
dir_path = 'data/split_files'
 
# Loop over the files in the directory
for file_name in os.listdir(dir_path):
    if file_name.endswith('.html'):
        print(f"Adding {file_name}")
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        # Get the embedding for the text using the model
        embedding = model.encode(text).reshape(1, -1)
        # Add the embedding to the index
        index.add(embedding)
 
# Save the index to disk
faiss.write_index(index, 'faiss_embeddings.index') 
