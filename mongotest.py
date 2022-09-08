import pymongo

client = pymongo.MongoClient("")
# db = client.test

# print(db)

d = {
    "name":"Suraj",
    "email":"s@g.com",
    "phone":"987654321"
}

db1 = client['mongotest']
col1 = db1['test']

col1.insert_one(d)

# Hello Git