from crewai import Crew


class CreatePostUseCase:
    def __init__(self, crew: Crew) -> None:
        self.crew = crew

    def execute(self, topic: str) -> str:
        return self.crew.kickoff(
            inputs={
                'topic': topic,
            }
        )
