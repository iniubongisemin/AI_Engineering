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


"SENTIMENT ANALYSIS"
from transformers import pipeline

my_pipeline = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print(pipeline("Wifi is slower than a snail today"))
RESPONSE = [{'label': 'NEGATIVE', 'score': 0.99}]

"GRAMMATICAL CORRECTNESS"
from transformers import pipeline
grammar_checker = pipeline(
    task="text-classification",
    model="abdulmatinomotoso/English_Grammar_Checker",
)

print(grammar_checker("He eat pizza everyday!"))
RESPONSE = [{'label': 'LABEL_ 0' , 'score': 0.99}]


"QNLI (Question Natural Language Inference)"
from transformers import pipeline

classifier = pipeline(
    task="text-classification",
    model="cross-encoder/qnli-electra-base"
)

classifier("Where is Seattle located?, Seattle is located in Washington state.")
RESPONSE = [{'label': 'LABEL_0' , 'score': 0.997}]


"DYNAMIC CATEGORY ASSIGNMENT"
classifier = pipeline(
    task="zero-shot-classification",
    model="facebook/bart-large-mnli"
)

text = "Hey Datacamp; we would like to feature your courses in our newsletter!"
categories = ["marketing", "sales", "support"]

output = classifier(text, categories)
print(f"Top Label: {output['Labels'][0]} with score: {output['scores'][0]}")

OUTPUT = "Top Label: support with score: 0.8183"


"QUESTION NATURAL LANGUAGE INFERENCE (QNLI)"
# Create the pipeline
classifier = pipeline(task="text-classification", model="cross-encoder/qnli-electra-base")

# Predict the output
output = classifier("Where is the capital of France?, Brittany is known for its stunning coastline.")
print(output)


"GRAMMATICAL CORRECTNESS"
# Create a pipeline for grammar checking
grammar_checker = pipeline(
  task="text-classification", 
  model="abdulmatinomotoso/English_Grammar_Checker"
)

# Check grammar of the input text
output = grammar_checker("I will walk dog")
print(output)


"DYNAMIC CATEGORY ASSIGNMENT"
text = "AI-powered robots assist in complex brain surgeries with precision."

# Create the pipeline
classifier = pipeline(task="zero-shot-classification", model="facebook/bart-large-mnli")

# Create the categories list
categories = ["politics", "science", "sports"]

# Predict the output
output = classifier(text, categories)
# Print the top label and its score
print(f"Top Label: {output['labels'][0]} with score: {output['scores'][0]}")


"SUMMARIZING LONG TEXT"
original_text = ""
# Create the summarization pipeline
summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum")

# Summarize the text
summary_text = summarizer(original_text)

# Compare the length
print(f"Original text length: {len(original_text)}")
print(f"Summary length: {len(summary_text[0]['summary_text'])}")


"ADJUSTING THE SUMMARY LENGTH"

#1 Generate a summary of original_text between 1 and 10 tokens
short_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_new_tokens=1, max_new_tokens=10)

short_summary_text = short_summarizer(original_text)

print(short_summary_text[0]["summary_text"])


#2 Repeat for a summary between 50 and 150 tokens
long_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_new_tokens=50, max_new_tokens=150)

long_summary_text = long_summarizer(original_text)
print(long_summary_text[0]["summary_text"])


"TOKENIZING TEXT WITH AutoTokenizer"
# Import necessary library for tokenization
from transformers import AutoTokenizer

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Split input text into tokens
tokens = tokenizer.tokenize("AI: Making robots smarter and humans lazier!")
# Display the tokenized output
print(f"Tokenized output: {tokens}")

"USING AUTOCLASSES"
from transformers import AutoModelForSequenceClassification
# Download the model and tokenizer
my_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
my_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the pipeline
my_pipeline = pipeline(task="sentiment-analysis", model=my_model, tokenizer=my_tokenizer)

# Predict the sentiment
output = my_pipeline("This course is pretty good, I guess.")
print(f"Sentiment using AutoClasses: {output[0]['label']}")