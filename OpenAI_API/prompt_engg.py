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
