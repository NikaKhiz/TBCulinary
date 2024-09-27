import asyncio
from database_generator import DatabaseGenerator
from scraper import Scrapper

CLIENT = 'mongodb://localhost:27017/'
DB = 'saladsdatabase'
COLLECTION = 'recipe_collection'

async def main():
    database = DatabaseGenerator(client=CLIENT, database=DB, collection_name=COLLECTION)
    scrapper = Scrapper()
    queries = mng_queries(DB)

    await scrapper.fetch_recipe_urls()
    await scrapper.fetch_salad_recipes()
    database.insert_recipes(scrapper._salads)

    await scrapper.close_conn()


if __name__ == '__main__':
    asyncio.run(main())
