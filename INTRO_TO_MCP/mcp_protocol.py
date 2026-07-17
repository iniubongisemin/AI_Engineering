import requests, asyncio, sys
from mcp.server.fastmcp import FastMCP

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