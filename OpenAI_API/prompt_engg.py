from openai import OpenAI

client = OpenAI(api_key="OPENAI_API_KEY")

"Using get_response function to call OpenAI API"
def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("Write a poem about ChatGPT.")
print(response)


"UTILIZING THE GET RESPONSE FUNCTION"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "Generate a poem about ChatGPT while ensuring that it is written in basic English that a child can understand."

# Get the response
response = get_response(prompt)

print(response)

"KEY PRINCIPLES OF PROMPT ENGINEERING"
"""
Crafting a well-structured prompt with delimiters
• Start prompt with instructions
• Use delimiters (parentheses, brackets, backticks, etc.) to specify input parts
• Mention which delimiters are used
"""

prompt = """Summarize the text delimited by triple backticks into bullet points.
```TEXT GOES HERE```"""
response = get_response (prompt)

"USING FORMATTED F-STRINGS"
"Include defined string into another string"

text = "This is a sample text to summarize"
prompt = f"""Summarize the text delimited by triple backticks into bullet points.
```{text}```"""


"USING DELIMITED PROMPTS WITH F-STRINGS"
story = ""
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that completes the story
prompt = f"Complete story delimited by triple backticks ```{story}```"

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)


"BUILDING SPECIFIC AND PRECISE PROMPTS"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to complete the story
prompt = f"Complete the story delimited with triple backticks with only two paragraphs in the style of Shakespeare {story}"

# Get the generated response
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)


"CUSTOM OUTPUT FORMAT"
text = """Once upon a time in a quaint little village, there lived a curious young boy named
David. David was [...]"""

instructions = """You will be provided with a text delimited by triple backticks. Generate a
suitable title for it."""

output_format = """Use the following format for the output:
- Text: <text we want to title>
- Title: <the generated title>"""

prompt = instructions + output_format + f"```{text}```"
print(get_response(prompt))

"""
RESPONSE: 
- Text: Once upon a time in a quaint little village, there lived a curious young boy [...]
- Title: The Extraordinary Adventure of David and the Mysterious Book
"""


"CONDITIONAL PROMPTS"
prompt = f"""You will be provided with a text delimited by triple backticks.
If the text is written in English, suggest a suitable title for it.
Otherwise, write 'I only understand English'.```{text}```"""

print(get_response(prompt))

">>> INCORPORATING MULTIPLE CONDITIONS"

text = "In the heart of the forest, sunlight filters through the lush green canopy, creating a tranquil atmosphere [...]"
prompt = f"""You will be provided with a text delimited by triple backticks.
If the text is written in English, check if it contains the keyword 'technology'.
If it does, suggest a suitable title for it, otherwise, write 'Keyword not found'.```{text}```"""

print(get_response(prompt))


"GENERATING A TABLE"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that generates the table
prompt = f"Generate a table of 10 books, with columns for Title, Author, and Year, that you should read given that you are a science fiction lover."

# Get the response
response = get_response(prompt)
print(response)

"CUSTOMIZING OUTPUT FORMAT"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "Determine the language and generate a suitable title for the pre-loaded text excerpt that will be provided using triple backticks (```) delimiters."

# Create the output format
output_format = "Include the text, language, and title, each on a separate line, using 'Text:', 'Language:', and 'Title:' as prefixes for each line."

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

"USING CONDITIONAL PROMPTS"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "Infer the language and the number of sentences of the given delimited text; then if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title."

# Create the output format
output_format = "Include the text, language, number of sentences, and title, each on a separate line,and ensure to use 'Text:', 'Language:', and 'Title:' as prefixes for each line."

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)


"ZERO-SHOT PROMPTING"
prompt = "What is prompt engineering?"
print(get_response(prompt))


"ONE-SHOT PROMPTING"
prompt = """
Q: Sum the numbers 3, 5, and 6. A: 3+5+6=14
Q: Sum the numbers 2, 4, and 7. A:
"""
print(get_response(prompt))


"FEW-SHOT PROMPTING"
prompt = """
Text: Today the weather is fantastic -> Classification: positive
Text: The furniture is small -> Classification: neutral
Text: I don't like your attitude -> Classification: negative
Text: That shot selection was awful -> Classification:
"""
print(get_response(prompt))


"SENTIMENT ANALYSIS WITH FEW-SHOT PROMPTING"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model = "gpt-4o-mini",
  # Provide the examples as previous conversations
  messages = [{"role": "user", "content": "The product quality exceeded my expectations"},
              {"role": "assistant", "content": "1"},
              {"role": "user", "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant", "content": "-1"},
              # Provide the text for the model to classify
              {"role": "user", "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)


"MULTI-STEP PROMPTING"
"e.g of Single-Step Prompt"
prompt = "Compose a travel blog"
print(get_response(prompt))

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a single-step prompt to get help planning the vacation
prompt = "Plan the perfect beach vacation"

response = get_response(prompt)
print(response)

"e.g of Multi-step Prompt"
prompt = """Compose a travel blog as follows:
Step 1: Introduce the destination.
Step 2: Share personal adventures during the trip.
Step 3: Summarize the journey.
"""
print(get_response(prompt))


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt detailing steps to plan the trip
prompt = """Make a plan for a beach vacation, which should include: four potential locations, each with some accommodation options, some activities, and an evaluation of the pros and cons."""

response = get_response(prompt)
print(response)