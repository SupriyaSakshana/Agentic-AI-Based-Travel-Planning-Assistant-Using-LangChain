# Agentic-AI-Based-Travel-Planning-Assistant-Using-LangChain
Planning a trip requires choosing flights, hotels, and attractions while considering time, budget, weather, distance, and personal preferences.

Agentic AI-Based Travel Planning Assistant Using LangChain — is basically an intelligent AI travel agent that can autonomously plan trips by combining:

AI reasoning (Gemini LLM)
Tool calling (LangChain Agents)
Real-world travel datasets
APIs
User preferences
Dynamic itinerary generation

<img width="720" height="480" alt="image" src="https://github.com/user-attachments/assets/b50ec3d3-82b9-4b29-bd60-1622a8367b7b" />

What Makes It “Agentic AI”

Your project is NOT just chatbot-based AI.

It is Agentic AI because:

The AI:

reasons
decides
selects tools
uses external data
combines outputs
generates final response

without hardcoded flow.

Example:

User asks for Goa trip
        ↓
LLM understands task
        ↓
Agent decides:
"I need flights first"
        ↓
Calls Flight Tool
        ↓
Then calls Hotel Tool
        ↓
Then Places Tool
        ↓
Then Budget Tool
        ↓
Combines everything
        ↓
Creates final itinerary

This autonomous decision-making is the core of Agentic AI.

                ┌────────────────────┐
                │   Streamlit UI     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │  LangChain Agent   │
                └─────────┬──────────┘
                          │
              ┌───────────┼───────────┐
              │           │           │
              ▼           ▼           ▼
      Flight Tool   Hotel Tool   Places Tool
              │           │           │
              ▼           ▼           ▼
        flights.json  hotels.json places.json

              ▼
       Weather API Tool
              ▼
        Open-Meteo API

              ▼
       Budget Estimator

              ▼
      Gemini LLM Response

              ▼
     Final Travel Itinerary

     
Technologies Used


Frontend
Streamlit

Used for:

user interface
trip forms
itinerary display
download feature
Backend
Python

Handles:

tool logic
APIs
JSON datasets
AI integration
AI / LLM
Gemini 1.5 Flash

Used for:

reasoning
itinerary generation
intelligent response synthesis



Main Goal

The goal of your project is:

To develop an autonomous AI travel assistant capable of understanding user preferences and generating personalized travel plans using LLMs, LangChain agents, APIs, and structured datasets.
