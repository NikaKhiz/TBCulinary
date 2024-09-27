from bs4 import BeautifulSoup
import re

# Removes whitespace characters
def clean_text(text):
    """Remove extra spaces and newlines from text."""
    return re.sub(r'\s+', ' ', text).strip()


# Fetch recipe information and returns data in valid format according to schema 
async def fetch_recipe(session, recipe_url, base_url):
    async with session.get(recipe_url) as response:
        if response.status != 200:
            return None
        
        result = await response.text()
        soup = BeautifulSoup(result, 'html.parser')

        # Parse fetched data
        title = soup.find('div', class_='post__title').find('h1').get_text().strip()
        url = soup.find('div', class_='post__img').find('a')['href']
        url = f'{base_url}{url.split("next=/")[-1]}'  
        category_link, subcategory_link = soup.find_all('a', class_='pagination__item')[2:]
        recipe_image = soup.find('div', class_='post__img').find('img')['src']
        recipe_description = soup.find('div', class_='post__description').get_text().strip()
        recipe_author = soup.find('div', class_='post__author').find('span').find('a').get_text().strip()
        recipe_servings = soup.find_all('div', class_='lineDesc__item')[1].get_text().strip()
        recipe_ingredients = soup.find_all('div', class_='list__item')
        recipe_stages_list = soup.find_all('div', class_='lineList__item')
        recipe_stages = [
            {
                'step': int(recipe_stage.find('div').get_text()),
                'description': recipe_stage.find('p').get_text()
            }
            for recipe_stage in recipe_stages_list
        ]

        # Redefine necessary properties
        category = {
            'title': category_link.get_text(),
            'url': f'{base_url}{category_link["href"]}'
        }
        subcategory = {
            'title': subcategory_link.get_text(),
            'url': f'{base_url}{subcategory_link["href"]}'
        }
        ingredients = [clean_text(ingredient.get_text()) for ingredient in recipe_ingredients]

        return {
            'title': title,
            'url': url,
            'category': category,
            'subcategory': subcategory,
            'image': recipe_image,
            'description': recipe_description,
            'author': recipe_author,
            'servings': recipe_servings,
            'ingredients': ingredients,
            'stages': recipe_stages
        }