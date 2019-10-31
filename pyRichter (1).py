#Python Richter Scale Calculation
#Your first and last name: Matthew Silano
#Your ID: s1292285

#Algorithm:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)

# test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6



richter = float(input("Enter the Richter scale value:"))

if richter == 1 or 1.1 or 1.2 or 1.3 or 1.4 or 1.5 or 1.6 or 1.7 or 1.8 or 1.9:
    print ("Microearthquakes, not felt, or felt rarely.")
elif richter == 2 or 2.2 or 2.3 or 2.4 or 2.5 or 2.6 or 2.7 or 2.8 or 2.9:
    print ("Felt slightly by some people. No damage to buildings.")
elif richter == 3 or 3.1 or 3.2 or 3.3 or 3.4 or 3.5 or 3.6 or 3.7 or 3.8 or 3.9:
    print ("Often felt by people, but very rarely causes damage. Shaking of indoor objects can be noticeable.")
elif richter == 4 or 4.1 or 4.2 or 4.3 or 4.4 or 4.5 or 4.6 or 4.7 or 4.8 or 4.9:
    print ("Noticeable shaking of indoor objects and rattling noises. Felt by most people in the affected area. Slightly felt outside.")
elif richter == 5 or 5.1 or 5.2 or 5.3 or 5.4 or 5.5 or 5.6 or 5.7 or 5.8 or 5.9:
    print ("Can cause damage of varying severity to poorly constructed buildings. At most, none to slight damage to all other buildings. Felt by everyone.")
elif richter == 6 or 6.1 or 6.2 or 6.3 or 6.4 or 6.5 or 6.6 or 6.7 or 6.8 or 6.9:
    print ("Damage to a moderate number of well-built structures in populated areas. Earthquake-resistant structures survive with slight to moderate damage. Poorly designed structures receive moderate to severe damage.")
elif richter == 7 or 7.1 or 7.2 or 7.3 or 7.4 or 7.5 or 7.6 or 7.7 or 7.8 or 7.9:
    print ("Causes damage to most buildings, some to partially or completely collapse or receive severe damage. Well-designed structures are likely to receive damage. Felt across great distances with major damage mostly limited to 250 km from epicenter.")
elif richter == 8 or 8.1 or 8.2 or 8.3 or 8.4 or 8.5 or 8.6 or 8.7 or 8.8 or 8.9:
    print ("Major damage to buildings, structures likely to be destroyed. Will cause moderate to heavy damage to sturdy or earthquake-resistant buildings. Damaging in large areas. Felt in extremely large regions.")
elif richter == 9:
    print ("At or near total destruction – severe damage or collapse to all buildings. Heavy damage and shaking extends to distant locations. Permanent changes in ground topography.")
else:
    print ("Invalid Value")

