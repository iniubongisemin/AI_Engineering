import itertools

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


"FETCHING VECTORS"
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')
ids = ['2', '5', '8']

# Fetch the vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids=ids)

# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)


"RETURNING THE MOST SIMILAR VECTORS"
vector=[-0.250919762305275, ...]
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')

# Retrieve the top three most similar records
query_result = index.query(
    vector=vector,
    top_k=3
)

print(query_result)


"CHANGING DISTANCE METRICS"
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

# Create an index that uses the dot product distance metric
pc.create_index(
    name="dotproduct-index",
    dimension=1536,
    metric="dotproduct",
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

# Print a list of your indexes
print(pc.list_indexes())


"FILTERING QUERIES"
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with the year 2024
query_result = index.query(
    vector=vector,
    filter={
        "year": {"$eq": 2024}
    },
    top_k=1,
    include_metadatas=True
)
print(query_result)


"MULTIPLE METADATA FILTERS"
# Initialize the Pinecone client using your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with genre and year filters
query_result = index.query(
    vector=vector,
    top_k=1,
    filter={
        "genre": {"$eq": "thriller"},
        "year": {"$lt": 2018}
    }
)
print(query_result)


"UPDATING VECTOR VALUES"
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')

# Update the values of vector ID 7
index.update(
    id="7",
    values=vector
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=["7"])
print(fetched_vector)


"UPDATING VECTOR METADATA"
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')

# Update the metadata of vector ID 7
index.update(
    id="7",
    set_metadata={"genre": "thriller", "year": 2024},
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=["7"])
print(fetched_vector)


"DELETING VECTORS"
# Initialize the Pinecone client using your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')

# Delete vectors
index.delete(
    ids=["3", "4"]
)

# Retrieve metrics of the connected Pinecone index
print(index.describe_index_stats())


"DEFINING A FUNCTION FOR CHUNKING"
def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))


"BATCHING UPSERTS IN CHUNKS"
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')

# Upsert vectors in batches of 100
for chunk in chunks(vectors):
    index.upsert(vectors=chunk) 

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())


"BATCHING UPSERTS IN PARALLEL"
# Initialize the client
pc = Pinecone(api_key=api_key, pool_threads=20)

index = pc.Index('datacamp-index')

# Upsert vectors in batches of 200 vectors
with pc.Index('datacamp-index', pool_threads=20) as index:
    async_results = [index.upsert(vectors=chunk, async_req=True) for chunk in chunks(vectors, batch_size=200)]
    [async_result.get() for async_result in async_results]

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())


"NAMESPACES"
vector_set1 = [...]
vector_set2 = [...]
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)
index = pc.Index('datacamp-index')

# Upsert vector_set1 to namespace1
index.upsert(
  vectors=vector_set1,
  namespace="namespace1"
)

# Upsert vector_set2 to namespace2
index.upsert(
  vectors=vector_set2,
  namespace="namespace2"
)

# Print the index statistics
print(index.describe_index_stats())


"QUERYING NAMESPACES"
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

index = pc.Index('datacamp-index')

# Query namespace1 with the vector provided
query_result = index.query(
    vector=vector,
    namespace="namespace1",
    top_k=3
)
print(query_result)


"CREATING AND CONFIGURING A PINECONE INDEX"
# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=api_key)

# Create Pinecone index
pc.create_index(
    name='pinecone-datacamp', 
    dimension=1536,
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)

# Connect to index and print the index statistics
index = pc.Index("pinecone-datacamp")
print(index.describe_index_stats())