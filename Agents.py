import os
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_react_agent
from langchain_ollama import ChatOllama

def get_weather(city: str):
    """Get the current weather of a given city."""
    return f"The weather in {city} is sunny."

# Model
model = ChatOllama(model="llama3.1:8b")

# Agent
agent = create_react_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant that can answer questions and help with tasks.",
)
A = agent.invoke({
    "messages": [{"role": "user", "content": "What is the weather in India?"}]
})

print(A["messages"][-1].content)