from pymongo import  MongoClient

client = MongoClient("mongodb+srv://pallab13nayagram:pallab2000@cluster0.5biuws4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.asset_db
collection = db['assets']