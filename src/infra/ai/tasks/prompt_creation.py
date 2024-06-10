from textwrap import dedent

from crewai import Task

from src.infra.ai.agents.designer import designer

prompt_creation_task = Task(
    description=dedent(
        """
        Create 3 alternatives detailed descriptions for images
        that illustrates the post on the topic {topic}.
        """
    ),
    expected_output='3 alternatives detailed descriptions for images related to the post.',
    tools=[],  # O designer não precisa de ferramentas adicionais
    agent=designer,
)
