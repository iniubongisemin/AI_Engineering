from pydantic import BaseModel, Field

from openai import OpenAI
import requests, json

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


"BUILDING CONFIDENCE WITH LLM SOURCES"
# Create a response with web search enabled and sources included
response = client.responses.create(
    model="gpt-5.4-mini",
    tools=[{"type": "web_search"}],
    input="What is the current stock price of Netflix?",
    include=["web_search_call.action.sources"]
)

# Extract and print sources from web search calls
for item in response.output:
    if item.type == "web_search_call":
        print(item.action.sources)
        
print(response.output_text)


"DEFINING A FUNCTION FOR CONVERTING TIMEZONES"
def convert_timezone(date_time: str, from_timezone: str, to_timezone: str) -> str:
    """
    Convert a datetime from one timezone to another.
    
    Args:
        date_time: The datetime string in ISO format
        from_timezone: Source timezone
        to_timezone: Target timezone
    
    Returns:
        A string with the converted datetime and timezone information
    """
    # Set the API endpoint
    url = "https://api.opentimezone.com/convert"
    
    # Prepare the request payload
    payload = {"dateTime": date_time, "fromTimezone": from_timezone, "toTimezone": to_timezone}
    
    try:
        # Make the API request and extract converted time
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        data = response.json()
        converted_time = data.get('dateTime', 'N/A')
        
        return f"Time in {to_timezone}: {converted_time}"
    
    except requests.exceptions.RequestException as e:
        return f"Error converting timezone: {str(e)}"

# Test the function
result = convert_timezone('2025-01-20T14:30:00', 'America/New_York', 'Europe/London')
print(result)


"BUILDING THE OPENAI TOOL DEFINITION"
tools = [
    {
        # Define a function tool called convert_timezone
        "type": "function",
        "name": "convert_timezone",
        "description": "Convert a datetime from one timezone to another using the OpenTimezone API.",
        "parameters": {
            "type": "object",
            # Define the parameter names, types, and descriptions
            "properties": {
                "date_time": {
                    "type": "string",
                    "description": "The datetime string in ISO format (e.g., '2025-01-20T14:30:00')"
                },
                "from_timezone": {
                    "type": "string",
                    "description": "The source timezone (e.g., 'America/New_York', 'Asia/Tokyo')"
                },
                "to_timezone": {
                    "type": "string",
                    "description": "The target timezone (e.g., 'Europe/London', 'Australia/Sydney')"
                }
            },
            # Ensure that all three parameters are required
            "required": ["date_time", "from_timezone", "to_timezone"],
            "additionalProperties": False
        }
    }
]


"INTEGRATING FUNCTION CALLING TOOLS"
messages = [{"role": "user", "content": "What time is 2:30pm on January 20th in New York in Tokyo time?"}]
response = client.responses.create(model="gpt-5.4-mini", input=messages, tools=tools)
messages += response.output

# Process function calls and execute the timezone conversion
for item in response.output:
    if item.type == "function_call":
        if item.name == "convert_timezone":
            timezone_result = convert_timezone(**json.loads(item.arguments))
            
            # Append function output to messages
            messages.append({"type": "function_call_output", "call_id": item.call_id, "output": json.dumps({"convert_timezone": timezone_result})})

# Make second API request with function results
response = client.responses.create(model="gpt-5.4-mini", input=messages, tools=tools)
print(response.output_text)


"CONSISTENT OUTPUTS EVERYTIME"
# Define the book recommendation schema
class MovieRecommendation(BaseModel):
    title: str = Field(description="The movie title")
    genre: str = Field(description="Primary genre")
    vibe: str = Field(description="One-word vibe: cozy, thrilling, emotional, or fun")
    why: str = Field(description="One sentence explaining why this matches")

# Generate structured recommendation
response = client.responses.parse(
    model="gpt-5.4-mini",
    instructions="You are a knowledgeable movie recommender.",
    input="Recommend a movie for someone who loved Inception and wants something mind-bending",
    text_format=MovieRecommendation,
)

# Extract the parsed output and results
recommendation = response.output_parsed
print(f"Title: {recommendation.title}")
print(f"Reason: {recommendation.why}")


"NESTING PYDANTIC CLASSES"
"1"
# Define the SimilarMovie class
class SimilarMovie(BaseModel):
    title: str = Field(description="Title of a similar movie")
    similarity_reason: str = Field(description="Why this movie is similar")
"2"
# Define the DetailedMovieRecommendation class
class DetailedMovieRecommendation(BaseModel):
    title: str = Field(description="The movie title")
    genre: str = Field(description="Primary genre")
    vibe: str = Field(description="One-word vibe: cozy, thrilling, emotional, or fun")
    why: str = Field(description="One sentence explaining why this matches")
    similar_movies: list[SimilarMovie] = Field(description="Other movies with similar themes or style")
"3"
# Create a structured response for movie recommendation
response = client.responses.parse(
    model="gpt-5.4-mini",
    instructions="You are a knowledgeable movie recommender.",
    input="Recommend a movie for someone who loved Inception and wants something mind-bending",
    text_format=DetailedMovieRecommendation
)
"4"
# Extract the parsed recommendation
recommendation = response.output_parsed

print(f"Title: {recommendation.title}")
print(f"\nSimilar movies:")
for movie in recommendation.title:
    print(f"- {movie.title}: {movie.similarity_reason}")