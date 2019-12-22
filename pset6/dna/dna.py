import sys
import csv
import pprint

#check to be sure usage is appropriate
if len(sys.argv) != 3:
    print("Usage: python dna.py strcounts dnasequence")
    sys.exit()

# assign csv to variable

strcounts = sys.argv[1]
sequence = ""

# empy holder for importing csv into array of ordered dicts

d = []

# input csv into d
# referenced https://docs.python.org/2/library/csv.html
with open(strcounts, newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        d.append(row)

# input txt into sequence
with open(sys.argv[2], 'r') as myfile:
  sequence = myfile.read()

# empty holder for our list, as we parse through sequence
l = []

index = 0

# look for each subsequence, and repetitions
for key in d[0].items():
    #do initial search
    currentkey = "".join(key[0])
    newkey = "".join(key[0])
    count = 0
    starti = sequence.find("".join(key[0]))
    # add a zero if no substring at all
    if starti == -1:
        l.append(0)
    # otherwise
    else:
        count += 1
        l.append(count)
        while True:
            #while we can still find still larger repetitions
            newkey = currentkey*(count+1)
            starti = sequence.find(newkey)
            if starti == -1:
                break
            # if this is the largest count we've found, note it down in l
            else:
                count += 1
                if (count > l[index] or len(l) == 0 or index < len(l)):
                    l[index] = count
    index += 1

# make new counters and bools for next search
looking = True
index = 0
name = ""

# search through array of ordereddicts to see which person matches
for person in d:
    if looking == False:
        break
    #if we still want to be searching through people, then search through that person's characteristics
    for key, value in person.items():
        #if we're searching beyond the l, then we should be done
        if index >= len(l):
            looking = False
            break
        #otherwise, if we're at a name, note it down for printing later
        elif (key == "name"):
            name = value
            index += 1
        #otherwise, if at a number, see if it matches the person and substring we're currently considering
        elif (key != "name"):
            if int(value) != int(l[index]):
                index = 0
                break
            else:
                index += 1
# if we're still looking, then no match
if looking == True:
    print("No match")
# otherwise, print out the name
else:
    print(name)









