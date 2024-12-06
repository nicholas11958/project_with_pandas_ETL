import pandas as pd
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
#Считываем CSV файл
data = pd.read_csv("portugal_listinigs.csv")
#Запускаем код в бесконечном цикле т.к. данные могут поступать бесконечно
while True:
  df = data
  df1 = df.sample(n=2)
  filteted_df = df1.query('Price < 50000 or TotalArea < 20') 
  #Из-за условия df может оказаться пустым
  if filteted_df.empty:
    print('It`s empty')  
    time.sleep(1)
  else:
    new_filtered_df = filteted_df[['Type', 'District', 'Price', 'TotalArea']]
    check_nan = new_filtered_df.isnull().any().any()
    #Борьба с NAN значениями
    if check_nan == False:
      new_filtered_df.to_sql('from_csv', db, if_exists= 'append', index=False)
      time.sleep(10)
    else:
      new_filtered_df.to_sql('from_csv_errors', db, if_exists= 'append', index=False)
      print("PROBLEM STRING")





