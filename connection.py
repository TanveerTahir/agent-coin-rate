import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel, function_tool


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client
)

config = RunConfig(
    model = model,
    model_provider=external_client,
    tracing_disabled = True
)



ex_rate_bitcoin = Agent(
    name = "BitCoin-Agent",
    instructions= "You are a Bit Coin expert. provide detailed and accurate uptodate rate of bitcoin in USD to PKR",

)

result = Runner.run_sync(
    ex_rate_bitcoin,
    input = "what is the current rate of BTC?",
    run_config=config,
    
)

print(result.final_output)