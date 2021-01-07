import csv
import os

clear = lambda: os.system('cls')
clear()

file1 = "orion-servers.csv";
file2 = "orion-servers2.csv";
#file1 = "servers1.csv"
#file2 = "servers2.csv"

servers1 = []
servers2 = []
servers1Header = []
servers2Header = []

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
    s1rowLength = range(len(serversArray1))
    s1colLength = range(len(serversArray1[0]))
    s2rowLength = range(len(serversArray2))
    for s1row in s1rowLength: #entire row of serverArray1
        for s1col in s1colLength: #item of serversArray1
            for s2row in s2rowLength: #entire row of serverArray2
                if (serversArray1[s1row][0] == serversArray2[s2row][0]): # check if ID is the same
                    #for s2col in s1colLength: #item of serversArray2
                    if(serversArray1[s1row][s1col] != serversArray2[s2row][s1col]):
                        #print("Servers1 Row:",s1row, "   Servers1 Column:",s1col)
                        #print("Servers2 Row:",s2row, "   Servers2 Column:",s1col)
                        print("Difference in:\nColumn [" + headerArray[s1col] + "] of Server NodeID [" + serversArray1[s1row][0] + "]")
                        #print("ServerID 1:",serversArray1[s1row][0])
                        #print("ServerID 2:",serversArray2[s2row][0])
                        print ("Servers1:",serversArray1[s1row][s1col],"\nServers2:",serversArray2[s2row][s1col], "\n\n")




importCSV(file1, servers1, servers1Header) # Import first CSV

importCSV(file2, servers2, servers2Header) # Import 2nd CSV

compareCSV(servers1, servers2, servers1Header) # Compare CSVs



