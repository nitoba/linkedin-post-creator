import requests
from bs4 import BeautifulSoup
from crewai_tools import tool


@tool('DuckDuckGoSearch')
def search(topic: str):
    """Search the web for information on a given topic"""

    search_url = 'https://duckduckgo.com/html/'
    params = {'q': topic}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(search_url, params=params, headers=headers)

    if response.status_code != 200:
        return 'Falha ao buscar resultados de pesquisa'

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('a', class_='result__a')

    search_results = []
    for result in results[:5]:  # Limitar aos 5 principais resultados
        title = result.text
        link = result['href']
        search_results.append(f'{title}: {link}')

    urls = [result['href'] for result in results[:5]]

    return urls
