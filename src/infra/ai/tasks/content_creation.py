from textwrap import dedent

from crewai import Task

from src.infra.ai.agents.editor import editor
from src.infra.ai.tools.post_scrapper import PostScrapperTool

content_creation_task = Task(
    description=dedent(
        """
        Write an engaging post based on the research and styles
        identified on the topic {topic} in pt-br.
        Use a charismatic, engaging and slightly informal tone.
        """
    ),
    expected_output='An engaging post ready to be published on LinkedIn in pt-br',
    tools=[PostScrapperTool()],
    agent=editor,
)
