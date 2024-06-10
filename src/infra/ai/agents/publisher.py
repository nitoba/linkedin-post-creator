from textwrap import dedent

from crewai import Agent

from src.infra.ai.llm import llm

publisher = Agent(
    role='Publisher',
    goal='Add the written post and the image prompt',
    verbose=True,
    backstory=dedent(
        """
        You are a content compiler, you can take different content and combine it all in one place.
        """
    ),
    allow_delegation=False,
    llm=llm,
)
