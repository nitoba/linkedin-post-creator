from textwrap import dedent

from crewai import Agent

from src.infra.ai.llm import llm
from src.infra.ai.tools.post_scrapper import PostScrapperTool

editor = Agent(
    role='Editor',
    goal='Write engaging posts for LinkedIn',
    verbose=True,
    backstory=dedent(
        """
        You are a talented writer, capable of creating content that resonates with
        your audience and generates engagement.
        You are an expert in writing LinkedIn posts replicating any influencer style
        """
    ),
    tools=[PostScrapperTool()],
    allow_delegation=False,
    llm=llm,
)
