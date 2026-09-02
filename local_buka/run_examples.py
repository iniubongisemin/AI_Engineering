"""Render the required recommendation examples without API keys or network access."""

from .localbuka.data import CATALOGUE
from .localbuka.embeddings import GeminiEmbedder
from .localbuka.models import UserPreferences
from .localbuka.pine_cone import PineconeRestaurantIndex
from .localbuka.recommender import Recommender


EXAMPLES = {
    "Ada — budget-conscious vegan in Lagos": UserPreferences(
        cuisines=["nigerian"], max_price_band="budget", dietary_restrictions=["vegan"],
        spice_preference="medium", cities=["Lagos"],
    ),
    "Tunde — hot, halal food in Abuja": UserPreferences(
        cuisines=["nigerian"], max_price_band="mid", dietary_restrictions=["halal"],
        spice_preference="hot", cities=["Abuja"], past_order_dish_ids=["abu-01", "kan-01"],
    ),
    "Chioma — mild continental choice in Lagos": UserPreferences(
        cuisines=["continental"], max_price_band="premium", dietary_restrictions=["vegetarian"],
        spice_preference="mild", cities=["Lagos"],
    ),
}


def main() -> None:
    embedder = GeminiEmbedder()
    restaurant_index = PineconeRestaurantIndex()
    recommender = Recommender(CATALOGUE, embedder, restaurant_index)
    for label, preferences in EXAMPLES.items():
        print(f"## {label}")
        query_parts = preferences.cuisines + preferences.dietary_restrictions + preferences.cities
        if preferences.spice_preference:
            query_parts.append(preferences.spice_preference)
        query_parts.append("food")
        query_text = " ".join(query_parts)
        for position, result in enumerate(recommender.recommend(query_text, preferences, limit=3), 1):
            print(f"{position}. {result.dish.name} | {result.dish.restaurant}, {result.dish.city} | score {result.score} | {'; '.join(result.reasons)}")
        print()


if __name__ == "__main__":
    main()
