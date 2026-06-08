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


"HUGGINGFACE DATASETS"
"https://huggingface.co/datasets"
"https://huggingface.co/docs/datasets/loading"


"DOWNLOADING A DATASET"
from datasets import load_dataset

data = load_dataset("IVN-RIN/BioBERT_Italian")

"Split parameter"
data = load_dataset("IVN-RIN/BioBERT_Italian", split="train")
"https://huggingface.co/docs/datasets/loading"
"https://huggingface.co/docs/datasets/v2.15.0/loading"

"Filter for pattern ' bella '"
filtered = data.filter(lambda row: " bella " in row["text"])
print(filtered)

"https://huggingface.co/docs/datasets/process#select-and-filter"

"Select the first two rows"
sliced = filtered.select(range(2))
print(sliced)

"Extract the 'text' for the first row"
print(sliced[0]["text"])


"LOADING DATASETS EXERCISE"
# Load the "validation" split of the TIGER-Lab/MMLU-Pro dataset
my_dataset = load_dataset("TIGER-Lab/MMLU-Pro", split="validation")

# Display dataset details
print(my_dataset)


"MANIPULATING DATASETS"
# Filter the documents
filtered = wikipedia.filter(lambda row: "football" in row["text"])

# Create a sample dataset
example = filtered.select(range(1))

print(example[0]["text"])