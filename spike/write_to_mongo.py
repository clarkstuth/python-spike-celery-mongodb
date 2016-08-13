from pymongo import MongoClient
import pymongo

client = MongoClient()

db = client.test_db
dataset = db.dataset
dataset.create_index([("name", pymongo.ASCENDING)])
dataset.create_index([("role", pymongo.ASCENDING)])

result = dataset.insert_one({'name': 'clark', 'role': 'architect'})
print "data inserted at {}".format(result.inserted_id)

result = dataset.insert_one({'name': 'ted', 'role': 'plumber'})
print "data inserted at {}".format(result.inserted_id)

result = dataset.insert_one({'name': 'bill', 'role': 'plumber'})
print "data inserted at {}".format(result.inserted_id)

employees = dataset.find()
print "Employees:"
for employee in employees:
    print employee['name']

print "Plumbers:"
for employee in dataset.find({"role": "plumber"}):
    print employee['name']

total_employees = dataset.count()
print "Total Employees: {}".format(total_employees)