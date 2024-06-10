from crewai import Task

from src.infra.ai.agents.scrapper import scraper
from src.infra.ai.tools.post_scrapper import PostScrapperTool

scraping_content_task = Task(
    description='scrape content from URLs promoted by DuckDuckGoSearch for the theme: {topic}.',
    expected_output='Content scraped from URLs.',
    tools=[PostScrapperTool()],
    agent=scraper,
)
