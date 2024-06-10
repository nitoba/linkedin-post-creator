from crewai import Agent

from src.infra.ai.llm import llm
from src.infra.ai.tools.search import search

researcher = Agent(
    role='Researcher',
    goal='Search for relevant topics related to a given topic on the web',
    verbose=True,
    backstory='You are a dedicated researcher, always looking for the latest trends and topics of interest.',
    tools=[search],
    allow_delegation=False,
    llm=llm,
)
