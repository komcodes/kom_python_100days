# if condition:
#    do this:
#else:
#    do this

water_level = 80
if water_level > 80:
    print("Drain Water!")
else: 
    print("Continue!")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry you have to grow taller before you can ride!")

#Comparison Operators
# > is greater than
# < is less than
# >= is greater than or equal to
# <= is less than or equal to
# == is equal to
# != is not equal to

# Modulo Operator -> %
# gives out the remainder -> 10 % 5 = 0
# 10 % 3 -> 3 with 1 remaining

# Write a code to check if the number you give as input is even or odd. Print EVEN and ODD accordingly.
number_to_check = int(input("What is the number that you want to check? "))
print(number_to_check % 2)
if number_to_check % 2 == 0:
    print("Even") 
else:
    print("Odd") 

# Nested if else
# if condition:
#    if another condition:
#       do this:
#    else: 
#        do this
#else:
#    do this    

# continuing the previous code
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")    
else:
    print("Sorry you have to grow taller before you can ride!")

# if / elif / else 
# if condition1:
#    do A
# elif condition2:
#    do B   
# else:
#    do this 

# continuing the previous code
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")    
else:
    print("Sorry you have to grow taller before you can ride!")

# Practice Question: BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

# Code
weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

# Multiple if
# if condition1:
#    do A
# if condition2:
#    do B
# if condiiton3:
#    do C

# continuing the previous code
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: #or you can write: elif 45 <= age <= 55:
        print("Everything is going to be okay. ave a free ride on us!")    
    else:
        bill = 12
        print("Adult Tickets are $12.")    

    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
    # Add $3 to their bill
       bill = bill + 3 # bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride!")

# Pizza Delivery Project
# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the toal for their order and tell them how much they hvae to pay.
# Small Pizza (S): $15
# Medium Pizza (M): $20
# Large Pizza (L): $25
# Add pepperoni for small pizza (Y or N): + $2
# Add pepperoni for medium or large pizza (Y or N): + $3
# Add extra cheese for any size pizza (Y or N): + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperni on your pizza? Y or N: ")
extra_cheese: input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.") 

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3    

# todo: work out their final amount based on whether they want extra cheese.
if extra_cheese == "Y":
   bill += 1
print(f"Your final bbill is ${bill}.")   

# if condition1 & condition2 & condition3:
#    do this
# else:
#    do this

# AND operator
# True and True = True
# False and True = False
# True and False = False

# OR operator
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# Not True = False

# PROJECT (DAY 3):
# Treasure Island
# Your goal today is to build a "Choose your own adventure game".

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
# using "" wont work and will show error here.

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input('You\'re at a crossroad, where do you want to go? ' \
                 'Type "left" or "right".\n').lower()
# \ the backslash symbol is used for the single quote for the syntax above, it is placed before the single quote to tell the computer to avoid the single quote or ESCAPE it.

if choice1 == "left":
    # Continue in game
    choice2 = input('You\'ve come to a lake, there is an island in the middle of the lake. ' \
              'Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if choice2 == "wait":
        # game will continue
        choice3 = input('You arrive at the island unharmed.'
                       'There is a house with 3 doors.'
                       'One red, One yellow and one blue.'
                       'Which colour do you choose?\n').lower()
        if choice3 == "red":
           print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
           print("You found the treasure. You win!")
        elif choice3 == "blue":     
           print("You eneter a room of beasts. Game Over.") 
        else:
           print("You chose a door that doesn't exist. Game Over.")   
    else: 
        print("You got attacked by an angry trout. Game Over.")    
else:
    print("You fell into a hole. Game Over.")
        



