import asyncio
from database_generator import DatabaseGenerator
from queries import mng_queries
from scraper import Scrapper

CLIENT = 'mongodb://localhost:27017/'
DB = 'saladsdatabase'
COLLECTION = 'recipe_collection'

async def main():
    database = DatabaseGenerator(client=CLIENT, database=DB, collection_name=COLLECTION)
    collection = database.collection
    scrapper = Scrapper()

    print('Fetching recipes. Please wait for a while...')
    await scrapper.fetch_recipe_urls()
    await scrapper.fetch_salad_recipes()
    
    database.insert_recipes(scrapper._salads)
    queries = mng_queries(collection)

    print(f'The average number of ingredients : {queries["avg_num_ingredients"]}')
    print(f'The average number of stages : {queries["avg_num_stages"]}')
    print(f'Most servings : {queries["most_servings"]["title"]}. რეცეპტის ნახვა შეგიძლიათ ლინკზე: {queries["most_servings"]["url"]}')
    print(f'Author with most recipes : {queries["auth_with_most_recipes"]["id"]} with {queries["auth_with_most_recipes"]["recipes"]} recipes.')

    await scrapper.close_conn()


if __name__ == '__main__':
    asyncio.run(main())
