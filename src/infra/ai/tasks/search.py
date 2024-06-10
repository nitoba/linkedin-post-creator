from crewai import Task

from src.infra.ai.agents.researcher import researcher
from src.infra.ai.tools.search import search

search_task = Task(
    description='Search for relevant topics and trends related to the topic: {topic}.',
    expected_output='List of URLs relevant to the topic.',
    tools=[search],
    agent=researcher,
)
