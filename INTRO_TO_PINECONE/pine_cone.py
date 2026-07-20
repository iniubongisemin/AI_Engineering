from decouple import config

api_key = config("PINECONE_API_KEY")

"CREATING A PINECONE CLIENT"
# Import the Pinecone library
from pinecone import Pinecone

# Initialize the Pinecone client
pc = Pinecone(api_key=api_key)


"YOUR FIRST PINECONE INDEX"
# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

# Create your Pinecone index
pc.create_index(
    name="my-first-index",
    dimension=256,
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)


"CONNECTING TO AN INDEX"
# Set up the client with your API key
pc = Pinecone(api_key=api_key)

# Connect to your index
index = pc.Index("my-first-index")

# Print the index statistics
print(index.describe_index_stats())


"DELETING AN INDEX"
# Delete your Pinecone index
pc.delete_index("my-first-index")

# List your indexes
print(pc.list_indexes())


"CHECKING DIMENSIONALITY"
vectors = [
    {
        "id": "0",
        "values": [0.025525547564029694, ..., 0.0188823901116848],
        "metadata": {"genre": "action", "year": 2024}
    },
        ...,
]
# Create your Pinecone index
pc.create_index(
    name="datacamp-index", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)

# Check that each vector has a dimensionality of 1536
vector_dims = [len(vector['values']) == 1536 for vector in vectors]
print(all(vector_dims))


"INGESTING VECTORS WITH METADATA"
# Connect to your index
index = pc.Index("datacamp-index")

# Ingest the vectors and metadata
index.upsert(vectors=vectors)

# Print the index statistics
print(index.describe_index_stats())