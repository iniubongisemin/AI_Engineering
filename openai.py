from openai import OpenAI

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
messages= [{"role": "user", "content": prompt}], max_completion_tokens=max_completion_tokens)

# Define price per token
input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000
# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")