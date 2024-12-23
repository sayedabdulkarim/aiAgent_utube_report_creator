from crewai import Agent
from tools import tool
from dotenv import load_dotenv
# from langchain.llms import Ollama
from langchain_ollama import OllamaLLM
import os

# Load environment variables
load_dotenv()

# Initialize the local Ollama model
# llm = Ollama(
#     base_url="http://localhost:11434",  # Ollama local server URL
#     model="llama3.2:1b",  # Specify the model
#     verbose=True  # Enable verbose logging
# )


llm = OllamaLLM(
    base_url="http://localhost:11434",
    model="llama3.2:1b",
    verbose=True
)


# Create a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world."
    ),
    tools=[tool],
    llm=llm,  # Use the local Ollama model
    allow_delegation=True
)

# Create a writer agent with custom tools responsible for writing news blogs
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,  # Use the local Ollama model
    allow_delegation=False
)


# response = news_researcher.act("hello world")
# print(response)

# response = news_writer.act("qwerty")
# print(response)
