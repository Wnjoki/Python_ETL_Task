import os
import datetime
import dotenv
import pymongo
import urllib.parse 

dotenv.load_dotenv()
mongo_database_name = 'sample_airbnb'
mongo_collection_name = 'listingsAndReviews'
localhost=urllib.parse.quote_plus('localhost:27017')
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
conn_string="mongodb+srv://%s%s%s/%s"%("root","password","localhost:8081","mongo_database_name")

client = pymongo.MongoClient(conn_string)
db = db_client[mongo_database_name]
collection = db[mongo_collection_name]
