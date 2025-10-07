# Subscripting
print("Hello"[0]) #will print H #this is called subscripting

print("Hello"[-1])
print("Hello"[4])
# these two lines will print o

# Strings
print("123" + "345")

# Integer = whole number
123 + 345

# Large Integers
print(123_456_789) #the same as 123,456,789; In Python, 123_456_789 represents an integer literal. The underscores (_) within a number are used as visual separators to improve readability and are completely ignored by the Python interpreter. This means that 123_456_789 is treated as the exact same integer value as 123456789.

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

print(type("Hello")) #this will return <class 'str'>
print(type("abc"))
print(type(3.14))
print(type(True))

# +, -, *, /

# BMI calculator
height = 1.65 
weight = 84
bmi = weight / height ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

score = 0
# user scores a point
score += 1 # the same as score = score + 1
print(score)

# formatted string is used to mix different data types
score = 0
height = 1.8
is_winning = True
print(f"Your score is ={score}, your height is {height}. You are winning is {is_winning}")

# Project

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 or 15- "))
people = int(type("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
