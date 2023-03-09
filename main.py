import sys
import petl as etl
import psycopg2 as pg
import sqlalchemy 
import warnings



dbConnection={'opperations': "dbname"}

path = "https://assets.datacamp.com/production/repositories/5899/datasets/19d6cf619d6a771314f0eb489262a31f89c424c2/ppr-all.zip"

# Import the required method
from zipfile import ZipFile

with ZipFile(path, "r") as f:
    # Get the list of files
    file_names = f.namelist()
    print(file_names)
    # Extract the CSV file
    csv_file_path = f.extract(file_names[0])
    print(csv_file_path)
