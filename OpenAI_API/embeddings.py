from openai import OpenAI
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from scipy.spatial import distance

"EMBEDDINGS"
# Create an OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to obtain embeddings
response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Software Engineering is morphing into AI Engineering!"
)

# Convert the response into a dictionary
response_dict = response.model_dump()
print(response_dict)


"DIGGING INTO THE EMBEDDINGS RESPONSE"
"#1"
print(response_dict["usage"]["total_tokens"])
"2"
# Extract the embeddings from response_dict
print(response_dict["data"][0]["embedding"])


"EMBEDDING PRODUCT DESCRIPTIONS"
products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics",
        "features": [
            "6.5-inch AMOLED display",
            "Quad-camera system with 48MP main sensor",
            "Face recognition and fingerprint sensor",
            "Fast wireless charging"
        ]
    },
    ...
]
# Extract a list of product short descriptions from products
product_descriptions = [product["short_description"] for product in products]

# Create embeddings for each product description
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=product_descriptions
)
response_dict = response.model_dump()

# Extract the embeddings from response_dict and store in products
for i, product in enumerate(products):
    product['embedding'] = response_dict["data"][0]["embedding"]
    
print(products[0].items())


"VISUALISING THE EMBEDDED DESCRIPTIONS"
"#1"
# Create categories and embeddings lists using list comprehensions
categories = [product["category"] for product in products]
embeddings = [product["embedding"] for product in products]
"#2"
# Reduce the number of embeddings dimensions to two using t-SNE
tsne = TSNE(n_components=2, perplexity=5)
embeddings_2d = tsne.fit_transform(np.array(embeddings))
"#3"
# Create a scatter plot from embeddings_2d
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])

for i, category in enumerate(categories):
    plt.annotate(category, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

plt.show()


"MORE REPEATABLE EMBEDDINGS"
# Define a create_embeddings function
def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  
  return [data['embedding'] for data in response_dict['data']]

# Embed short_description and print
short_description = "DataCamp is awesome!"
print(create_embeddings(short_description)[0])

# Embed list_of_descriptions and print
list_of_descriptions = ["Python is the best!", "R is the best!"]
print(create_embeddings(list_of_descriptions))


"FINDING THE MOST SIMILAR PRODUCT"
# Embed the search text
search_text = "soap"
search_embedding = create_embeddings(search_text)[0]

distances = []
for product in products:
  # Compute the cosine distance for each product description
  dist = distance.cosine(search_embedding, product["embedding"])
  distances.append(dist)

# Find and print the most similar product short_description    
min_dist_ind = np.argmin(distances)
print(products[min_dist_ind]["short_description"])