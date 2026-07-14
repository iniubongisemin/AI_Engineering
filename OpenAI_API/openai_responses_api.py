from openai import OpenAI

"FIRST RESPONSE API CALL"

# Define an OpenAI API client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the OpenAI API request
response = client.responses.create(
    model="gpt-5.4-mini",
    input="In simple terms, what is the OpenAI Responses API?",
    reasoning={"effort": "none"},
    max_output_tokens=100
)

# Print the generated text from the response
print(response.output_text)

"ADDING MODEL INSTRUCTIONS"
# Create a guardrailed AI response
response = client.responses.create(
    model="gpt-5.4-mini",
    instructions="You are a customer support AI that only answers questions about account balances and transaction history. Politely decline any other requests such as password resets.",
    input="Can you help me reset my password?"
)

print(response.output_text)


"EXTRACTING INFORMATION FROM THE RESPONSE"
response = {}
"1"
# Extract the number of output tokens
print(response.usage.output_tokens)
"2"
# Extract the response ID
print(response.id)
"3"
# Extract and print each item in the response
for item in response.output:
    print(item)


"EXPERIMENTING WITH MORE POWERFUL MODELS"
"1"
# Prompt gpt-5.4-nano with no reasoning
response = client.responses.create(
    model="gpt-5.4-nano",
    input='Write the same sentence in three tones: professional, sarcastic, and poetic. The sentence is: "The meeting could have been an email."',
  reasoning={"effort": "none"}
)

print(response.output_text)
"2"
# Prompt gpt-5.4-mini with no reasoning
response = client.responses.create(
    model="gpt-5.4-mini",
    input='Write the same sentence in three tones: professional, sarcastic, and poetic. The sentence is: "The meeting could have been an email."',
  reasoning={"effort": "none"}
)

print(response.output_text)
"3"
# Prompt gpt-5.5 with no reasoning
response = client.responses.create(
    model="gpt-5.5",
    input='Write the same sentence in three tones: professional, sarcastic, and poetic. The sentence is: "The meeting could have been an email."',
  reasoning={"effort": "none"}
)

print(response.output_text)


"REASONING ABOUT REASONING"
from datetime import time
start_time = time.time()
prompt = "How many of the letter 's' are in the sentence, 'Mississippi are possessive over their successes?'"

# Complete the challenge!
response = client.responses.create(
    model="gpt-5.4-mini",
    input=prompt,
    reasoning={"effort":"medium"},
    max_output_tokens=50
)

runtime = time.time() - start_time

print(response.output_text)
print(f"\nRuntime: {runtime:.2f} seconds")


"FROM ONE MESSAGE TO ANOTHER"
"1"
# Create the first request
response1 = client.responses.create(
    model="gpt-5.4-mini",
    input="Draft a short LinkedIn post announcing that I'm learning about the OpenAI Responses API to upskill in AI engineering on DataCamp!",
    reasoning={"effort": "none"}
)

# Extract the ID from response1
conversation_id = response1.id
print("Initial post:", response1.output_text)
"2"
# Create the first request
response1 = client.responses.create(
    model="gpt-5.4-mini",
    input="Draft a short LinkedIn post announcing that I'm learning about the OpenAI Responses API to upskill in AI engineering on DataCamp!",
    reasoning={"effort": "none"}
)

# Extract the ID from response1
conversation_id = response1.id
print("Initial post:", response1.output_text)

# Create the second request
response2 = client.responses.create(
    model="gpt-5.4-mini",
    input="Add more emojis to the post",
    reasoning={"effort": "none"},
    previous_response_id=conversation_id,
)

print("Revised post:", response2.output_text)


"EXTRACTING OUTPUT ITEMS & THEIR CONTENT"
# Loop through the output items
for item in response.output:
    # Check for reasoning items
    if item.type == 'reasoning':
        print('Found reasoning item')
    
    # Check for message items and extract text
    if item.type == 'message':
        message_text = item.content[0].text
        print(message_text)


"USING ITEMS FOR CUSTOM HANDLING"
# Loop through each item in the response output
for item in response.output:
    # Check if the item is a reasoning item
    if item.type == 'reasoning':
        if item.summary:
            print(f"Reasoning: {item.summary[0]}")
        else:
            print("No reasoning summary found.")   
    
    # Check if the item is a message item
    if item.type == 'message':
        print(f"Assistant: {item.content[0].text}")

    
"COMBINING LLMS & WEB SEARCH"
# Create a response with web search enabled
response = client.responses.create(
    model="gpt-5.4-mini",
    tools=[{"type": "web_search"}],
    input="What is the current temperature in Berlin, Germany?"
)

# Print the output text
print(response.output_text)

