import os
import csv
from time import time
import glob

def get2LatestFiles(fileExtension, csvPath, fileSearchString):
    # This will get  the latest CSV files
    allFiles = csvPath + "*." + fileExtension
    allFiles = (glob.glob(allFiles))
    count = range(len(allFiles))
    allFiles.sort(key=os.path.getmtime, reverse=True)
    return (allFiles)

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
            #print (serversArray2[s2row][0], "is a new record.")
            changeCount = changeCount + 1
    print()
    print(changeCount,"new records found.")

fileExtension = "csv"
csvPath ="csv/"
fileSearchString = "orion-servers"
print("Getiing 2 latest",fileExtension, "files from path:",csvPath)
file1 = (get2LatestFiles(fileExtension, csvPath, fileSearchString)[1]) # Gets the next-to-last modified CSV
file2 = (get2LatestFiles(fileExtension, csvPath, fileSearchString)[0]) # Gets the latest modified CSV
print("Found file 1:",file1)
print("Found file 2:",file2)
print()

#Get modified times of CSV files
csvModTime1 = os.path.getmtime(file1)
csvModTime2 = os.path.getmtime(file2)
if(csvModTime1 < csvModTime2):
    print(file2, "is newer file.")
    print(file1, "is older file.")
else:
    print(file1, "is newer file.")
    print(file2, "is older file.")

servers1 = [] # Stores the 1st CSV file
servers2 = [] # Stores the 2nd CSV file
serversHeader = [] # Stores the header titles. # Don't know if we really need this yet.
toChange = [] # Stores the record items to be changed. Is set up in 3's: 1) nodeID  2) Header title  3) Value
theTimeStart = time() # Can be deleted. Just to see howlong it takes to process.
orphanID = False # Doesn't work yet. It is to find ID's in the 2nd CSV that were not in the 1st.

importCSV(file1, servers1, serversHeader) # Imports 1st CSV. Needs to be here.
importCSV(file2, servers2, serversHeader) # Imports 2nd CSV. Needs to be here.
compareCSV(servers1, servers2, serversHeader) # Compare the 2 CSVs. This needs servers1 and servers2 to be populated with values.

#This find records in the 2nd CSV that were not in the 1st CSV
#Whichever file is newer will be the 2nd file to be checked
if(csvModTime1 < csvModTime2):
    findNewRecord(servers1, servers2)
else:
    findNewRecord(servers2, servers1)


theTimeEnd = time() # This is the time it finished processing
# Just prints out how long this all took. Just for myself.
print (round((len(toChange))/3), "changes in",len(servers2),"records.")
print ("Time elapsed:", round(theTimeEnd - theTimeStart), "seconds.")
print()

