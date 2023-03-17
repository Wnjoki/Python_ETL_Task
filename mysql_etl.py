# python modules
import pandas as pd
import mysql.connector
import psycopg2 
import json


db = mysql.connector.connect(user = 'root',password= "Njoki3130#", database="test")
cursor = db.cursor()

query= "select name,height from csv"
cursor.execute(query)

myallData= cursor.fetchall()

all_name = []
all_height= []
for name,height in myallData:
    all_name.append(name)
    all_height.append(height)

#store the data into CSV

dict= {'name': all_name,'height':all_height}

df = pd.DataFrame(dict)
df.to_csv(r'C:\Users\omuku\OneDrive\Desktop\Data Engineering\Python_ETL_Task\data\df.csv')

print(df)

#store the data into json

dict_JSON = json.dumps(dict)
print(dict_JSON)