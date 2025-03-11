
# print hello world
print("Hello World")

"""
This is a multi line comment.
Printing another message to the display.
"""
print("Let us learn python")

# Variable declaration
name = "Ashish"
skill = 'python'
grade = 10
phone_num=7896789645
marks = 256.3
cleared = False

print(type(name))
print(type(grade))
print(type(marks))
print(type(cleared))
print(type(phone_num))


# Create a python program to add the sum of two numbers

num1 = 10
num2 = 20
print(num1 , num2, (num1 + num2))

# Assign many values to multiple variables
a, b, c = 1, 2, 3
print(a, b, c)

# Assign one value to many varibles
d = e = f = 5
print(d, e, f)

"""
Python built in datatypes

Text      str
Numeric   int, float
Boolean   bool
"""

name = str("Arun")
age = int(24)
is_employed = bool(False)

# Operators in python
"""
They perform predefined operations on values and variables.
Arithematic   Operators
Logical       Operators
Assignment    Operators
Comparison    Operators
"""

# print("Type your name")
# name = input()
# print("Hello, ", name)

# Conditional programming
# n1 = input("Enter number 1: ")
# n2 = input("Enter number 2: ")
# print(n1, n2)

# if n1 > n2:
#   print(n1, " is greater")
# elif n1 == n2:
#   print(n1, " and ", n2, " are same.")
# else:
#   print(n2, " is greater")

# if n1 > n2 or n1 == n2:
#   pass

citizenship = ""
# Nested if block
if age >= 18:
  if citizenship == "indian":
    # print('You can vote')
    # Placeholder for future code
    pass

# Alternative to nested if
if age >= 18 and citizenship == "indian":
  pass

# Iterative Programming

index = 10
i = 0
while i <= index:
  # print("Hello ", i)
  i = i + 1
else: # else block can run statements once the loop condition is evalued to false
  print("Loop ended")

print("continue")

i = 0
while i<6:
  i += 1
  if i == 3:
    continue
  print(i)

print("break")

i = 0
while i<6:
  i += 1
  if i == 3:
    break
  print(i)

# Declare arrays in python
fruits = ["Apple", "Mango", "Banana", "Kiwi"]
index = 0

while index < len(fruits):
  print(fruits[index])
  index += 1

print("for in loop")
for fruit in fruits:
  print(fruit)

class Student:
  pass

def some_function():
  pass