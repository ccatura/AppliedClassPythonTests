import os
import csv
from time import time
import glob

class CompareAndUpdate:
    def __init__(self, fileExtension, filepath, fileSearchString):
        self.fileExtension = fileExtension
        self.csvPath = "csv/"
        self.fileSearchString = "orion-servers"
        self.file1 = self.get2LatestFiles(fileExtension, self.csvPath, self.fileSearchString)[1] # Gets the next-to-last modified CSV
        self.file2 = self.get2LatestFiles(fileExtension, self.csvPath, self.fileSearchString)[0] # Gets the latest modified CSV
        self.csvModTime1 = os.path.getmtime(self.file1)
        self.csvModTime2 = os.path.getmtime(self.file2)

        self.servers1 = [] # Stores the 1st CSV file
        self.servers2 = [] # Stores the 2nd CSV file
        self.serversHeader = [] # Stores the header titles. # Don't know if we really need this yet.
        self.toChange = [] # Stores the record items to be changed. Is set up in 3's: 1) nodeID  2) Header title  3) Value
        self.orphanID = False # Doesn't work yet. It is to find ID's in the 2nd CSV that were not in the 1st.

        self.importCSV(self.file1, self.servers1, self.serversHeader) # Imports 1st CSV. Needs to be here.
        self.importCSV(self.file2, self.servers2, self.serversHeader) # Imports 2nd CSV. Needs to be here.
        self.compareCSV(self.servers1, self.servers2, self.serversHeader) # Compare the 2 CSVs. This needs servers1 and servers2 to be populated with values.

        #This find records in the 2nd CSV that were not in the 1st CSV
        #Whichever file is newer will be the 2nd file to be checked
        if(self.csvModTime1 < self.csvModTime2):
            self.findNewRecord(self.servers1, self.servers2)
        else:
            self.findNewRecord(self.servers2, self.servers1)

    def get2LatestFiles(self, fileExtension, csvPath, fileSearchString):
        # This will get  the latest CSV files
        self.allFiles = self.csvPath + "*." + self.fileExtension
        self.allFiles = (glob.glob(self.allFiles))
        #count = range(len(self.allFiles)) #i think i can delete this
        self.allFiles.sort(key=os.path.getmtime, reverse=True)
        return (self.allFiles)

    def importCSV(self, file, serversArray, headerArray):
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

    def compareCSV(self, serversArray1, serversArray2, headerArray):
        print()
        print("INDIVIDUAL VALUE CHANGES")
        print()
        s1rowLength = range(len(serversArray1)) # Gets number of records in 1st CSV into range
        s1colLength = range(len(serversArray1[0])) # Gets number of columns in 1st CSV. We're assuming they will all havet he exact same amount of columns and titles.
        s2rowLength = range(len(serversArray2)) # Gets number of records in 2nd CSV into range
        for s1row in s1rowLength: # cycle through row of serverArray1
            for s1col in s1colLength: # cycle through items of serversArray1
                for s2row in s2rowLength: # cycle through row of serverArray2
                    if (serversArray1[s1row][0] == serversArray2[s2row][0]): # check if ID is the same
                        if(serversArray1[s1row][s1col] != serversArray2[s2row][s1col]): # Checks if the value is different.
                            self.addToChangeArray(serversArray1[s1row][0], headerArray[s1col], serversArray2[s2row][s1col])

    def findNewRecord(self, serversArray1, serversArray2):
        print()
        print("ADDED RECORDS")
        print()
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
                print ("Added new record:", serversArray2[s2row][0])
                changeCount = changeCount + 1
        print()
        print()
        print(changeCount,"new records.")

    def addToChangeArray(self, nodeID, columnName, value):
        self.toChange.append(nodeID) # Add nodeID to toChange array
        self.toChange.append(columnName) # Add column name to toChange array
        self.toChange.append(value) # Add new value to toChange array
        print("Updated NodeID:", nodeID)
        print("Column:", columnName)
        print("Value:", value)
        print()



theTimeStart = time() # Can be deleted. Just to see howlong it takes to process.

a = CompareAndUpdate(
    "csv",
    "csv/",
    "orion-servers"
    )

theTimeEnd = time() # This is the time it finished processing
# Just prints out how long this all took. Just for myself.
print (round((len(a.toChange))/3), "changes in",len(a.servers2),"records.")
print ("Time elapsed:", round(theTimeEnd - theTimeStart), "seconds.")
print()

