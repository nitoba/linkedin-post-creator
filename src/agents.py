from crewai import Agent
from llm import llm
from tools import DuckDuckGoScraperTool, DuckDuckGoTool, ScrapeWebsiteTool

pesquisador = Agent(
    role='Pesquisador',
    goal='Pesquisar tópicos relevantes no LinkedIn',
    verbose=True,
    backstory='Você é um pesquisador dedicado, sempre buscando as últimas tendências e tópicos de interesse.',
    tools=[DuckDuckGoTool()],
    allow_delegation=False,
    llm=llm,
)

scraper = Agent(
    role='Scraper',
    goal='Analisar perfis de influenciadores no LinkedIn',
    verbose=True,
    backstory='Você é um especialista em scraping, capaz de extrair dados valiosos de perfis de influenciadores pesquisando nas suas atividades recentes.',
    tools=[ScrapeWebsiteTool()],
    allow_delegation=False,
    llm=llm,
)

redator = Agent(
    role='Redator',
    goal='Escrever posts engajantes para o LinkedIn',
    verbose=True,
    backstory='Você é um escritor talentoso, capaz de criar conteúdo que ressoa com a audiência e gera engajamento.',
    tools=[DuckDuckGoTool(), ScrapeWebsiteTool(), DuckDuckGoScraperTool()],
    allow_delegation=False,
    llm=llm,
)

designer = Agent(
    role='Designer',
    goal='Criar prompts descritivos para imagens que ilustrarão os posts no LinkedIn',
    verbose=True,
    backstory='Você é um designer criativo, capaz de gerar descrições detalhadas para imagens que complementam e melhoram os posts.',
    tools=[],  # O designer não precisa de ferramentas adicionais
    allow_delegation=False,
    llm=llm,
)
