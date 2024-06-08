import requests
from bs4 import BeautifulSoup
from crewai_tools import BaseTool


# Definindo DuckDuckGoTool
class DuckDuckGoTool(BaseTool):
    name: str = 'DuckDuckGo Search Tool'
    description: str = 'Tool to search the web using DuckDuckGo.'

    def _run(self, topic: str) -> str:
        search_url = 'https://duckduckgo.com/html/'
        params = {'q': topic}
        response = requests.post(search_url, data=params)

        if response.status_code != 200:
            return 'Failed to fetch search results'

        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', class_='result__a')

        search_results = []
        for result in results[:5]:  # Limiting to top 5 results
            title = result.text
            link = result['href']
            search_results.append(f'{title}: {link}')

        return '\n'.join(search_results)


# Definindo ScrapeWebsiteTool
class ScrapeWebsiteTool(BaseTool):
    name: str = 'LinkedIn Scraper'
    description: str = (
        "Tool to scrape LinkedIn profiles to analyze influencers' writing styles."
    )

    def _run(self, profile_url: str) -> str:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(profile_url, headers=headers)

        if response.status_code != 200:
            return 'Failed to fetch profile data'

        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('div', class_='feed-shared-update-v2')

        post_texts = []
        for post in posts[:5]:  # Limiting to top 5 posts
            post_text = post.find('span', class_='break-words').text.strip()
            post_texts.append(post_text)

        return '\n'.join(post_texts)


# Definindo DuckDuckGoScraperTool
class DuckDuckGoScraperTool(BaseTool):
    name: str = 'DuckDuckGo Scraper Tool'
    description: str = (
        'Tool to scrape content from URLs provided by DuckDuckGo search results.'
    )

    def _run(self, urls: list) -> str:
        scraped_content = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        for url in urls:
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                scraped_content.append(f'Failed to fetch content from {url}')
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            page_content = ' '.join([para.text for para in paragraphs])

            scraped_content.append(page_content)

        return '\n\n'.join(scraped_content)
