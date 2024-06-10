from crewai import Agent

from src.infra.ai.llm import llm
from src.infra.ai.tools.post_scrapper import PostScrapperTool

scraper = Agent(
    role='Scraper',
    goal='Extract content from within web pages by scraping.',
    verbose=True,
    backstory='You are a scraping expert, able to extract valuable data from web pages.',
    tools=[PostScrapperTool()],
    allow_delegation=False,
    llm=llm,
)
