"""Create Gemini embeddings for the sample dishes and store them in Pinecone."""

from .localbuka.data import CATALOGUE
from .localbuka.embeddings import GeminiEmbedder
from .localbuka.pine_cone import PineconeRestaurantIndex

def dish_to_text(dish):
    """Build the searchable sentence Gemini will convert into an embedding"""
    dietary_tags = ", ".join(dish.dietary_tags)
    return (
        f"{dish.name}. Restaurant: {dish.restaurant}. City: {dish.city}. "
        f"Cuisine: {dish.cuisine}. Price: {dish.price_band}. "
        f"Dietary tags: {dietary_tags}. Spice: {dish.spice_level}. "
        f"Description: {dish.description}"
    )

def main():
    embedder = GeminiEmbedder()
    restaurant_index = PineconeRestaurantIndex()
    dish_texts = []
    for dish in CATALOGUE:
        dish_texts.append(dish_to_text(dish))
    vectors = embedder.embed_texts(dish_texts)
    restaurant_index.upsert_dishes(CATALOGUE, vectors)
    print(f"Stored {len(CATALOGUE)} Gemini embeddings in the Pinecone index.")

if __name__ == "__main__":
    main()

