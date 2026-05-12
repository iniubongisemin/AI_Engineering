from openai import OpenAI

"Using get_response function to call OpenAI API"
def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

"PROMPT ENGINEERING FOR BUSINESS APPLICATIONS"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the report
prompt = f"""Summarize the report (formatted using f-string) in maximum five sentences, while focusing on aspects related to AI and data privacy. {report}"""

response = get_response(prompt)

print("Summarized report: \n", response)