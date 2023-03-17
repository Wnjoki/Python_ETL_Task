
import pandas as pd
from psycopg2 import connect
from sqlalchemy import create_engine
import json
import pymysql
import os

engine = create_engine('mysql+pymysql://root:Njoki3130#:@localhost:3306/myDB')
df = pd.read_json(r"C:\Users\omuku\OneDrive\Desktop\Data Engineering\Python_ETL_Task\data\source1.json",lines = True)
df.to_sql("newTable", con=engine, if_exists = 'replace', index=False)


#Import JSON file into MySQL
    # read JSON file which is in the next parent folder
file = os.path.abspath(r'C:\Users\omuku\OneDrive\Desktop\Data Engineering\Python_ETL_Task\data') + "/source1.json"
json_data=open(file).read()
json_obj = json.loads(json_data)



# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val

# connect to MySQL
conn = pymysql.connect(host = 'localhost',user = 'root',passwd = 'Njoki3130#',db = 'test')
cursor = conn.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
     name = validate_string(item.get("name", None))
     height= validate_string(item.get("weight", None))
     weight = validate_string(item.get("company", None))

     cursor.execute("INSERT INTO testp (name, height,	weight) VALUES (%s,	%s,	%s)", (name,	height,	weight))
conn.commit()
conn.close()
        

        
                     