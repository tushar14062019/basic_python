"""
Write a program that repeatedly adds the digits of a number until the sum is a single digit.

Algorithm
-----------------------
1. Start
2. Accept a number
3. if the number has only one digit then return the number
4. Extract the digits and calaculate the sume of these digits
5. Verify if the sum of digits is a single digit number
6. If yes print the sum
7. If no repeat step 4
8. Stop

Example
  Input: 9875
  Step 1: 9 + 8 + 7 + 5 = 29
  Step 2: 2 + 9 = 11
  Step 3: 1 + 1 = 2
  Output: 2

"""

num = int(input("Enter a number: "))

while num >= 10:
    total = 0
    while num > 0:
        total =total+num % 10
        num =num//10
    num = total
print("Output:",num)
