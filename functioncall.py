import os
from connection import config
from agents import Agent, Runner, function_tool



@function_tool
def get_bitcoin_rate() -> str:
    """
    Fetch the current Bitcoin rate in USD and PKR.
    """
    # Here you would implement the logic to fetch the Bitcoin rate.
    # For demonstration purposes, we will return a mock value.
    return "1 {BTC} = 60,000 USD, 1 {BTC} = 17,000,000 PKR"



ex_rate_bitcoin = Agent(
    name = "BitCoin-Agent",
    instructions= "You are a Bit Coin expert. provide detailed and accurate uptodate rate of bitcoin in USD to PKR",
    tools = [get_bitcoin_rate],

)

result = Runner.run_sync(
    ex_rate_bitcoin,
    input = "what is the current rate of BTC?",
    run_config=config,
    
)

print(result.final_output)