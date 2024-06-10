import requests
from bs4 import BeautifulSoup
from crewai_tools import BaseTool


class PostScrapperTool(BaseTool):
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
