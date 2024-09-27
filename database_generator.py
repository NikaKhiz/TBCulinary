
import pymongo
from pymongo.errors import CollectionInvalid
from schemas import recipe_schema


class DatabaseGenerator():
    def __init__(self, client='mongodb://localhost:27017/', database='saladsdatabase', collection_name='recipe_collection') -> None:
        self.client = client
        self.database = database
        self.collection = collection_name


    @property
    def client(self):
        return self._client
    
    @client.setter
    def client(self, client):
        self._client = pymongo.MongoClient(client)
    

    @property
    def database(self):
        return self._database
    
    @database.setter
    def database(self, database):
        self._database = self._client[database]
    
    
    @property
    def collection(self):
        return self._collection
    
    @collection.setter
    def collection(self, collection_name):
        try:
            self._collection = self._database.create_collection(collection_name, validator = recipe_schema)
        except CollectionInvalid:
            self._collection = self._database[collection_name]


    def insert_recipes(self, recipes):
        try:
            self.collection.insert_many(recipes)
        except Exception as e:
            print(e)
