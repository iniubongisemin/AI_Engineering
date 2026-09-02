"""Command-line entry point for the LocalBuka assistant."""

from .assistant import FoodAssistant
from .data import CATALOGUE
from .embeddings import GeminiEmbedder
from .pine_cone import PineconeRestaurantIndex
from .recommender import Recommender


def main() -> None:
    embedder = GeminiEmbedder()
    restaurant_index = PineconeRestaurantIndex()
    assistant = FoodAssistant(Recommender(CATALOGUE, embedder, restaurant_index))
    print("Welcome to LocalBuka 😇.  'quit' to leave.")
    location = input("Type your city: ").strip() or None
    while True:
        try:
            message = input("Type what you want to eat: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return
        if message.lower() == "quit" or message.lower() == "exit":
            print("Thanks for using our platform, bye!")
            return
        print(f"LocalBuka: {assistant.reply(message, location)}")


if __name__ == "__main__":
    main()
