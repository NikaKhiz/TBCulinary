from pymongo import MongoClient


class MongodbConn:
    def __init__(self, db_name='saladsdatabase', collection_name='recipes'):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_collection(self):
        return self.collection

    def close(self):
        self.client.close()
