import os
clear = lambda: os.system('cls')
clear()

abc = "Florfida"

servers1 = {
  "001" : {
    "Type"     : "Windows 10",
    "Location" : "Ohio"
  },
  "002" : {
    "Type"     : "Linux",
    "Location" : "California"
  },
  "003" : {
    "Type"     : "Unix",
    "Location" : abc,
    "Chicken"  : "Soft",
    "Name"     : "Charlie",
    "Height"   : "Shorter than his girlfriend"
  }
}

servers2 = {
  "001" : {
    "Type"     : "Windows 10",
    "Location" : "Ohio"
  },
  "002" : {
    "Type"     : "Linux",
    "Location" : "California"
  },
  "003" : {
    "Type"     : "Windows 95",
    "Location" : "Floridat",
    "Name"     : "Richard"
  }
}



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


print();
print();
print(servers1);