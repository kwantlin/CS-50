# TODO
import cs50
import csv
import sys

from cs50 import sql

#set database
db = cs50.SQL("sqlite:///students.db")

#usage check
if len(sys.argv) != 2:
    print("Usage: python import.py characters.csv")
    sys.exit()

#start reading in
with open(sys.argv[1], "r") as characters:
    reader = csv.DictReader(characters, delimiter = ',')
    #read in by row
    for row in reader:
        #two names
        if row["name"].count(' ') == 2:
            #input names
            first = row["name"].split()[0]
            middle = row["name"].split()[1]
            last = row["name"].split()[2]
        #three names
        elif row["name"].count(' ') == 1:
            #input names
            first = row["name"].split()[0]
            middle = None
            last = row["name"].split()[1]
        #set house
        house = row["house"]
        #set birth
        birth = int(row["birth"])
        #insert into database
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)