
names  = []
n1 = input("enter first name:")
n2 = input ("enter next name:")
n3 = input ("enter next name:")
n4 = input ("enter next name:")
n5 = input ("enter next name:")
n6 = input ("enter next name:")
n7 = input ("enter next name:")
n8 = input ("enter next name:")
n9 = input ("enter next name:")
n10 = input ("enter final name:")

names.append(n1)
names.append(n2)
names.append(n3)
names.append(n4)
names.append(n5)
names.append(n6)
names.append(n7)
names.append(n8)
names.append(n9)
names.append(n10)

import sys

stop=False
while not stop: 
    search = input("enter search name:")
    if search in names:
        print(search, "was found")
    else:
        print (search, "was not found")
    if search == "end":
        break
    if search == "End":
        break




    
