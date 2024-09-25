import requests
from bs4 import BeautifulSoup
import re


def fetch_page_content(url):
    """Fetch the content of the page."""
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def clean_text(text):
    """Remove extra spaces and newlines from text."""
    return re.sub(r'\s+', ' ', text).strip()


def extract_recipe_details(recipe):
    """Extract details from a single recipe."""
    title_tag = recipe.find('a', class_='box__title')
    if not title_tag:
        return None

    recipe_name = title_tag.text.strip()
    recipe_url = "https://kulinaria.ge" + title_tag['href']

    img_tag = recipe.find('img')
    image_url = img_tag['data-src'] if img_tag and img_tag.has_attr('data-src') else img_tag['src']
    if image_url.startswith("/"):
        image_url = "https://www.kulinaria.ge" + image_url

    recipe_soup = fetch_page_content(recipe_url)

    meta_url = recipe_soup.find('meta', property='og:url')
    recipe_url = meta_url['content'] if meta_url else recipe_url

    h1_tag = recipe_soup.find('h1', class_='post__title')
    recipe_name = h1_tag.text.strip() if h1_tag else recipe_name

    author_tag = recipe_soup.find('div', class_='post__author')
    author = author_tag.find('a').text.strip() if author_tag and author_tag.find('a') else 'N/A'

    description = recipe_soup.find('div', class_='post__description').text.strip() if recipe_soup.find('div', class_='post__description') else 'N/A'

    servings_tag = recipe_soup.find_all('div', class_='lineDesc__item')
    servings = next((tag.text.strip() for tag in servings_tag if 'ულუფა' in tag.text), 'N/A')

    categories = recipe_soup.select('.pagination__item')
    if len(categories) >= 2:
        main_category = categories[-2].text.strip()
        main_category_url = "https://kulinaria.ge" + categories[-2]['href']
        subcategory = categories[-1].text.strip()
        subcategory_url = "https://kulinaria.ge" + categories[-1]['href']
    else:
        main_category = subcategory = main_category_url = subcategory_url = 'N/A'

    ingredients = [clean_text(item.text) for item in recipe_soup.select('.list__item') if item.text.strip()]

    stages = []
    for idx, step in enumerate(recipe_soup.select('.lineList__item'), start=1):
        step_description = step.find('p').text.strip() if step.find('p') else 'N/A'
        stages.append({"step": str(idx), "description": step_description})

    return {
        "recipe_name": recipe_name,
        "recipe_url": recipe_url,
        "main_category": {"title": main_category, "url": main_category_url},
        "subcategory": {"title": subcategory, "url": subcategory_url},
        "image_url": image_url,
        "description": description,
        "author": author,
        "servings": servings,
        "ingredients": ingredients,
        "stages": stages
    }


def main():
    base_url = "https://kulinaria.ge/receptebi/cat/salaTebi/"
    page_number = 1

    while True:
        url = f"{base_url}?page={page_number}"
        soup = fetch_page_content(url)
        recipes = soup.find_all('div', class_='box--author')

        if not recipes:
            break

        for recipe in recipes:
            details = extract_recipe_details(recipe)
            if details:
                print(f"რეცეპტის დასახელება: {details['recipe_name']}")
                print(f"რეცეპტის მისამართი: {details['recipe_url']}")
                print(f"რეცეპტის მთავარი კატეგორიის დასახელება და მისამართი: {details['main_category']['title']} ({details['main_category']['url']})")
                print(f"რეცეპტის ქვეკატეგორიiს დასახელება და მისამართი: {details['subcategory']['title']} ({details['subcategory']['url']})")
                print(f"მთავარი სურათის მისამართი: {details['image_url']}")
                print(f"მოკლე აღწერა: {details['description']}")
                print(f"ავტორი სახელი: {details['author']}")
                print(f"ულუფების რაოდენობა: {details['servings']}")
                print("რეცეპტის ინგრედიენტები:")
                for ingredient in details['ingredients']:
                    print(f" - {ingredient}")
                print("რეცეპტის მომზადების ეტაპები:")
                for stage in details['stages']:
                    print(f"ნაბიჯი {stage['step']}: {stage['description']}")
                print("\n")

        page_number += 1


if __name__ == "__main__":
    main()
