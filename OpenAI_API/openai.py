from OpenAI_API.openai import OpenAI

client = OpenAI(api_key="ENTER YOUR KEY HERE")

response = client.chat.completions.create(
    model="gpt-40-mini",
    messages=[{"role": "user", "content": "What is the OpenAI API?"}]
)

print(response.choices[0].message.content)

text = ""

# Calculating the cost
prompt = f"""Summarize the customer support chat
in three concise key points: {text}"""

max_completion_tokens = 500

response = client.chat.completions.create(
    model="gpt-40-mini",
    messages= [{"role": "user", "content": prompt}], max_completion_tokens=max_completion_tokens
)

# Define price per token
input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens

# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")

"FIND & REPLACE"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt = """Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# MAKE A REQUEST TO THE CHAT COMPLETIONS ENDPOINT
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100
)

print(response.choices[0].message.content)