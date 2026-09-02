# Sample Gemini/Pinecone recommendation output

Generated with `python3 -m localbuka_case_study.run_examples` after ingesting the catalogue.

## Ada — budget-conscious vegan in Lagos

1. Spicy Beans & Plantain | Lekki Green Pot, Lagos | score 75.5 | semantic match score: 0.717; available in Lagos; within your budget budget; meets your dietary requirement
2. Akara & Pap Breakfast Bowl | Yaba Morning Buka, Lagos | score 73.8 | semantic match score: 0.702; available in Lagos; within your budget budget; meets your dietary requirement
3. Asaro with Fried Plantain | Eko Plant Kitchen, Lagos | score 73.8 | semantic match score: 0.697; available in Lagos; within your budget budget; meets your dietary requirement; matches your medium spice preference

## Tunde — hot, halal food in Abuja

1. Tuwo Shinkafa & Miyan Kuka | Wuse Buka House, Abuja | score 85.9 | semantic match score: 0.819; available in Abuja; within your mid budget; meets your dietary requirement
2. Ofada Rice & Ayamase Mushrooms | Capital Vegan Table, Abuja | score 78.5 | semantic match score: 0.745; available in Abuja; within your mid budget; meets your dietary requirement; matches your hot spice preference

Only two items meet all of Tunde’s stated city, Nigerian-cuisine, halal, and maximum-price constraints. Returning two is safer than relaxing a hard constraint.

## Chioma — mild continental choice in Lagos

1. Roasted Vegetable Pizza | Sabo Bistro, Lagos | score 71.7 | semantic match score: 0.682; available in Lagos; within your premium budget; meets your dietary requirement; matches your mild spice preference
2. Creamy Mushroom Pasta | The Continental Plate, Lagos | score 71.7 | semantic match score: 0.680; available in Lagos; within your premium budget; meets your dietary requirement; matches your mild spice preference
3. Falafel Bowl | Marina Mezze, Lagos | score 69.8 | semantic match score: 0.661; available in Lagos; within your premium budget; meets your dietary requirement; matches your mild spice preference

Similarity scores can change slightly if Gemini updates its embedding service. The city, cuisine, price, and dietary constraint checks remain deterministic.
