from textwrap import dedent

from crewai import Task

from src.infra.ai.agents.editor import editor
from src.infra.ai.tasks.content_scrapper import scraping_content_task

content_creation_task = Task(
    description=dedent(
        """
        Based on content scrapped provided from Scraper,
        write an engaging post based on the research and styles
        identified on the topic {topic} in pt-br.
        Use a charismatic, engaging and slightly informal tone.
        """
    ),
    expected_output='An engaging post ready to be published on LinkedIn in pt-br',
    agent=editor,
)

content_creation_task.context = [scraping_content_task]
