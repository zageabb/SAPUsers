#!/bin/bash

# usage: export_to_csv.sh <database.sqlite>

sqlite3 $1 "SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%';" | while read table; do

echo $table

sqlite3 $1 <<!
.headers on
.mode csv
.output "$table.csv"
select * from "$table";
!

done
