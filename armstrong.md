# More basic concepts

Here's the definition of an **Armstrong Number** in **Markdown format**:  

## Armstrong Number

An **Armstrong number** is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

## Formula

For an _n_-digit number:

\[
\text{Sum of each digit}^n = \text{Original Number}
\]

## Examples

1. **153** (3-digit number)
   \[
   1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
   \]

2. **9474** (4-digit number)
   \[
   9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474
   \]

3. **9475** (Not an Armstrong number)
   \[
   9^4 + 4^4 + 7^4 + 5^4 = 6561 + 256 + 2401 + 625 = 9843 \neq 9475
   \]

## Steps to Check Armstrong Number

1. **Count the number of digits** in the given number.
2. **Extract each digit** one by one.
3. **Raise each digit to the power of the total digits** and compute the sum.
4. **Compare the sum** with the original number:
   - If they are equal, the number is an **Armstrong number**.
   - Otherwise, it is **not an Armstrong number**.

     
Here is the **pseudocode** for the `count_digits` function:  

```
FUNCTION count_digits(num):
    IF num == 0 THEN
        RETURN 1  // Special case: 0 has 1 digit

    SET count = 0
    WHILE num > 0 DO:
        num = num / 10  // Remove the last digit
        count = count + 1  // Increment digit count
    END WHILE

    RETURN count
END FUNCTION
```

### **Explanation:**
1. **If `num` is 0**, return `1` because 0 has exactly one digit.
2. **Initialize `count = 0`**.
3. **Use a loop to divide `num` by 10** in each step, removing the last digit.
4. **Increment `count`** each time a digit is removed.
5. **Return `count`** when `num` becomes `0`.

# Dry Run of `count_digits` Function

### **Input:** `num = 153`  
### **Expected Output:** `3` (since 153 has 3 digits)

---

## **Dry Run Table**

| Iteration | `num` (Before) | `num % 10` (Last Digit) | `num = num / 10` (After) | `count` (Incremented) |
| --------- | -------------- | ----------------------- | ------------------------ | --------------------- |
| **Start** | 153            | -                       | -                        | 0                     |
| **1**     | 153            | 3                       | 15                       | 1                     |
| **2**     | 15             | 5                       | 1                        | 2                     |
| **3**     | 1              | 1                       | 0                        | 3                     |
| **End**   | 0              | -                       | -                        | **3 (Final Count)**   |

---

### **Final Output:**  
The function returns `3`, which is correct.