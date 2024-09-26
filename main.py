from database_generator import DatabaseGenerator

CLIENT = 'mongodb://localhost:27017/'
DB = 'saladsdatabase'
COLLECTION = 'recipe_collection'

def main():
    database_generator = DatabaseGenerator(client=CLIENT, database=DB, collection_name=COLLECTION)



if __name__ == '__main__':
    main()

