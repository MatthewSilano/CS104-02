#Sum/Average Program
#Your first and last name: Matthew Silano
#Your student ID: s1292285

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers
#Instead of searching for a name in the list
#   Compute the sum of all 10 numbers
#   Compute the average for all 10 numbers

#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

numberlist = []
sumInt = 0
avgInt = 0.0


#for loop to enter 20 numbers

for i in range(0,20):
    number = int(input("Enter a number:"))
    numberlist.append(number)



#for loop to sum/average 20 numbers

for x in range(0,20):
    sumInt=sumInt + numberlist [x]
print(sumInt)

for x in range(0,20):
    avgInt=(sumInt/20)
print(avgInt)
