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


"CODE GENERATION WITH PROBLEM DESCRIPTION"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = "Write a Python function that receives a list of 12 floats representing monthly sales data as input and, returns the month with the highest sales value as output."

response = get_response(prompt)
print(response)


"INPUT-OUTPUT EXAMPLES FOR CODE GENERATION"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"""Infer the Python function that maps the inputs to the outputs in the provided examples delimited by triple backticks ```{examples}```"""

response = get_response(prompt)
print(response)


"MODIFYING CODE WITH MULTISTEP PROMPTS"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""Modify the function delimited by triple backticks ```{function}``` according to these specified requirements: 
1. Test if the inputs to the functions are positive, and if not, display appropriate error messages
2. If the inputs are positive, return the area and perimeter of the rectangle."""

response = get_response(prompt)
print(response)


"EXPLAINING CODE STEP BY STEP"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f"""Q: Explain, step by step the provided function delimited by triple backticks ```{function}```
A: The function does...
"""
 
response = get_response(prompt)
print(response)


"CREATING A DUAL PROMPT get_response() FUNCTION"
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

system_prompt = """You are a principal software engineer at a 'FAANG' company who has a decade of experience building and scaling distributed systems. Only respond to questions related to software engineering & computer science! If you're asked an unrelated question 'respond with: I am designed to answer only software related questions"""

user_prompt = "Explain what 'microservices' are to me like I'm an intern at your company"

# Try the function with a system and user prompts of your choice 
response = get_response(system_prompt, user_prompt)
print(response)