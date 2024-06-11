from textwrap import dedent
from crewai import Agent

social_media = Agent(
    role='Social Media Creator',
    goal='Write engaging texts to carousels for social media post',
    verbose=True,
    backstory=dedent(
        """
        You are an expert copywriter specializing in social media, particularly Linkedin.
        """
)
)