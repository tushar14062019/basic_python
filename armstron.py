"""
An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

Algorithm to check if a number is an armstrong number or not

Begin
Accept a number as num
Count the total digits of the number as count
Extract each number 
Raise each to the power of the total digits and compute sum
Verify the sum is same as that of the number
if Yes then it is armstrong otherwise it is not
End

Example
num     = 153
count   = 3
sum     = 1^3 + 5^3 +  3^3 = 153
sum     == num => Yes

Psuedocode
START
  INPUT num
  SET   sum   = 0
  SET   temp  = num
  SET   num_digits = count_digits(num)

  WHILE temp > 0 DO
    digit = temp % 10                     // extract the last digit
    sum = sum + (digit ^ num_digits)      
    temp = temp / 10
  END WHILE

  IF sum == num THEN
    PRINT 'Armstrong number'
  ELSE
    PRINT 'Not an armstrong number'
  END IF
END

FUNCTION count_digits(num)
  SET count = 0
  IF num == 0
    RETURN 1
  WHILE num > 0 DO
    num = num / 10
    count += 1  
  END WHILE
  RETURN count
END FUNCTION

"""

# Armstrong number python program

# Define a function named count_digits that will accept a number and return the number of digits.
def count_digits(num):
  if num == 0:
    return 1
  count = 0
  while num > 0:
    num = num // 10   # integer division
    count +=1
  return count

def is_armstrong(num):
  num_digits = count_digits(num)
  temp = num
  sum = 0

  while temp > 0:
    digit = num % 10
    sum = sum + (digit ** num_digits)
    temp = temp // 10

  return sum == num

num = 153
print(is_armstrong(num))