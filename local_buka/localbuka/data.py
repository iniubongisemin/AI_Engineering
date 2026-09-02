"""This is a deliberately small, hand-curated Nigeria-first food catalogue."""

from .models import Dish

def dish(
        id: str, restaurant: str, city: str, cuisine: str, name: str, price_band: str,
        dietary_tags: list[str], spice_level: str, popularity: int, description: str,
) -> Dish:
    return Dish(id, restaurant, city, cuisine, name, price_band, dietary_tags, spice_level, popularity, description)


CATALOGUE = [
    dish("lag-01", "Buka on Adeola", "Lagos", "nigerian", "Smoky Jollof Rice & Grilled Chicken", "mid", ["halal"], "medium", 95, "Party-style jollof rice with charcoal-grilled chicken."),
    dish("lag-02", "Eko Plant Kitchen", "Lagos", "nigerian", "Asaro with Fried Plantain", "budget", ["vegan", "vegetarian", "halal", "gluten-free"], "medium", 82, "Yam porridge cooked with tomato, pepper and palm oil."),
    dish("lag-03", "Lagos Lagoon Seafood", "Lagos", "nigerian", "Peppered Catfish & Yam", "premium", ["halal", "gluten-free"], "hot", 88, "Whole catfish in a hot pepper sauce with boiled yam."),
    dish("lag-04", "Suya Junction", "Lagos", "nigerian", "Beef Suya Wrap", "budget", ["halal"], "hot", 91, "Spiced skewered beef, onions and tomatoes in a flatbread wrap."),
    dish("lag-05", "The Continental Plate", "Lagos", "continental", "Creamy Mushroom Pasta", "premium", ["vegetarian"], "mild", 75, "Tagliatelle, mushrooms and herb cream sauce."),
    dish("lag-06", "Iya Tinu's Kitchen", "Lagos", "nigerian", "Efo Riro & Amala", "mid", ["halal", "gluten-free"], "hot", 90, "Rich spinach stew with assorted meat and smooth yam flour."),
    dish("abu-01", "Wuse Buka House", "Abuja", "nigerian", "Tuwo Shinkafa & Miyan Kuka", "budget", ["halal", "gluten-free"], "medium", 81, "Northern rice swallow with baobab-leaf soup."),
    dish("abu-02", "Capital Vegan Table", "Abuja", "nigerian", "Ofada Rice & Ayamase Mushrooms", "mid", ["vegan", "vegetarian", "halal", "gluten-free"], "hot", 79, "Ofada rice with a green pepper mushroom stew."),
    dish("abu-03", "Jabi Grill", "Abuja", "continental", "Peri-Peri Chicken & Rice", "mid", ["halal", "gluten-free"], "hot", 87, "Flame-grilled chicken with spicy peri-peri sauce."),
    dish("abu-04", "Northern Spice Hub", "Abuja", "nigerian", "Kilishi Platter", "premium", ["halal", "gluten-free"], "hot", 72, "Air-dried, peanut-spiced beef with fresh vegetables."),
    dish("ph-01", "Creekside Pot", "Port Harcourt", "nigerian", "Fisherman Soup & Pounded Yam", "premium", ["halal", "gluten-free"], "hot", 86, "Seafood-rich Delta soup with pounded yam."),
    dish("ph-02", "Garden City Buka", "Port Harcourt", "nigerian", "Bole & Fish", "budget", ["halal", "gluten-free"], "medium", 93, "Roasted plantain and fish with a pepper sauce."),
    dish("ph-03", "Rivers Veggie Bowl", "Port Harcourt", "nigerian", "Beans & Dodo Bowl", "budget", ["vegan", "vegetarian", "halal", "gluten-free"], "mild", 78, "Honey beans, fried plantain and tomato stew."),
    dish("iba-01", "Oyo Heritage Kitchen", "Ibadan", "nigerian", "Abula Combo", "budget", ["halal", "gluten-free"], "medium", 84, "Amala with ewedu, gbegiri and tomato stew."),
    dish("iba-02", "Bodija Bowl", "Ibadan", "nigerian", "Afang Soup & Fufu", "mid", ["halal", "gluten-free"], "medium", 77, "Leafy afang soup served with cassava fufu."),
    dish("enu-01", "Coal City Kitchen", "Enugu", "nigerian", "Oha Soup & Pounded Yam", "mid", ["halal", "gluten-free"], "medium", 85, "Aromatic oha leaf soup with tender beef."),
    dish("enu-02", "Nsukka Rice Bar", "Enugu", "nigerian", "Coconut Jollof & Plantain", "budget", ["vegan", "vegetarian", "halal", "gluten-free"], "mild", 80, "Coconut-infused jollof rice and sweet fried plantain."),
    dish("kan-01", "Kano Kilishi Court", "Kano", "nigerian", "Masa & Miyan Taushe", "budget", ["vegetarian", "halal"], "mild", 76, "Rice cakes with a creamy pumpkin and groundnut soup."),
    dish("kan-02", "Arewa Flame Grill", "Kano", "nigerian", "Chicken Suya & Kuli-Kuli", "mid", ["halal", "gluten-free"], "hot", 89, "Spiced grilled chicken with groundnut crumble."),
    dish("ben-01", "Benin Pepper Pot", "Benin City", "nigerian", "Banga Soup & Starch", "mid", ["halal", "gluten-free"], "hot", 83, "Palm-fruit soup with local starch."),
    dish("lag-07", "Marina Mezze", "Lagos", "continental", "Falafel Bowl", "mid", ["vegan", "vegetarian", "halal"], "mild", 74, "Falafel, hummus, salad and flatbread."),
    dish("lag-08", "Yaba Morning Buka", "Lagos", "nigerian", "Akara & Pap Breakfast Bowl", "budget", ["vegan", "vegetarian", "halal", "gluten-free"], "mild", 73, "Bean cakes with warm millet pap and pepper sauce on the side."),
    dish("lag-09", "Lekki Green Pot", "Lagos", "nigerian", "Spicy Beans & Plantain", "budget", ["vegan", "vegetarian", "halal", "gluten-free"], "hot", 76, "Slow-cooked beans with ripe plantain and ata rodo sauce."),
    dish("lag-10", "Sabo Bistro", "Lagos", "continental", "Roasted Vegetable Pizza", "premium", ["vegetarian"], "mild", 71, "Stone-baked pizza with roasted peppers, mushroom and herbs."),
]
