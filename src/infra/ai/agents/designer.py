from textwrap import dedent

from crewai import Agent

from src.infra.ai.llm import llm

designer = Agent(
    role='Designer',
    goal=dedent(
        """
        Create 3 alternative descriptive prompts for images that illustrate LinkedIn posts.
        """
    ),
    verbose=True,
    backstory='Create descriptive prompts for images that illustrate LinkedIn posts',
    tools=[],  # O designer não precisa de ferramentas adicionais
    allow_delegation=False,
    llm=llm,
)
