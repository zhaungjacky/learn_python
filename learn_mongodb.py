import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["feathers-chat-mongodb"]

mycol = mydb["messages"]

# dblists = mydb.list_collection_names()
# for x in dblists:
#     print(x)
# print("The database exists.") if "mydatabase" in dblists else print("not exists")

# mydb = myclient["mydatabase"]

# data={
#     "text": "hello again hi",
#     "userId": '65b61611918d5344890d1783',

#     "createdAt": datetime.datetime.now()
# }
# x = mycol.insert_one(data)
# manyX= mycol.insert_many([])
# print(x.inserted_id)

for x in mycol.find({},{ "_id": 0, "text": 1, "createdAt": 1 }):
  print(x)


