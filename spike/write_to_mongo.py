from pymongo import MongoClient

client = MongoClient()

db = client.test_db

result = db.dataset.insert_one({'name': 'clark', 'role': 'architect'})
print "data inserted at {}".format(result.inserted_id)

result = db.dataset.insert_one({'name': 'ted', 'role': 'plumber'})
print "data inserted at {}".format(result.inserted_id)

result = db.dataset.insert_one({'name': 'bill', 'role': 'plumber'})
print "data inserted at {}".format(result.inserted_id)

all_plumbers = db.dataset.find({'role':'plumber'})
print "All plumbers:"
for plumber in all_plumbers:
    print plumber['name']

print "Total employees: {}".format(db.dataset.find().count())