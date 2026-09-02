import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

class GeminiEmbedder:
    """This Embedder creates a 768-number embeddings using the Gemini API."""

    MODEL_NAME = "gemini-embedding-2"
    DIMENSION = 768

    def __init__(self):
        root_folder = Path(__file__).resolve().parents[2]
        load_dotenv(root_folder / ".env")
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing. Add it to the root .env file.")
        self.client = genai.Client(api_key=api_key)

    def embed_texts(self, texts):
        """This method sends one or more text strings to Gemini and returns their vectors"""
        vectors = []
        for text in texts:
            response = self.client.models.embed_content(
                model=self.MODEL_NAME,
                contents=text,
                cofig=types.EmbedContentConfig(output_dimensionality=self.DIMENSION),
            )
            vectors.append(response.embeddings[0].values)
        return vectors
    
    def embed_one_text(self, text):
        return self.embed_texts([text])[0]
    

