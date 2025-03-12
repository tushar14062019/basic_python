"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""

First_number = int(input("Enter the Number: "))
Last_number= int(input("Enter the Number: "))

for i in range(First_number, Last_number):
    num = 1
    for j in range(2, i-1):
        if i%j == 0:
            num = 0
    if num == 1:
        print(i)
