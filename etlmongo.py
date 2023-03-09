#Importing necessary libraries for the project
from http import client
import pandas as pd
import pymongo
import petl as etl


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
#read the data
cardata=pd.read_csv(r'C:\Users\omuku\OneDrive\Desktop\Data Engineering\Python_ETL_Task\data\cardata.csv')
print(cardata.head())

#connect to destination
conn_string="mongodb+srv://%s:%s%s/%s"%("root","password","localhost:8081","cardata")
client = pymongo.MongoClient(conn_string)



#loading data into a CSV  file
table1 = etl.fromdb(conn_string,cardata)
 
table2 = etl.sort(table1,'Name')
 
etl.tocsv(table2,'cardata.csv')


