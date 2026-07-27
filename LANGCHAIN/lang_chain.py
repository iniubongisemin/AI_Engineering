"OPENAI MODELS IN LANGCHAIN!"
from langchain_openai import ChatOpenAI

# Define the LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>")

# Predict the words following the text in question
prompt = 'Three reasons for using LangChain for LLM application development.'
response = llm.invoke(prompt)

print(response.content)


"HUGGINGFACE MODELS IN LANGCHAIN!"
# Import the HuggingFacePipeline class for defining Hugging Face pipelines
from langchain_huggingface import HuggingFacePipeline

# Define the LLM from the Hugging Face model ID
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20}
)

prompt = "Hugging Face is"

# Invoke the model
response = llm.invoke(prompt)
print(response)


"PROMPT TEMPLATES & CHAINING"
from langchain_core.prompts import PromptTemplate
# Create a prompt template from the template string
template = "You are an artificial intelligence assistant, answer the question. {question}"
prompt = PromptTemplate.from_template(
    template=template
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')	

# Create a chain to integrate the prompt template and LLM
llm_chain = prompt | llm

# Invoke the chain on the question
question = "How does LangChain make LLM application development easier?"
print(llm_chain.invoke({"question": question}))


"CHAT PROMPT TEMPLATES"
from langchain_core.prompts import ChatPromptTemplate
llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

# Create a chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a geography expert that returns the colors present in a country's flag."),
        ("human", "France"),
        ("ai", "blue, white, red"),
        ("human", "{country}")
    ]
)

# Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm

country = "Japan"
response = llm_chain.invoke({"country": country})
print(response.content)


"CREATING THE FEW SHOT EXAMPLES SET"
# Create the examples list of dicts
examples = [
  {
    "question": "How many DataCamp courses has Jack completed?",
    "answer": "36"
  },
  {
    "question": "How much XP does Jack have on DataCamp?",
    "answer": "284,320XP"
  },
  {
    "question": "What technology does Jack learn about most on DataCamp?",
    "answer": "Python"
  }
]


"BUILDING THE FEW-SHOT PROMPT TEMPLATE"
from langchain_core.prompts import FewShotPromptTemplate
# Complete the prompt for formatting answers
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

# Create the few-shot prompt
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

prompt = prompt_template.invoke({"input": "What is Jack's favorite technology on DataCamp?"})
print(prompt.text)


"IMPLEMENTING FEW-SHOT PROMPTING"
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

# Create an OpenAI chat LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

# Create and invoke the chain
llm_chain = prompt_template | llm
print(llm_chain.invoke({"input": "What is Jack's favorite technology on DataCamp?"}))


"BUILDING PROMPTS FOR SEQUENTIAL CHAINS"
# Create a prompt template that takes an input activity
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

# Create a prompt template that places a time constraint on the output
time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}."
)

# Invoke the learning_prompt with an activity
print(learning_prompt.invoke({"activity": "Learn Pandas Library"}))


"SEQUENTIAL CHAINS WITH LCEL"
from langchain_core.output_parsers import StrOutputParser
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a concise plan to help me hit this goal: {learning_plan}."
)

# Complete the sequential chain with LCEL
seq_chain = ({"learning_plan": learning_prompt | llm | StrOutputParser()}
    | time_prompt
    | llm
    | StrOutputParser())

# Call the chain
print(seq_chain.invoke({"activity": "Learn how to swim"}))


"ReAct AGENTS"
from langchain_community.agent_toolkits.load_tools import load_tools
from langgraph.prebuilt import create_react_agent

# Define the tools
tools = load_tools(["wikipedia"])

# Define the agent
agent = create_react_agent(llm, tools)

# Invoke the agent
response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})
print(response['messages'][-1].content)


"DEFINING A FUNCTION FOR TOOL USE"
customers = {"name": "Peak Performance Co."} # DUMMY variable
# Define a function to retrieve customer info by-name
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    # Filter customers for the customer's name
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Call the function on Peak Performance Co.
print(retrieve_customer_info("Peak Performance Co."))


"CREATING CUSTOM TOOLS"
from langchain_core.tools import tool
# Convert the retrieve_customer_info function into a tool
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Print the tool's arguments
print(retrieve_customer_info.args)


"INTEGRATING CUSTOM TOOLS WITH AGENTS"
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()

# Create a ReAct agent
agent = create_react_agent(llm, [retrieve_customer_info])

# Invoke the agent on the input
messages = agent.invoke({"messages": [("human", "Create a summary of our customer: Peak Performance Co.")]})
print(messages['messages'][-1].content)