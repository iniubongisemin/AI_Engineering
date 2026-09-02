"""This is a bounded, data-grounded conversational layer for food discovery."""

from .models import PRICE_ORDER, UserPreferences
from .recommender import Recommender

class FoodAssistant:
    """Convert limited food-discovery language into catalogue-backed suggestions."""

    CUISINE_TERMS = {"nigerian": "nigerian", "local": "nigerian", "continental": "continental", "pasta": "continental", "falafel": "continental"}
    DIET_TERMS = {"vegan": "vegan", "vegetarian": "vegetarian", "halal": "halal", "gluten-free": "gluten-free", "gluten free": "gluten-free"}
    PRICE_TERMS = {"cheap": "budget", "affordable": "budget", "budget": "budget", "mid-range": "mid", "mid range": "mid", "premium": "premium", "fancy": "premium"}
    SPICE_TERMS = {"spicy": "hot", "hot": "hot", "medium spice": "medium", "mild": "mild", "not spicy": "mild"}

    def __init__(self, recommender: Recommender):
        self.recommender = recommender
        self._cities = {}
        for dish in recommender.catalogue:
            self._cities[dish.city.lower()] = dish.city

    def reply(self, message: str, location=None):
        """Produce a short answer containing only catalogue facts.

        The prototype intentionally does not use an LLM, so it cannot invent opening
        times, delivery coverage, prices, nutrition values, or restaurant claims. 
        """
        normalized = message.strip().lower()
        if not normalized:
                return "Tell me what you feel like eating, for example: 'cheap spicy Nigerian food in Lagos'."
        operational_terms = ["opening", "hours", "address", "phone", "reservation", "delivery"]
        for term in operational_terms:
            if term in normalized:
                return "I only have the sample menu catalogue, so I can't verify operational details. I can help you find a dish by city, budget, cuisine, diet, or spice level."
        preferences = self.parse_preferences(normalized, location)
        if "near me" in normalized and not preferences.cities:
            return "Which Nigerian city are you in? I currently support Lagos, Abuja, Port Harcourt, Ibadan, Enugu, Kano, and Benin City."
        results = self.recommender.recommend(normalized, preferences, limit=3)
        if not results:
            return "I couldn't find a compatible dish in this sample catalogue. Try relaxing one preference or choose another city."
        lines = ["Here are the best matches from the sample catalogue:"]
        for index, result in enumerate(results, start=1):
            dish = result.dish
            lines.append(f"{index}. {dish.name} - {dish.restaurant}, {dish.city} ({dish.price_band}, {dish.spice_level}). {result.reasons[0]}.")
        return "\n".join(lines)
    
    def parse_preferences(self, message, location=None):
        """Extract only terms supported by the catalogue; unknown text is ignored."""
        cities = []
        for city_name, city_value in self._cities.items():
            if self._contains(message, city_name):
                cities.append(city_value)
        if not cities and location and "near me" in message:
            canonical = self._cities.get(location.strip().lower())
            if canonical:
                cities.append(canonical)
        cuisines = self._matched_values(message, self.CUISINE_TERMS)
        dietary = self._matched_values(message, self.DIET_TERMS)
        price = self._best_price(message)
        spice = self._best_spice(message)
        return UserPreferences(self._remove_duplicates(cuisines), price, self._remove_duplicates(dietary), spice, self._remove_duplicates(cities))
    
    @staticmethod
    def _contains(message, term):
        "Use basic substring matching because the supported vocabulary is small."
        return term in message
    
    def _matched_values(self, message, terms):
        matches = []
        for term, value in terms.items():
            if self._contains(message, term):
                matches.append(value)
        return matches
    
    def _best_price(self, message):
        matches = self._matched_values(message, self.PRICE_TERMS)
        if not matches:
            return None
        cheapest_match = matches[0]
        for price_band in matches:
            if PRICE_ORDER[price_band] < PRICE_ORDER[cheapest_match]:
                cheapest_match = price_band
        return cheapest_match
    
    def _best_spice(self, message):
        if self._contains(message, "not spicy"):
            return "mild"
        matches = self._matched_values(message, self.SPICE_TERMS)
        return matches[0] if matches else None
    
    def _remove_duplicates(self, items):
        unique_items = []
        for item in items:
            if item not in unique_items:
                unique_items.append(item)
        return unique_items

        
        