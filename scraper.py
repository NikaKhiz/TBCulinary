import asyncio, aiohttp
from bs4 import BeautifulSoup
from utils import fetch_recipe

class Scrapper():
    def __init__(self, items_per_page=6) -> None:
        self._salads_url = []
        self._base_url = 'https://kulinaria.ge'
        self._items_per_page = items_per_page
        self._session = aiohttp.ClientSession()
        self._salads = []

    # Fetch and save urls for recipies for future usage
    async def fetch_recipe_urls(self):
        page = 1
        while True:
            url = f'{self._base_url}/receptebi/cat/salaTebi/?page={page}'
            async with self._session.get(url) as response:
                if response.status != 200:
                    break

                result = await response.text()
                soup = BeautifulSoup(result, 'html.parser')
                recipes = soup.find_all('div', class_='box')

                for recipe in recipes:
                    description = recipe.find('div', class_='box-space')
                    url = description.find('a')['href']
                    self._salads_url.append(self._base_url + url)

                if len(recipes) < self._items_per_page:
                    break  

                page += 1

    # Fetches salad recipes simultaneously and currently save them in private propery 
    async def fetch_salad_recipes(self):
        self._salads.extend(await asyncio.gather(*(fetch_recipe(self._session, url, self._base_url) for url in self._salads_url)))


    # Close connection 
    async def close_conn(self):
        await self._session.close()
