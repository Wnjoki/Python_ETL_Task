#import the packages
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine


    

#Read CSV file with Pandas and MySQL
# read CSV file
column_names = ['name','height', 'weight']

df = pd.read_csv(r'C:\Users\omuku\OneDrive\Desktop\Data Engineering\Python_ETL_Task\data\source1.csv', header = None, names = column_names)
print(df)

#connect to MySQL
engine = create_engine('mysql://root:Njoki3130#@localhost/test')

#Create new MSQL table
with engine.connect() as conn, conn.begin():
    df.to_sql('csv', conn, if_exists='append', index=False)
        

        
    
    




