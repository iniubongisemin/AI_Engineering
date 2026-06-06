from transformers import pipeline

gpt2_pipeline = pipeline(task="text-generation", model="openai-community/gpt2")

print(gpt2_pipeline("What if AI"))

"MODEL-CARD: https://huggingface.co/openai-community/gpt2"

"MAKING ADJUSTMENTS TO THE PIPELINE"
results = gpt2_pipeline("What if AI", max_new_tokens=10, num_return_sequences=2)

for result in results:
    print(result["generated_text"])

"""RESULTS:
What if AI had never existed?
What if AI could be really smarter than us?"""

"USING INFERENCE PROVIDERS"
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="together",
    api_key=os.environ["HF_TOKEN"]
)
"https://huggingface.co/docs/inference-providers/en/index"

"USING A CONVERSATIONAL INTERFACE"
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)

print(completion.choices[0].message)

"INFERENCING WITH HUGGING FACE MODELS"
from transformers import pipeline 

gpt2_pipeline = pipeline(task="text-generation", model="openai-community/gpt2")

# Generate three text outputs with a maximum length of 10 tokens
results = gpt2_pipeline("What if AI", max_new_tokens=10, num_return_sequences=2)

for result in results:
    print(result['generated_text'])