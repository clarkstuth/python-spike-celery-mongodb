from pymongo import MongoClient
import pymongo

client = MongoClient()

collection = client.test_db.test_collection

print "Data currently stored in mongo: "
for item in collection.find():
    print item
