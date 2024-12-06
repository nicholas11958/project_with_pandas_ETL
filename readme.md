# О проекте

Данный проект это ETL процесс, который выбирает данные из CSV файла, обрабатывает их и складывает в СУБД Postgresql.

Проект состоит из двух PY файлов, CSV с исходными данными и скриншота из DATA LENS.

Немного подробнее про PY файлы: 
1. load_data_from_csv.py - выгружает данные из csv
1. load_data_to_dm.py - выгружает данные из таблицы from_csv в dm предварительно их обработав.

В работе PY скриптов используется несколько таблиц для их создания используйте скрипт:
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
Немножко о таблицах:
1. from_csv - сюда складываются данные из csv файлы
1. from_csv_errors - сюда складываются поломонные данные из csv файла
1. dm - сюда складываются данные прошедшии трансформацию и готовые к визализации.

После создание таблиц в вашей СУБД можно запустить два PY файла одновременно и ожидает обновление результатов в конечной таблицы dm. На основании этих данных можно построить отчет в любой системе визуализации.