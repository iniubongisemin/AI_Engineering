import os
import numpy as np
import pandas as pd
from openai import OpenAI
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from scipy.spatial import distance

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

# CREATING & STORING EMBEDDINGS
# Load your OpenAI API key securely (do not hardcode in production)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set your OpenAI API key in the OPENAI_API_KEY environment variable.")

# Load the reviews dataset
reviews = pd.read_csv("womens_clothing_e-commerce_reviews.csv")

# Select the text column to embed (e.g., 'Review Text')
texts = reviews['Review Text'].dropna().astype(str).tolist()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Create embeddings for the first 10 reviews as an example (to avoid quota issues)
response = client.embeddings.create(
    model="text-embedding-3-small",
    # input=texts[:10]
    input=texts
)

# Extract embeddings
response_dict = response.model_dump()
embeddings = [item["embedding"] for item in response_dict["data"]]

# DIMENSIONALITY REDUCTION & VISUALIZATION
tsne = TSNE(n_components=2, perplexity=5)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

# Plotting Reviews
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])
plt.title("t-SNE of Review Embeddings")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.show()

# FEEDBACK CATEGORIZATION
# >> Semantic Search for: 'quality', 'fit', 'style', 'comfort'
words = ['quality', 'fit', 'style', 'comfort']

# Embed the Search Query
def create_embeddings(texts):
    # Accepts either a string or a list of strings
    if isinstance(texts, str):
        texts = [texts]
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    response_dict = response.model_dump()
    return [data["embedding"] for data in response_dict["data"]]

# Get embeddings for each word
word_embeddings = create_embeddings(words)

# ii. Compute the Cosine Distances
def find_n_closest(query_vector, embeddings, n=3):
    distances = []
    for index, embedding in enumerate(embeddings):
        dist = distance.cosine(query_vector, embedding)
        distances.append({"distance": dist, "index": index})
    distances_sorted = sorted(distances, key=lambda x: x["distance"])
    return distances_sorted[0:n]

# iii. Extract the texts with the smallest Cosine Distances
for word, word_emb in zip(words, word_embeddings):
    hits = find_n_closest(word_emb, embeddings)
    print(f"Word '{word}': Closest reviews:")
    for hit in hits:
        idx = hit["index"]
        print(f"  Review idx {idx}, distance {hit['distance']:.4f}, text: {texts[idx]}")

# SIMILARITY SEARCH FUNCTION
def closest_reviews(review, texts):
    # Ensure review is embedded as a single vector, not a list of vectors
    review_embedding = create_embeddings(review)[0]  # Get the first (and only) embedding
    text_embeddings = create_embeddings(texts)
    three_closest = find_n_closest(review_embedding, text_embeddings)
    most_similar_reviews = []

    for close in three_closest:
        idx = close["index"]
        most_similar_reviews.append(texts[idx])
        
    return most_similar_reviews

# APPLICATION OF SIMILARITY SEARCH FUNCTION
review =  "Absolutely wonderful - silky and sexy and comfortable"
most_similar_reviews = closest_reviews(review, texts)