from openai import OpenAI

message = ""

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Use the try statement
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[message]
    )
    # Print the response
    print(response.choices[0].message.content)
    # Use the except statement
except client.AuthenticationError:
    print("Please double check your authentication key and try again, the one provided is not valid.")


"AVOIDING RATE LIMITS WITH RETRY"

# Import the tenacity library
from tenacity import (
    retry, 
    wait_random_exponential, 
    stop_after_attempt
  )

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Add the appropriate parameters to the decorator
@retry(wait=wait_random_exponential(min=5, max=40), stop=stop_after_attempt(4))
def get_response(model, message):
    response = client.chat.completions.create(
      model=model,
      messages=[message]
    )
    return response.choices[0].message.content
print(get_response("gpt-4o-mini", {"role": "user", "content": "List ten holiday destinations."}))


"BATCHING MESSAGES"
measurements = []
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = []
# Provide a system message and user messages to send the batch
messages.append({
    "role": "system",
    "content": """Convert each of the measurements from kilometers to miles and present the results in a table containing both the original and converted measurements."""
})
# Append measurements to the message
[messages.append({"role": "user", "content": i}) for i in measurements]

response = get_response(messages)
print(response)