from pymongo import MongoClient
myclient =MongoClient("mongodb://localhost:27017/")
mydb = myclient["Students"]
mycol = mydb["Studentdata"]

myquery = { "name": "Himanshu" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)