import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myFirstDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]


coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})


documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)