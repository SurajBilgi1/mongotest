import pymongo

client = pymongo.MongoClient("mongodb+srv://suraj:surajineuron@cluster0.u6rrf7p.mongodb.net/?retryWrites=true&w=majority")
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