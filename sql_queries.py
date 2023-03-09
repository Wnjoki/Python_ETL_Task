from unicodedata import name
import mysql.connector
from mysql.connector import Error
import pandas as pd
import numpy as np
def create_connection(host_name, user_name, user_password): # type: ignore
    connection = None
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="Njoki3130#"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "")

#create a database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE myData"
create_database(connection, create_database_query)


def create_connection(host_name,user_name, user_password,database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="Njoki3130#",
            database="myData"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "","database")


data=pd.read_csv(r"C:\Users\omuku\OneDrive\Desktop\Data Engineering\Python_ETL_Task\data\source1.csv")