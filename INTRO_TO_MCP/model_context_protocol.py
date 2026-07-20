import requests, asyncio, sys
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server instance
mcp = FastMCP("Currency Converter")

@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Convert an amount from one currency to another using current exchange rates.

    Args:
        amount: The amount to convert
        from_currency: Source currency code (e.g., 'USD', 'EUR', 'GBP')
        to_currency: Target currency code (e.g., 'USD', 'EUR', 'GBP')

    Returns:
        A string with the conversion result and exchange rate
    """
    # API endpoint for Frankfurter
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"

    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()

        # Parse the response
        data = response.json()

        # Get the exchange rate
        rate = data['rates'].get(to_currency)

        if rate is None:
            return f"Could not find exchange rate for {from_currency} to {to_currency}"

        # Calculate the converted amount
        converted_amount = amount * rate

        return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency} (Rate: {rate})"

    except requests.exceptions.RequestException as e:
        return f"Error converting currency: {str(e)}"

print("Testing Currency Converter:")
result = convert_currency(amount=1, from_currency="GBP", to_currency="NGN")
print(result)


"BUILDING A CURRENCY CONVERTER MCP SERVER"
"1"
# Create an MCP server instance
mcp = FastMCP("Currency Converter")
"2"
# Create an MCP server instance
mcp = FastMCP("Currency Converter")

# Define the MCP tool
@mcp.tool()
def convert_currency(amount, from_currency, to_currency):
    pass
"3"
# Create an MCP server instance
mcp = FastMCP("Currency Converter")

# Define the MCP tool
@mcp.tool()
def convert_currency(amount, from_currency, to_currency):
    # API endpoint for Frankfurter
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
"4"
# Create an MCP server instance
mcp = FastMCP("Currency Converter")

# Define the MCP tool
@mcp.tool()
def convert_currency(amount, from_currency, to_currency):
    # API endpoint for Frankfurter
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"

    # 1. Make the API request
    response = requests.get(url)

    # 2. Extract the currency exchange rate from the response
    data = response.json()
    rate = data['rates'].get(to_currency)

    if rate is None:
        return f"Could not find exchange rate for {from_currency} to {to_currency}"

    # 3. Calculate the converted amount
    converted_amount = amount * rate 
    return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency} (Rate: {rate})"
      
print(convert_currency(amount=100, from_currency="EUR", to_currency="USD"))


"ADDING DOCSTRINGS & TYPE HINTS"
# Adding typing to the function arguments and return object
@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    # Complete the docstring with the function arguments
    """
    Convert an amount from one currency to another using current exchange rates.

    Args:
        amount: The amount to convert-
        from_currency: Source currency code (e.g., 'USD', 'EUR', 'GBP')
        to_currency: Target currency code (e.g., 'USD', 'EUR', 'GBP')

    Returns:
        A string with the conversion result and exchange rate
    """

    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"

    response = requests.get(url)
    data = response.json()
    rate = data['rates'].get(to_currency)

    if rate is None:
        return f"Could not find exchange rate for {from_currency} to {to_currency}"

    converted_amount = amount * rate
    return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency} (Rate: {rate})"

print(convert_currency(amount=100, from_currency="EUR", to_currency="USD"))


"DYNAMIC TOOL DISCOVERABILITY"
"1"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def get_tools_from_mcp():
    # Define the server parameters
    params = StdioServerParameters(
        command=sys.executable,
        args=["currency_server.py"],
    )
"2"
async def get_tools_from_mcp():
    # Define the server parameters
    params = StdioServerParameters(
        command=sys.executable,
        args=["currency_server.py"],
    )

    # Connect to the MCP server and open a session
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            # Initialize the session
            await session.initialize()
"3"
async def get_tools_from_mcp():
    # Define the server parameters
    params = StdioServerParameters(
        command=sys.executable,
        args=["currency_server.py"],
    )

    # Connect to the MCP server and open a session
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            # Initialize the session
            await session.initialize()

            # Ask the server what tools it provides
            response = await session.list_tools()
"4"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def get_tools_from_mcp():
    # Define the server parameters
    params = StdioServerParameters(
        command=sys.executable,
        args=["currency_server.py"],
    )

    # Connect to the MCP server and open a session
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            # Initialize the session
            await session.initialize()

            # Ask the server what tools it provides
            response = await session.list_tools()

            # Display the available tools
            print("Connected to MCP server!")
            print("Available tools:")
            for tool in response.tools:
                print(f" - {tool.name}: {tool.description}")
                
            return response.tools

asyncio.run(get_tools_from_mcp())


"CALLING SERVER TOOLS"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def call_mcp_tool(tool_name: str, arguments: dict) -> str:
    params = StdioServerParameters(
        command=sys.executable,
        args=["currency_server.py"],
    )

    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            # Call the currency conversion tool
            result = await session.call_tool(tool_name, arguments)

            # Extract and print the text content of the server response
            text_content = result.content[0].text

            print(f"Conversion Result: {text_content}")
            return text_content

# Run the "convert_currency" tool
asyncio.run(
    call_mcp_tool("convert_currency",
                  {"amount": 250.0, "from_currency": "USD", "to_currency": "EUR"})
)


"DEFINING MCP SERVER RESOURCES"
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Currency Converter")

# Define a resource for the currencies file
@mcp.resource("file://currencies.txt")
def get_currencies() -> str:
    """
    Get the list of currency names published by the European Central Bank for currency conversion.

    Returns:
        Contents of the currencies.txt file with currency names
    """
    # Open currencies.txt and read the data
    try:
        with open('currencies.txt', 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "currencies.txt file not found"

# Test the resource function
print(get_currencies())


"LISTING RESOURCES FROM THE CLIENT"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def list_resources():
    """List all available resources from the MCP server."""
    params = StdioServerParameters(command=sys.executable, args=["currency_server.py"])

    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Get the list of resources
            response = await session.list_resources()

            print("Available resources:")
            # Print each resource's URI, name, and description
            for resource in response.resources:
                print(f" - {resource.uri}")
                print(f"   Name: {resource.name}")
                print(f"   Description: {resource.description}")

            return response.resources

asyncio.run(list_resources())


"READING RESOURCES FROM THE CLIENT"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Define an async function for reading MCP resources
async def read_resource(resource_uri: str):
    """Read a specific resource by URI."""
    params = StdioServerParameters(
        command=sys.executable,
        args=["currency_server.py"],
    )

    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            print(f"Reading resource: {resource_uri}")
            # Read the resource from the session context
            resource_content = await session.read_resource(resource_uri)

            # Print the contents of each resource
            for content in resource_content.contents:
                print(f"\nContent ({content.mimeType}):")
                print(content.text)

            return resource_content

asyncio.run(read_resource("file://currencies.txt"))


"DEFINING AN MCP SERVER PROMPT"
# Define a prompt for currency conversion
@mcp.prompt(title="Currency Conversion")
def currency_converter(currency_request: str) -> str:
    return f"""You are a currency conversion assistant.

Your task is to:
1. Extract the amount and source currency from the user's natural language input.
2. Identify the target currency.
3. Use the conversion tool to convert the amount.

Rules:
- If the amount or currencies are ambiguous or missing, ask the user for clarification.
- Use only supported currency codes (e.g., USD, EUR, GBP).

User's currency conversion request: {currency_request}"""

# Test the prompt function
print(currency_converter("100 USD to EUR"))


"LISTING PROMPTS FROM THE CLIENT"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def list_prompts():
    """List all available prompts from the MCP server."""
    params = StdioServerParameters(command=sys.executable, args=["currency_server.py"])

    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            # List available prompts
            prompts = await session.list_prompts()
            print(f"Available prompts: {[p.name for p in prompts.prompts]}")

            return prompts.prompts

asyncio.run(list_prompts())


"RETRIEVING A PROMPT FROM A CLIENT"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def read_prompt(user_input: str = "How much is 50 GBP in euros?", prompt_name: str = "convert_currency_prompt") -> str:
    """Retrieve a prompt from the MCP server with user input."""
    params = StdioServerParameters(command=sys.executable, args=["currency_server.py"])

    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            # Retrieve the prompt with the user's input
            prompt = await session.get_prompt(prompt_name, arguments={"currency_request": user_input})

            # Print the full prompt text (template + user request)
            text = prompt.messages[0].content.text
            print(text)
            return text

asyncio.run(read_prompt(user_input="How much is 50 GBP in euros?"))


"LLM TOOL USE IN MCP SERVERS"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from anthropic import AsyncAnthropic

async def call_anthropic_llm(user_query: str):
    """Call Claude with MCP tools."""
    
    print(f"\nUser: {user_query}\n")

    mcp_tools = await get_tools_from_mcp()
    
    anthropic_tools = []
    for tool in mcp_tools:
        anthropic_tool = {
            "name": tool.name,
            "description": tool.description or "",
            "input_schema": tool.inputSchema,
        }
        anthropic_tools.append(anthropic_tool)
    
    # Send the user query and formatted tools to the LLM
    client = AsyncAnthropic(api_key="<ANTHROPIC_API_TOKEN>")

    response = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_query}],
        tools=anthropic_tools,
    )

    if response.stop_reason == "tool_use":
        tool_use = next(block for block in response.content if block.type == "tool_use")
        name = tool_use.name
        args = tool_use.input

        print(f"Model decided to call: {name}")
        print(f"Arguments: {args}\n")

        # Call the MCP tool
        result = await call_mcp_tool(name, args)

        # Send the result back to Claude for the final response
        followup = await client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": user_query},
                {"role": "assistant", "content": response.content},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": result,
                        }
                    ],
                },
            ],
            tools=anthropic_tools,
        )

        final_text = next((block.text for block in followup.content if block.type == "text"), None)
        if final_text:
            print(f"\nAssistant: {final_text}")
            return str(final_text)
        else:
            print("No follow-up message from model.")

    else:
        text = next((block.text for block in response.content if block.type == "text"), "")
        print(f"\nAssistant: {text}")
        return str(text)


if __name__ == "__main__":
    asyncio.run(call_anthropic_llm("How much is 250 US dollars in euros?"))


"FETCH RESOURCE AND PROMPT FROM MCP"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def get_context_from_mcp(user_query: str) -> tuple[str, str]:
    """Fetch resource content and prompt text from the MCP server."""
    params = StdioServerParameters(command=sys.executable, args=["currency_server.py"])

    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            # Read the resource (supported currencies)
            resource_result = await session.read_resource("file://currencies.txt")
            resource_text = resource_result.contents[0].text

            # Get the prompt with the user's query
            prompt_result = await session.get_prompt("convert_currency_prompt",
                arguments={"currency_request": user_query})
            prompt_text = prompt_result.messages[0].content.text

            return resource_text, prompt_text

print(asyncio.run(get_context_from_mcp("How much is 50 GBP in euros?")))


"BUILDING THE MESSAGE & CALLING THE LLM"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def get_context_from_mcp(user_query: str) -> tuple[str, str]:
    params = StdioServerParameters(command=sys.executable, args=["currency_server.py"])
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            resource_result = await session.read_resource("file://currencies.txt")
            resource_text = resource_result.contents[0].text
            prompt_result = await session.get_prompt("convert_currency_prompt",
                arguments={"currency_request": user_query})
            prompt_text = prompt_result.messages[0].content.text
            return resource_text, prompt_text

async def get_tools_from_mcp():
    params = StdioServerParameters(command=sys.executable, args=["currency_server.py"])
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            response = await session.list_tools()
            return response.tools

async def call_mcp_tool(tool_name: str, arguments: dict) -> str:
    params = StdioServerParameters(command=sys.executable, args=["currency_server.py"])
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            return str(result.content[0].text)

async def call_llm_with_context(user_query: str):
    """Call the LLM with resource and prompt context from MCP."""
    resource_text, prompt_text = await get_context_from_mcp(user_query)

    # Combine the resource and prompt text
    full_prompt = prompt_text + "\n\nSupported currencies:\n" + resource_text

    client = AsyncAnthropic(api_key="<ANTHROPIC_API_TOKEN>")
    mcp_tools = await get_tools_from_mcp()
    anthropic_tools = [{"name": t.name, "description": t.description or "", "input_schema": t.inputSchema} for t in mcp_tools]

    # Send full_prompt (as a user message) and the tools list to the model
    response = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": full_prompt}],
        tools=anthropic_tools,
    )

    # Return the text response
    if response.stop_reason == "end_turn":
        text = next((block.text for block in response.content if block.type == "text"), "")
        print(f"\nAssistant: {text}")
        return str(text)

    # Call the tool requested in the LLM's tool use
    if response.stop_reason == "tool_use":
        tool_use = next(block for block in response.content if block.type == "tool_use")
        result = await call_mcp_tool(tool_use.name, tool_use.input)
        followup = await client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": full_prompt},
                {"role": "assistant", "content": response.content},
                {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tool_use.id, "content": result}]},
            ],
            tools=anthropic_tools,
        )
        final_text = next((block.text for block in followup.content if block.type == "text"), None)
        if final_text:
            print(f"\nAssistant: {final_text}")
            return str(final_text)

print("=== Ambiguous request (prompt asks for clarification) ===")
asyncio.run(call_llm_with_context("Convert some euros to dollars"))
print("\n=== Unambiguous request (model calls tool) ===")
asyncio.run(call_llm_with_context("How much is 50 GBP in euros?"))


"CREATING DATABASE CONNECTIONS"
import sqlite3

# Connect to currencies.db
conn = sqlite3.connect("currencies.db")
conn.row_factory = sqlite3.Row

# Execute the query
cursor = conn.execute("SELECT code, name FROM currencies WHERE code = ? LIMIT 1", ("USD",))
row = cursor.fetchone()
print(dict(row))

# Close the connection
conn.close()


"DATABASES AS RESOURCES"
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Currency Converter")

# Connect to the database on startup
conn = sqlite3.connect("currencies.db")
conn.row_factory = sqlite3.Row

# Create an MCP resource
@mcp.resource("db://currencies")
def get_currencies() -> str:
    """
    Get the list of currency names published by the European Central Bank for currency conversion.

    Returns:
        One line per currency (code - name), from the database.
    """
    try:
        # Query the database
        cursor = conn.execute("SELECT code, name FROM currencies")
        rows = cursor.fetchall()
        return "\n".join(f"{row['code']} - {row['name']}" for row in rows)
    except sqlite3.Error as e: return f"Error: {e}"

result = get_currencies()
print(result[:200] + "..." if len(result) > 200 else result)


"PARAMETERIZED DATABASE LOOKUP TOOLS"
# Add lookup_currencies(prefix): find rows where name or code contains prefix
@mcp.tool()
def lookup_currencies(prefix: str) -> str:
    """Find currencies whose code or name contains the given prefix."""
    try:
        # Use parameterized query and LIMIT 50
        cursor = conn.execute(
            "SELECT code, name FROM currencies WHERE name LIKE ? OR code LIKE ? LIMIT 50",
            (f"%{prefix}%", f"%{prefix}%")
        )
        rows = cursor.fetchall()
        return "\n".join(f"{row['code']} - {row['name']}" for row in rows)
    except sqlite3.Error as e:
        return f"Database error: {e}"

print(lookup_currencies("Euro"))


"MAKING API TOOL CALLS ROBUST"
@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Convert an amount from one currency to another using current exchange rates.

    Args:
        amount: The amount to convert
        from_currency: Source currency code (e.g., 'USD', 'EUR', 'GBP')
        to_currency: Target currency code (e.g., 'USD', 'EUR', 'GBP')

    Returns:
        A string with the conversion result and exchange rate
    """
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
    # Implement try-except to gracefully handle errors
    try:
        # Add a 10-second timeout so the request does not hang
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        rate = data["rates"].get(to_currency)
        if rate is None:
            return f"Could not find exchange rate for {from_currency} to {to_currency}"
        return f"{amount} {from_currency} = {amount * rate:.2f} {to_currency} (Rate: {rate})"
    except requests.exceptions.RequestException as e:
        return f"Error converting currency: {e}"

print(convert_currency(10, "USD", "EUR"))


"WHEN APIS REQUIRE AUTHENTICATION"
@mcp.tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Convert an amount from one currency to another using current exchange rates."""
    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
    # Read optional API key from the server's environment
    headers = {}
    api_key = os.environ.get("CURRENCY_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    try:
        # Pass headers (and timeout) to the request; key never goes in the URL
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        rate = data["rates"].get(to_currency)
        if rate is None:
            return f"Could not find exchange rate for {from_currency} to {to_currency}"
        return f"{amount} {from_currency} = {amount * rate:.2f} {to_currency} (Rate: {rate})"
    except requests.exceptions.RequestException as e:
        return f"Error converting currency: {e}"

print(convert_currency(10, "USD", "EUR"))


"SEARCH FOR A BOOK BY TITLE WITH THE OPEN LIBRARY MCP"
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

OPEN_LIBRARY_SERVER_CMD = ""
OPEN_LIBRARY_SERVER_ARGS = ""

async def main():
    params = StdioServerParameters(command=OPEN_LIBRARY_SERVER_CMD, args=OPEN_LIBRARY_SERVER_ARGS)
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call get_book_by_title for "AI" and assign the result
            result = await session.call_tool("get_book_by_title", {"title": "AI"})
            # Assign the result text and print it
            text = result.content[0].text
            print(text)

asyncio.run(main())