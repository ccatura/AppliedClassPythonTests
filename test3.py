import csv
import os

clear = lambda: os.system('cls')
clear()






#file = "C:/Users/chacat1/Desktop/My Stuff/Homework/Python Tests/servers1.csv";
#file = "C:/Users/Chuck/Desktop/To Backup/Homework/Python Tests Home/orion-servers.csv";
#file = "servers1.csv";
file1 = "orion-servers.csv";
file2 = "orion-servers2.csv";

servers1 = []
servers2 = []
servers1Header = []
servers2Header = []
temp = []

# FIRST SERVER FILE
with open(file1) as csvfile:
    reader = csv.reader(csvfile) # change contents to floats


    temp.append(next(reader))
    
    # Puts first row of column titles into servers1Header array
    for x in temp:
        for y in x:
            servers1Header.append(y)
    temp.clear()

    """# Prints contents of servers1Header array
    for x in servers1Header:
        print (x, ' ', end = '')
    """

    # Puts the rest of the CSV file into servers1 array
    for row in reader: # each row is a list
        servers1.append(row)
        

    """# Prints contents of servers1 array
    for x in servers1:
        for y in x:
            print (y, ' ', end = '')
        print()
    """


# SECOND SERVER FILE
with open(file2) as csvfile:
    reader = csv.reader(csvfile) # change contents to floats


    temp.append(next(reader))
    
    # Puts first row of column titles into servers1Header array
    for x in temp:
        for y in x:
            servers2Header.append(y)
    temp.clear()

    """# Prints contents of servers2Header array
    for x in servers2Header:
        print (x, ' ', end = '')
    """

    # Puts the rest of the CSV file into servers1 array
    for row in reader: # each row is a list
        servers2.append(row)
        

    """# Prints contents of servers2 array
    for x in servers2:
        for y in x:
            print (y, ' ', end = '')
        print()
    """





print (servers1)
print()
print()
print (servers2)