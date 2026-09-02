"""Gemini embedding and Pinecone retrieval logic for LocalBuka."""
from .models import PRICE_ORDER, Recommendation, VALID_DIETARY_TAGS, VALID_SPICE_LEVELS

class Recommender:
    """Find semantically relevant dishes while enforcing user safety constraints."""

    def __init__(self, catalogue, embedder, restaurant_index):
        self.catalogue = catalogue
        self.embedder = embedder
        self.restaurant_index = restaurant_index
        self.dishes_by_id = {}
        for dish in catalogue:
            self.dishes_by_id[dish.id] = dish

    def recommend(self, query_text, preferences, limit=5):
        """Embed the request, retrieve Pinecone matches, then double-check diet tags."""
        self._validate(preferences, limit)
        query_with_history = self._add_order_history(query_text, preferences.past_order_dish_ids)
        query_vector = self.embedder.embed_one_text(query_with_history)
        matches = self.restaurant_index.search(query_vector, preferences, top_k=limit * 5)

        recommendations = []
        for match in matches:
            dish = self.dishes_by_id.get(match["id"])
            if not dish:
                continue
            if not self._meets_dietary_requirements(dish, preferences.dietary_restrictions):
                continue
            score = round((match["score"] * 100) + (dish.popularity * 0.05), 1)
            reasons = self._build_reasons(dish, preferences, match["score"])
            recommendations.append(Recommendation(dish, score, reasons))
            if len(recommendations) == limit:
                break
        return recommendations
    
    def _validate(self, preferences, limit):
        if limit < 1:
            raise ValueError("limit must be at least 1")
        if preferences.max_price_band and preferences.max_price_band not in PRICE_ORDER:
            raise ValueError("max_price_band must be budget, mid, or premium")
        for restriction in preferences.dietary_restrictions:
            if restriction not in VALID_DIETARY_TAGS:
                raise ValueError(f"Unsupported dietary restriction: {restriction}")
        if preferences.spice_reference and preferences.spice_preference not in VALID_SPICE_LEVELS:
            raise ValueError("spice_preference must be mild, medium, or not")
    
    def _add_order_history(self, query_text, dish_ids):
        history_names = []
        for dish_id in dish_ids:
            dish = self.dishes_by_id.get(dish_id)
            if dish:
                history_names.append(dish.name)
        if not history_names:
            return query_text
        return query_text + ". The user previously enjoyed: " + ", ".join(history_names)
    
    def _meets_dietary_requirements(self, dish, restrictions):
        for restriction in restrictions:
            if restriction not in dish.dietary_tags:
                return False
        return True
    
    def _build_reasons(self, dish, preferences, similarity_score):
        reasons = [f"semantic match score: {similarity_score:.3f}"]
        if preferences.cities:
            reasons.append(f"available in {dish.city}")
        if preferences.max_price_band:
            reasons.append(f"within your {preferences.max_price_band} budget")
        if preferences.dietary_restrictions:
            reasons.append("meets your dietary requirement")
        if preferences.spice_preference and dish.spice_level == preferences.spice_preference:
            reasons.append(f"matches your {dish.spice_level} spice preference")
        return reasons