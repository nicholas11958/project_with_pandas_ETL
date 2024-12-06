import pandas as pd
import numpy as np
import time
import psycopg2
from sqlalchemy import create_engine
#Подключение к БД
conn_string = 'postgresql://postgres123:G734kUks3j6*uw393@90.156.150.127:5432/db1'
db = create_engine(conn_string)
conn= db.connect
conn1 = psycopg2.connect( 
    database="db1", 
  user='postgres123',  
  password='G734kUks3j6*uw393',  
  host='90.156.150.127',  
  port= '5432'
) 

#Запускаем код в бесконечном цикле т.к. данные могут приходить бесконечно
while True:
    time.sleep(30)
    df = pd.read_sql_query('select * from "from_csv"',con=db)
    length = df.__len__()
    grouped_df = df.groupby(['Type', 'District'], as_index=False).agg({'TotalArea': 'mean', 'Price': 'mean'})
    grouped_df['Avg_Per_Sm'] = grouped_df.Price / grouped_df.TotalArea
    a = grouped_df
    a.rename(columns={'TotalArea': 'Avg_Total_Area', 'Price': 'Avg_Price'}, inplace=True)
    a = a.replace([np.inf, -np.inf], '0')
    a['Counf_Of_Ad'] = length
    print(a)
    a.to_sql('dm', db, if_exists= 'replace', index=False)

