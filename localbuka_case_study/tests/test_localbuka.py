import unittest

from localbuka.assistant import FoodAssistant
from localbuka.data import CATALOGUE
from localbuka.models import UserPreferences
from localbuka.recommender import Recommender


class FakeEmbedder:
    """Avoids paid Gemini calls while testing the local application logic."""

    def __init__(self):
        self.last_text = ""

    def embed_one_text(self, text):
        self.last_text = text
        return [0.1, 0.2, 0.3]


class FakeRestaurantIndex:
    """Returns predictable Pinecone-like results without a network call."""

    def __init__(self):
        self.last_preferences = None

    def search(self, query_vector, preferences, top_k):
        self.last_preferences = preferences
        return [
            {"id": "lag-02", "score": 0.95},
            {"id": "lag-04", "score": 0.90},
            {"id": "lag-01", "score": 0.85},
        ]


class LocalBukaTests(unittest.TestCase):
    def setUp(self):
        self.embedder = FakeEmbedder()
        self.restaurant_index = FakeRestaurantIndex()
        self.recommender = Recommender(CATALOGUE, self.embedder, self.restaurant_index)
        self.assistant = FoodAssistant(self.recommender)

    def test_catalogue_exceeds_required_size(self):
        self.assertGreaterEqual(len(CATALOGUE), 20)

    def test_dietary_requirements_are_checked_after_vector_search(self):
        preferences = UserPreferences(dietary_restrictions=["vegan"])
        results = self.recommender.recommend("vegan food", preferences)
        self.assertTrue(results)
        self.assertTrue(all("vegan" in item.dish.dietary_tags for item in results))

    def test_recommender_sends_query_text_to_the_embedder(self):
        preferences = UserPreferences(cities=["Lagos"])
        self.recommender.recommend("cheap food near me", preferences)
        self.assertEqual(self.embedder.last_text, "cheap food near me")
        self.assertEqual(self.restaurant_index.last_preferences.cities, ["Lagos"])

    def test_past_order_names_are_added_to_the_embedding_query(self):
        preferences = UserPreferences(past_order_dish_ids=["lag-01"])
        self.recommender.recommend("something similar", preferences)
        self.assertIn("Smoky Jollof Rice", self.embedder.last_text)

    def test_assistant_parses_near_me_using_known_location(self):
        parsed = self.assistant.parse_preferences("I want something spicy and cheap near me", "Lagos")
        self.assertEqual(parsed.max_price_band, "budget")
        self.assertEqual(parsed.spice_preference, "hot")
        self.assertEqual(parsed.cities, ["Lagos"])

    def test_assistant_requests_location_when_near_me_is_ambiguous(self):
        reply = self.assistant.reply("I want something spicy and cheap near me")
        self.assertIn("Which Nigerian city", reply)

    def test_assistant_does_not_invent_operational_information(self):
        reply = self.assistant.reply("What are the opening hours of Buka on Adeola?")
        self.assertIn("can't verify operational details", reply)


if __name__ == "__main__":
    unittest.main()
