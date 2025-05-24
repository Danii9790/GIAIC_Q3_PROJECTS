import os
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel
from typing import Optional,Dict 
from agents.tool import function_tool

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API setting
provider=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# Configure the language model
model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=provider)
import requests

@function_tool("get_weather")
def get_weather(location: str, unit: str = "C") -> str:
    """
    Fetch the weather for a given location using OpenWeatherMap API.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "Weather API key not set."

    units = "metric" if unit == "C" else "imperial"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units={units}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"Sorry, I couldn't find the weather for '{location}'."

        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        return f"The weather in {location} is {weather_desc} with a temperature of {temp}°{unit}. Feels like {feels_like}°{unit}."

    except Exception as e:
        return f"An error occurred while fetching the weather: {str(e)}"
    

@function_tool("get_news")
def get_news(query: str) -> str:
    """
    Fetch latest news headlines related to a query using NewsAPI.
    """
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return "News API key not set."

    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=5&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or data.get("status") != "ok":
            return f"Error fetching news: {data.get('message', 'Unknown error')}"

        if not data.get("articles"):
            return "No news articles found for your query."

        news_list = [f"{idx + 1}. {article['title']}" for idx, article in enumerate(data["articles"])]
        return "\n".join(news_list)

    except Exception as e:
        return f"An error occurred while fetching the news: {str(e)}"


# Create a Agent
agent=Agent(
    name="Greeting ,Weather, News Agent",
  instructions = """
You are a greeting, weather, and news assistant.

1. If the user says a greeting like "Hi", "Hello", or "Salam", respond with:
   "Hello from Muhammad Daniyal!"

2. If the user says goodbye, like "Bye" or "Allah Hafiz", respond with:
   "ALLAH HAFIZ"

3. If the user asks about the weather in a specific city, use the `get_weather` tool to fetch the live weather information.

4. If the user asks for news, mentions the word 'news', 'latest update', or asks about current events, use the `get_news` tool to fetch the latest news headlines.

5. If the user says anything else that is not a greeting, farewell, weather query, or news-related message, reply with:
   "I am a greeting agent. I don't communicate with you other than greeting, weather, or news-related messages."
"""

,
    model=model,
    tools=[get_weather,get_news]
    )


# Decorator to handle OAuth callback from Github
@cl.oauth_callback
def oauth_callback(
    provider_id:str,
    raw_user_data: Dict[str,str],
    token: str,
    default_user : cl.User
) -> Optional[cl.User]:
    
    print(f"Provider : {provider_id}")
    print(f"User data : {raw_user_data}")

    return default_user

# Handle new chat session starts
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])
    await   cl.Message(
        content="Hello! How can i help you today?"
    ).send()

# Handle incoming chat_session
@cl.on_message
async def handle_message(message : cl.Message):
    history=cl.user_session.get("history")
    history.append(
        {"role":"user","content":message.content}
    )  #Add user message to histroy
# 1.cahinlit function is work Asynchronus
# 1.Agent function is now work synchronus
    result=await cl.make_async(Runner.run_sync)(agent,input=history)

    response_text=result.final_output

    await cl.Message(content=response_text).send()

    history.append({"role":"assistant","content":response_text})
    cl.user_session.set("history",history)
