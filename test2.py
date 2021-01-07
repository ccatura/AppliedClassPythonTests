from collections import defaultdict
import os
import csv

clear = lambda: os.system('cls')
clear()


file = "C:/Users/chacat1/Desktop/My Stuff/Homework/Python Tests/servers1.csv"

servers1 = {}
with open(file, 'r') as data_file:

    reader = csv.reader(data_file)
    row1 = next(reader)

    header = [];
    for x in row1:
        header.append(x);

    print ("Header Row:", header);
    print();

    for row in data_file:
        row = row.strip().split(",")

        #This is the format, but it's not correct to get the nested dictionary
        #servers1[row[0]] = header[1] + ': ' + row[1], header[2] + ': ' + row[2], header[3] + ': ' + row[3];

        for x in header:

                servers1.setdefault(row[0],{})[x] = row[1];


        # https://stackoverflow.com/questions/39233973/get-all-keys-of-a-nested-dictionary

        #servers1.setdefault(row[0],{})[row[1]] = int(row[2])


# How it should look: {'001': {'Type': 'Windows 10', 'Location': 'Ohio'}, etc... 


print (servers1);



"""
# Comparing two values
i = servers1.get("003").get("Location");
j = servers2.get("003").get("Location");

print("Old Record: 003 - Location:", i);
print("New Record: 003 - Location:", j);
print();

if (i == j):
    print ("Records are identical.");
else:
    print ("Records are different.");
"""

