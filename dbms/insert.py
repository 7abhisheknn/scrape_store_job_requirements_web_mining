import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db"]
mycol = mydb["dt"]

myquery = { "keyWord": "python engineer" }

mydoc = mycol.find_one(myquery)

print(mydoc["l"])