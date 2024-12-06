# О проекте

Проект состоит из двух py файлов, CSV с данными и скриншота из DATA LENS.
1. load_data_from_csv.py - выгружает данные из csv
1. load_data_to_dm - выгружает данные из таблицы from_csv в dm предварительно их обработав.

В работе используется несколько таблиц для их создания используйте скрипт:
```
create table from_csv(
"Type" text,
"District" text,
"Price" float,
"TotalArea" float
);
create table from_csv_errors(
"Type" text,
"District" text,
"Price" float,
"TotalArea" float
);
create table dm(
"Type" text,
"District" text,
"Avg_Total_Area" float,
"Avg_Price" float,
"Avg_per_sm" float
);
```