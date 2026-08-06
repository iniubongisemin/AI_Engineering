import os

import chromadb
from matplotlib import pyplot as plt
import numpy as np
from openai import OpenAI
import pandas as pd
from sklearn.manifold import TSNE

# INSTALL USEFUL LIBRARIES
# Run this cell to install ChromaDB if desired
try:
    # assert version('chromadb') == '0.4.17'
    ...
except:
    # !pip install chromadb==0.4.17
    ...
try:
    # assert version('pysqlite3') == '0.5.2'
    ...
except:
    # !pip install pysqlite3-binary==0.5.2
    ...
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb


# Load your OpenAI API key securely (do not hardcode in production)
# You can set your API key as an environment variable: export OPENAI_API_KEY='sk-...'
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set your OpenAI API key in the OPENAI_API_KEY environment variable.")

# LOAD THE DATASET
# Load the reviews dataset
reviews = pd.read_csv("womens_clothing_e-commerce_reviews.csv")

# Select the text column to embed (e.g., 'Review Text')
# Make sure to drop NaNs and convert to a list of strings
texts = reviews['Review Text'].dropna().astype(str).tolist()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Create embeddings for the first 10 reviews as an example (to avoid quota issues)
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts[:10]
)

# Extract embeddings
response_dict = response.model_dump()

# FIX: Extract all embeddings, not just the first one
embeddings = [item["embedding"] for item in response_dict["data"]]

# Dimensional Reduction
tsne = TSNE(n_components=2, perplexity=5)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

# Plotting Reviews
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])
plt.title("t-SNE of Review Embeddings")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.show()

# Feedback Categorization
