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
report = ""

# Craft a prompt to summarize the report
prompt = f"""Summarize the report (formatted using f-string) in maximum five sentences, while focusing on aspects related to AI and data privacy. {report}"""

response = get_response(prompt)

print("Summarized report: \n", response)


"PRODUCT FEATURES SUMMARIZATION"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")
product_description = ""

# Craft a prompt to summarize the product description
prompt = """Summarize the {product_description} (formatted using f-string) in no more than five bullet points"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)


"PRODUCT FEATURES EXPANSION"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f"""Expand the {product_description} (formatted using f-string) pre-loaded string, and write a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)


"TRANSLATION FOR MULTILINGUAL COMMUNICATION"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

marketing_message = ""

# Craft a prompt that translates
prompt = f"""Translate the marketing message (formatted using f-string) from English to French, Spanish, and Japanese. {marketing_message}"""
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)


"TONE ADJUSTMENT FOR EMAIL MARKETING"
sample_email = ""

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f"""Transform the sample email (formatted using f-string) by changing its tone to be professional, positive, and user-centric.{sample_email}"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)


"WRITING IMPROVEMENT (using Multi-step Prompting)"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

text = ""
# Craft a prompt to transform the text
prompt = f"""Improve the text delimited by triple backticks as follows: 
Step 1: Proofread the message without changing its structure
Step 2: Adjust its tone to be formal and friendly. ```{text}```"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)


"CUSTOMER SUPPORT TICKET ROUTING"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

ticket = ""
# Craft a prompt to classify the ticket
prompt = f"""Classify the ticket delimited by triple backticks as technical issue, billing inquiry, or product feedback, without providing anything else in the response. ```{ticket}```
"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)


"TEXT ANALYSIS"
