
import pymongo


class DatabaseGenerator():
    def __init__(self, client='mongodb://localhost:27017/', database='saladsdatabase', collection='recipe_collection') -> None:
        self.client = client
        self.database = database
        self.collection = collection
        pass


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
    def collection(self, collection):
        self._collection = self._database[collection] 

