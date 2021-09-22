from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
myclient = MongoClient("mongodb://127.0.0.1:27017")
print("connection successful", myclient)
mydb=myclient['Employee']
information=mydb.employeeinformation
records=[{
        'firstname':"himanshu",
        'lastname':"Sugandhi",
        'department':"Developer"
    },
    {
        'firstname': "sheetal",
        'lastname': "Sugandhi",
        'department': "housewife"

    }]
information.insert_many(records)
# print(result)