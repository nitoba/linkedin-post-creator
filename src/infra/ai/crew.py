from crewai import Crew, Process

from src.infra.ai.agents.designer import designer
from src.infra.ai.agents.editor import editor
from src.infra.ai.agents.publisher import publisher
from src.infra.ai.agents.researcher import researcher
from src.infra.ai.tasks.content_creation import content_creation_task
from src.infra.ai.tasks.content_scrapper import scraping_content_task
from src.infra.ai.tasks.final_response import final_response_task
from src.infra.ai.tasks.prompt_creation import prompt_creation_task
from src.infra.ai.tasks.search import search_task

crew = Crew(
    agents=[
        researcher,
        editor,
        designer,
        publisher,
    ],
    tasks=[
        search_task,
        scraping_content_task,
        content_creation_task,
        prompt_creation_task,
        final_response_task,
    ],
    process=Process.sequential,
    verbose=2,
)
