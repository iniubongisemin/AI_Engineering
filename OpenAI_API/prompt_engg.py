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
TEXT GOES HERE"""
response = get_response (prompt)

"USING FORMATTED F-STRINGS"
"Include defined string into another string"

text = "This is a sample text to summarize"
prompt = f"""Summarize the text delimited by triple backticks into bullet points.
{text}"""