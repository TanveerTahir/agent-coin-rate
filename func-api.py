from agents import Agent, Runner, function_tool
import requests
from connection import config


@function_tool
def get_coin_price(coin): # url 1 is for all coins, url 2 is for specific coin
#   url = "https://api.binance.com/api/v3/ticker/"  # Example URL for fetching the price of a specific cryptocurrency
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT" 

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns the JSON response containing the current price of all coins
    else:
        return f"error:, Failed to fetch Cryptocurrency rate, status code: ", {response.status_code}
    
coin_agent = Agent(
    name = "CoinAgent",
    instructions = "help to find current market price of Cryptocurrency.",
    tools = [ get_coin_price ]
)

result = Runner.run_sync(
    coin_agent,
    input = "what is the current price of BTC in USD ?",
    run_config = config
)

print(result.final_output)