from textwrap import dedent

from crewai import Task

from src.infra.ai.agents.designer import designer

prompt_creation_task = Task(
    description=dedent(
        """
        Create a detailed description for an image that illustrates the post on the topic {topic}.
        """
    ),
    expected_output='A detailed description for an image related to the post.',
    tools=[],  # O designer não precisa de ferramentas adicionais
    agent=designer,
)
