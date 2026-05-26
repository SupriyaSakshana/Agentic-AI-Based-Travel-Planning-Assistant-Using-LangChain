import os
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Gemini Model
from langchain_google_genai import ChatGoogleGenerativeAI

# LangChain Agent
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# Import Custom Tool Functions
from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import recommend_places
from tools.weather_tool import get_weather
from tools.budget_tool import calculate_budget


# -----------------------------------
# CREATE TOOLS
# -----------------------------------

flight_tool = Tool(
    name="Flight Search Tool",
    func=search_flights,
    description="""
    Search available flights between source and destination cities.
    Can suggest cheapest or fastest flights.
    """
)

hotel_tool = Tool(
    name="Hotel Recommendation Tool",
    func=recommend_hotels,
    description="""
    Recommend hotels based on city, budget, rating, and hotel type.
    """
)

places_tool = Tool(
    name="Places Discovery Tool",
    func=recommend_places,
    description="""
    Recommend tourist attractions based on destination
    and user interests like beaches, nightlife,
    shopping, adventure, etc.
    """
)

weather_tool = Tool(
    name="Weather Lookup Tool",
    func=get_weather,
    description="""
    Fetch live weather forecast for the destination city.
    """
)

budget_tool = Tool(
    name="Budget Estimation Tool",
    func=calculate_budget,
    description="""
    Calculate estimated total travel cost including
    flights, hotels, food, and local transport.
    """
)


# -----------------------------------
# TOOL LIST
# -----------------------------------

tools = [
    flight_tool,
    hotel_tool,
    places_tool,
    weather_tool,
    budget_tool
]


# -----------------------------------
# GEMINI LLM
# -----------------------------------

# Ideally use gemini-2.5-flash
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


# -----------------------------------
# CREATE AGENT
# -----------------------------------

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)


print("✅ AI Travel Agent Ready!")