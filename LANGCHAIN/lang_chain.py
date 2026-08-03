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


"PDF DOCUMENT LOADERS"
# Import library
from langchain_community.document_loaders import PyPDFLoader

# Create a document loader for rag_vs_fine_tuning.pdf
loader = PyPDFLoader("rag_vs_fine_tuning.pdf")

# Load the document
data = loader.load()
print(data[0])


"CSV DOCUMENT LOADERS"
# Import library
from langchain_community.document_loaders.csv_loader import CSVLoader

# Create a document loader for fifa_countries_audience.csv
loader = CSVLoader("fifa_countries_audience.csv")

# Load the document
data = loader.load()
print(data[0])


"HTML DOCUMENT LOADERS"
from langchain_community.document_loaders import UnstructuredHTMLLoader

# Create a document loader for unstructured HTML
loader = UnstructuredHTMLLoader("white_house_executive_order_nov_2023.html")

# Load the document
data = loader.load()

# Print the first document
print(data[0])

# Print the first document's metadata
print(data[0].metadata)


"SPLITTING BY CHARACTER"
# Import the character splitter
from langchain_text_splitters import CharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=24,
    chunk_overlap=10)

# Split the string and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])


"RECURSIVELY SPLITTING BY CHARACTER"
# Import the recursive character splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = RecursiveCharacterTextSplitter(
    separators=["\n", " ", ""],
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap)

# Split the document and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])

"""
output:
  ['Words are flowing out', 'out like endless rain', 'rain into a paper cup,', 'they slither while they', 'they pass,', 'they slip away across', 'across the universe.']
  [21, 21, 22, 23, 10, 21, 20]

VARIANTS:
1.
chunk_size = 22
chunk_overlap = 8

['Words are flowing out', 'out like endless rain', 'rain into a paper', 'a paper cup,', 'they slither while', 'while they pass,', 'they slip away across', 'across the universe.']
[21, 21, 17, 12, 18, 16, 21, 20]

2.
chunk_size = 20
chunk_overlap = 6

['Words are flowing', 'out like endless', 'rain into a paper', 'paper cup,', 'they slither while', 'while they pass,', 'they slip away', 'away across the', 'the universe.']
[17, 16, 17, 10, 18, 16, 14, 15, 13]

3.
chunk_size = 18
chunk_overlap = 4

['Words are flowing', 'out like endless', 'rain into a paper', 'cup,', 'they slither', 'while they pass,', 'they slip away', 'across the', 'the universe.']
[17, 16, 17, 4, 12, 16, 14, 10, 13]

4.
chunk_size = 24
chunk_overlap = 4

['Words are flowing out', 'out like endless rain', 'into a paper cup,', 'they slither while they', 'pass,', 'they slip away across', 'the universe.']
[21, 21, 17, 23, 5, 21, 13]

5. 
chunk_size = 24
chunk_overlap = 2

['Words are flowing out', 'like endless rain into', 'a paper cup,', 'they slither while they', 'pass,', 'they slip away across', 'the universe.']
[21, 22, 12, 23, 5, 21, 13]

6.
chunk_size = 30
chunk_overlap = 2

['Words are flowing out like', 'endless rain into a paper', 'cup,', 'they slither while they pass,', 'they slip away across the', 'universe.']
[26, 25, 4, 29, 25, 9]
"""


"SPLITTING HTML"
# Load the HTML document into memory
loader = UnstructuredHTMLLoader("white_house_executive_order_nov_2023.html")
data = loader.load()

# Define variables
chunk_size = 300
chunk_overlap = 100

# Split the HTML
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=".")

docs = splitter.split_documents(data)
print(docs)


"PREPARING THE DOCUMENTS & VECTOR DATABASE"
import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

# Split the document using RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50)
docs = splitter.split_documents(data) 

# Embed the documents in a persistent Chroma vector database
embedding_function = OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small')
vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding_function,
    persist_directory=os.getcwd()
)

# Configure the vector store as a retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


"BUILDING A RETRIEVAL PROMPT TEMPLATE"
# Add placeholders to the message string
message = """
Answer the following question using the context provided:

Context:
{context}

Question:
{question}

Answer:
"""

# Create a chat prompt template from the message string
prompt_template = ChatPromptTemplate.from_messages([("human", message)])


"CREATING A RAG CHAIN"
from langchain_core.runnables import RunnablePassthrough
vectorstore = Chroma.from_documents(
    docs,
    embedding=OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small'),
    persist_directory=os.getcwd()
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Create a chain to link retriever, prompt_template, and llm
rag_chain = ({"context": retriever, "question": RunnablePassthrough()}
            | prompt_template
            | llm)

# Invoke the chain
response = rag_chain.invoke("Which popular LLMs were considered in the paper?")
print(response.content)