#import the packages
import os
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
from sqlalchemy.pool import Pool
import mysql.connector
import json

    
    # Load the csv file equipment_failure_sensors.log
source1csv = pd.read_csv(r"C:\Users\omuku\OneDrive\Desktop\Data Engineering\Python_ETL_Task\data\source1.csv",)
                                


    # Load the log file equipment.json
#source1json= json.loads(r"C:\Users\omuku\OneDrive\Desktop\Data Engineering\Python_ETL_Task\data\source1.json")



     # Create a database connection -- DATABASE TARGET
db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="persons", # schema used to be load
        )
    # Create a MySQL cursor to process the steps
db_cursor = db_connection.cursor()
    
    # Total heights ?
total = """SELECT SUM(height) AS TOTAL_height
            FROM source1csv"""
        
db_cursor.execute(total)
records = db_cursor.fetchall()
        
print("This is the total height:" + total)
        

        
        
        

        
                     
    




