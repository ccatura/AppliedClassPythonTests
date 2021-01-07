import os
import csv
from time import time

# These will point to the 2 latest CSV files to compare.
file1 = "orion-servers.csv";
file2 = "orion-servers2.csv";

servers1 = [] # Stores the 1st CSV file
servers2 = [] # Stores the 2nd CSV file
serversHeader = [] # Stores the header titles. # Don't know if we really need this yet.
toChange = [] # Stores the record items to be changed. Is set up in 3's: 1) nodeID  2) Header title  3) Value
theTimeStart = time() # Can be deleted. Just to see howlong it takes to process.
orphanID = False; # Doesn't work yet. It is to find ID's in the 2nd CSV that were not in the 1st.

#Get modified times of CSV files
csvModTime1 = os.path.getmtime(file1)
csvModTime2 = os.path.getmtime(file2)


def addToChangeArray(nodeID, columnName, value):
    toChange.append(nodeID) # Add nodeID to toChange array
    toChange.append(columnName) # Add column name to toChange array
    toChange.append(value) # Add new value to toChange array

def importCSV(file, serversArray, headerArray):
    temp = []
    # Read CSV to array
    with open(file) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        temp.append(next(reader))
        # Puts first row of column titles into headerArray array
        for x in temp:
            for y in x:
                headerArray.append(y)
        temp.clear()
        # Puts the rest of the CSV file into serversArray array
        for row in reader: # each row is a list
            serversArray.append(row)

def compareCSV(serversArray1, serversArray2, headerArray):
    s1rowLength = range(len(serversArray1)) # Gets number of records in 1st CSV into range
    s1colLength = range(len(serversArray1[0])) # Gets number of columns in 1st CSV. We're assuming they will all havet he exact same amount of columns and titles.
    s2rowLength = range(len(serversArray2)) # Gets number of records in 2nd CSV into range
    for s1row in s1rowLength: # cycle through row of serverArray1
        for s1col in s1colLength: # cycle through items of serversArray1
            for s2row in s2rowLength: # cycle through row of serverArray2
                if (serversArray1[s1row][0] == serversArray2[s2row][0]): # check if ID is the same
                    #print("Orphan:",orphanID,"- NodeID: SAME")
                    if(serversArray1[s1row][s1col] != serversArray2[s2row][s1col]): # Checks if the value is different.
                        addToChangeArray(serversArray1[s1row][0], headerArray[s1col], serversArray2[s2row][s1col])

def findNewRecord(serversArray1, serversArray2):
    changeCount = 0
    s2rowLength = range(len(serversArray2)) # Gets number of records in 2nd CSV into range
    s1rowLength = range(len(serversArray1)) # Gets number of records in 1st CSV into range
    for s2row in s2rowLength: # cycle through row of serverArray1
        for s1row in s1rowLength: # cycle through row of serverArray2
            if (serversArray2[s2row][0] == serversArray1[s1row][0]): # check if ID is the same
                orphanID = False
                #print(serversArray2[s2row][0],"=",serversArray1[s1row][0])
                break
            else:
                orphanID = True
                #print(serversArray2[s2row][0],"!=",serversArray1[s1row][0])
        if(orphanID == True):
            print (serversArray2[s2row][0], "is a new record.")
            changeCount = changeCount + 1
    print()
    print(changeCount,"new records found.")




# I don't know if I need the "serversHeader" thing yet. Just leaving it here for now.
# It keeps track of the header title.




importCSV(file1, servers1, serversHeader) # Imports 1st CSV. Needs to be here.
importCSV(file2, servers2, serversHeader) # Imports 2nd CSV. Needs to be here.
compareCSV(servers1, servers2, serversHeader) # Compare the 2 CSVs. This needs servers1 and servers2 to be populated with values.


# This prints out the results. We can delete this block.
"""
for cc in range(0, len(toChange), 3):
    #print("Change #",round(((cc)/3)+1)) #Counts which number change this is
    print(toChange[cc])
    print(toChange[cc+1])
    print(toChange[cc+2])
    print()
"""

#This find records in the 2nd CSV that were not in the 1st CSV
#Whichever file is newer will be the 2nd file to be checked
if(csvModTime1 < csvModTime2):
    findNewRecord(servers1, servers2) 
else:
    findNewRecord(servers2, servers1)

theTimeEnd = time() # This is the time it finished processing


# Just prints out how long this all took. Just for myself.
print ("It took", round(theTimeEnd - theTimeStart), "seconds to find", round((len(toChange))/3), "changes in",len(servers2),"records.")
print()


