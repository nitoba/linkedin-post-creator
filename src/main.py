from agents import designer, pesquisador, redator, scraper
from crewai import Crew, Process
from tasks import (
    criacao_conteudo_tarefa,
    criacao_prompts_tarefa,
    pesquisa_tarefa,
    scraping_conteudo_tarefa,
    scraping_tarefa,
)

crew = Crew(
    agents=[pesquisador, scraper, redator, designer],
    tasks=[
        pesquisa_tarefa,
        scraping_tarefa,
        scraping_conteudo_tarefa,
        criacao_conteudo_tarefa,
        criacao_prompts_tarefa,
    ],
    process=Process.sequential,
    verbose=2,
)

# Executando a crew
result = crew.kickoff(
    inputs={
        'topic': 'NestJs como framework backend',
        'profile_url': 'https://www.linkedin.com/in/vitormarkis/recent-activity/all/',
    }
)
print(result)
