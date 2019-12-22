# TODO
import cs50
import csv
import sys

from cs50 import sql

#usage check

if len(sys.argv) != 2:
    print("Usage: roster.py house")
    sys.exit()

#set database

db = cs50.SQL("sqlite:///students.db")

#get house we want to filter by
house_chosen = sys.argv[1]

#filter table

table = db.execute("SELECT first, middle, last, birth FROM students WHERE house = %s ORDER BY last, first", house_chosen)

#print statement
for n in table:
    #2 names
    if n["middle"] == None:
        print(n["first"] + " " + n["last"] + ", born " + str(n["birth"]))
    #3 names
    else:
        print(n["first"] + " " + n["middle"] + " " + n["last"] + ", born " + str(n["birth"]))