"""Simple data containers used by the LocalBuka prototype."""

from dataclasses import dataclass, field


# Numbers make it easy to compare the three price bands.
PRICE_ORDER = {"budget": 1, "mid": 2, "premium": 3}
VALID_DIETARY_TAGS = ["vegetarian", "vegan", "halal", "gluten-free"]
VALID_SPICE_LEVELS = ["mild", "medium", "hot"]


@dataclass
class Dish:
    """Stores the details of one dish in the sample catalogue."""

    id: str
    restaurant: str
    city: str
    cuisine: str
    name: str
    price_band: str
    dietary_tags: list[str]
    spice_level: str
    popularity: int
    description: str


@dataclass
class UserPreferences:
    """Stores the optional preferences collected from a user."""

    cuisines: list[str] = field(default_factory=list)
    max_price_band: str = None
    dietary_restrictions: list[str] = field(default_factory=list)
    spice_preference: str = None
    cities: list[str] = field(default_factory=list)
    past_order_dish_ids: list[str] = field(default_factory=list)


@dataclass
class Recommendation:
    """Stores one ranked dish and the plain-English reasons for its score."""

    dish: Dish
    score: float
    reasons: list[str]
