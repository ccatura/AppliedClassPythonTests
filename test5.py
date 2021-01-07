import csv
import os

clear = lambda: os.system('cls')
clear()

"""file1 = "orion-servers.csv";
file2 = "orion-servers2.csv";"""
file1 = "servers1.csv"
file2 = "servers2.csv"

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
            
def getItem(serversArray, headerArray, attrib, serverID):
    count = 0

    print("Attrib: ", attrib, "\nserverID: ", serverID, "\n\n")
    print()
    for x in headerArray:
        if(x == attrib): #Find the attribute
            print (x, "found at column:", count)
            for y in serversArray:
                if(y[0] == serverID):
                    print(y[count])
                if (count > len(x) -1):
                    count = 0
        count = count + 1

            

importCSV(file1, servers1, servers1Header)

importCSV(file2, servers2, servers2Header)

getItem(servers1, servers1Header, "location", "200")





"""# Prints contents of serversArray array
for x in serversArray:
    for y in x:
        print (y, ' ', end = '')
    print()
"""

"""# Prints contents of headerArray array
for x in headerArray:
    print (x, ' ', end = '')
"""
