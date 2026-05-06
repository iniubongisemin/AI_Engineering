from OpenAI_API.openai import OpenAI

client = OpenAI(api_key="ENTER YOUR KEY HERE")

response = client.chat.completions.create(
    model="gpt-40-mini",
    messages=[{"role": "user", "content": "What is the OpenAI API?"}]
)

print(response.choices[0].message.content)

text = ""

"COST ESTIMATION"
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
"NB: Always estimate before deploying AI solutions."

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


"CONTROLLING RESPONSE RANDOMNESS"
response = client.chat.completions.create(
    model="gpt-40-mini",
    messages= [{"role": "user", "content": "Life is like a box of chocolates. "}],
    temperature=2
)
print(response.choices[0].message.content)


"PROMPT SETUP"
messages=[
{"role": "system",
"content": "You are a Python programming tutor who speaks concisely."},
{"role": "user",
"content": "What is the difference between mutable and immutable objects?"}]

"ADDING GUARDRAILS"

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": sys_msg},
    {"role": "user", "content": "Help me learn to swim."}
  ]
)

print(response.choices[0].message.content)

"UTILIZING THE ASSISTANT ROLE"
response = client.chat.completions.create(
model="gpt-40-mini",
messages=[
{
    "role": "system",
    "content": "You are a Python programming tutor who speaks concisely."
},
{
    "role": "user",
    "content": "How do you define a Python list?"
},
{
    "role": "assistant",
    "content": "Lists are defined by enclosing a comma-separated sequence of objects inside square brackets [ ]"
},
{
    "role": "user",
    "content": "What is the difference between mutable and immutable objects?"
}
]
)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)


"CODING A CONVERSION"
messages = [{
    "role": "system",
    "content": "You are a data science tutor who provides short, simple explanations."
}]

user_qs = ["Why is Python so popular?", "Summarize this in one sentence."]

for q in user_qs:
    print("User: ", q)
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choice[0].message.content, "\n")


"CREATING A CONVERSATION HISTORY"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."},
    {"role": "user", "content": "Explain what pi is."}
]

# Send the chat messages to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_completion_tokens=100
)

# Extract the assistant message from the response
assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}

# Add assistant_dict to the messages dictionary
messages.append(assistant_dict)
print(messages)


"CREATING AN AI CHATBOT"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

# Loop over the user questions
for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )
    
    # Append the assistant's message to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")

"LAST OUTPUT:"
"""
output:
    User:  Explain what pi is.
    Assistant:  Pi (π) is a mathematical constant representing the ratio of a circle's circumference to its diameter. It is an irrational number, approximately equal to 3.14159, meaning it cannot be expressed as a simple fraction and has an infinite number of non-repeating decimal places. Pi is used in various mathematical calculations involving circles, such as finding the area (A = πr²) and circumference (C = 2πr), where r is the radius. 
    
    User:  Summarize this in two bullet points.
    Assistant:  - Pi (π) is the ratio of a circle's circumference to its diameter, approximately equal to 3.14159, and is an irrational number.
    - It is used in calculations involving circles, such as area (A = πr²) and circumference (C = 2πr). 
    
"""