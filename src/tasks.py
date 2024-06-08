from agents import designer, pesquisador, redator, scraper
from crewai import Task
from tools import DuckDuckGoScraperTool, DuckDuckGoTool, ScrapeWebsiteTool

pesquisa_tarefa = Task(
    description='Pesquisar um tópicos relevantes e tendências relacionado ao tema {topic}.',
    expected_output='Um tópico relevante e tendência.',
    tools=[DuckDuckGoTool()],
    agent=pesquisador,
)

scraping_tarefa = Task(
    description='Analisar perfis de influenciadores no LinkedIn para entender o estilo de escrita relacionado ao tema {topic}.',
    expected_output='Dados analisados dos perfis de influenciadores.',
    tools=[ScrapeWebsiteTool()],
    agent=scraper,
)

scraping_conteudo_tarefa = Task(
    description='Scrapear o conteúdo das URLs providas pelo DuckDuckGoTool para o tema {topic}.',
    expected_output='Conteúdo scrapado das URLs.',
    tools=[DuckDuckGoScraperTool()],
    agent=scraper,
)

criacao_conteudo_tarefa = Task(
    description='Escrever um post engajante baseado nas pesquisas e estilos identificados sobre o tema {topic} em pt-br.',
    expected_output='Um post engajante pronto para ser publicado no LinkedIn em pt-br',
    tools=[DuckDuckGoScraperTool()],
    agent=redator,
)

criacao_prompts_tarefa = Task(
    description='Criar uma descrição detalhada para uma imagem que ilustrará o post sobre o tema {topic}.',
    expected_output='Uma descrição detalhada para uma imagem relacionada ao post.',
    tools=[],  # O designer não precisa de ferramentas adicionais
    agent=designer,
)
