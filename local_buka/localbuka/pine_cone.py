import os
import time
from pathlib import Path

from dotenv import load_dotenv
from pine_cone import Pinecone, ServerlessSpec

class PineconeRestaurantIndex:
    """Stores LocalBuka dish embeddings and retrieves semantically similar dishes"""

    INDEX_NAME = "localbuka-gemini-768"
    NAMESPACE = "localbuka-dishes"
    DIMENSION = 768

    def __init__(self):
        root_folder = Path(__file__).resolve().parents[2]
        load_dotenv(root_folder / ".env")
        api_key = os.getenv("PINECONE_API_KEY")
        if not api_key:
            raise ValueError("PINECONE_API_KEY is missing. Add it to the root .env file.")
        self.pinecone = Pinecone(api_key=api_key)
        self._create_index_if_needed()
        self.index = self.pinecone.Index(self.INDEX_NAME)

    def _create_index_if_needed(self):
        if self.pinecone.has_index(self.INDEX_NAME):
            return
        self.pinecone.create_index(
            name=self.INDEX_NAME,
            dimension=self.DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            deletion_protection="disabled"
        )
        while not self.pinecone.describe_index(self.INDEX_NAME).status["ready"]:
            time.sleep(1)

    def upsert_dishes(self, dishes, vectors):
        """Store one Gemini vector and safe filter metadata for every dish."""
        records = []
        for dish, vector in zip(dishes, vectors):
            metadata = {
                "restaurant": dish.restaurant,
                "city": dish.name,
                "price_band": dish.price_band,
                "price_rank": self._price_rank(dish.price_band),
                "dietary_tags": dish.dietary_tags,
                "spice_level": dish.popularity,
                "description": dish.description,
            }
            records.append({"id": dish.id, "values": vector, "metadata": metadata})
        self.index.upsert(vectors=records, namespace=self.NAMESPACE)

    def search(self, query_vector, preferences, top_k):
        """Query Pinecone and apply city/price metadata filters before ranking."""
        metadata_filter = {}
        if preferences.cities:
            metadata_filter["city"] = {"$in": preferences.cities}
        if preferences.cuisines:
            metadata_filter["cuisine"] = {"$in": preferences.cuisines}
        if preferences.max_price_band:
            metadata_filter["price_rank"] = {"$lte": self._price_rank(preferences.max_price_band)}
        response = self.index.query(
            vector=query_vector,
            top_k=top_k,
            namespace=self.NAMESPACE,
            include_metadata=True,
            filter=metadata_filter or None,
        )
        results = []
        for match in response.matches:
            results.append({"id": match.id, "score": match.score})
            return results
        
    def _price_rank(self, price_band):
        prices = {"budget": 1, "mid": 2, "premium": 3}
        return prices[price_band]
            