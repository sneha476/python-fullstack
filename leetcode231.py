# a=input("enter a character")
# if '0'<=a<='9':
#     print("it is a digit")
# else:
#     print("it is not a digit")


# a=input("enter a character")
# if 'a'<=a<='z' or 'A'<=a<='Z' or '0'<=a<='9':
#      print("it is a digit or character")
# else:
#      print("it is special character")


<<<<<<< HEAD
# s=input("enter a character")
# if '0'<=s<='9':
#      print(ord(s),s)
=======
s=input("enter a character")
if '0'<=s<='9':
     print(ord(s),s)
    
### leetcode236:##

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n%3==0:
            n//=3
        return n==1

        
>>>>>>> 34a3ee03fee47b350207f0fc0a71d65f143705d3















number =153

# Separate digits and compute the length of the number
digits = [int(d) for d in str(number)]
length = len(digits)

# Raise each digit to the power of the length
powers = [digit ** length for digit in digits]

# Sum the powered digits
result_sum = sum(powers)

# Check the condition: does the sum equal the original number?
is_armstrong = result_sum == number

print("Number:", number)
print("Length:", length)
print("Digits:", digits)
print("Each digit^length:", powers)
print("Sum:", result_sum)
print("Condition (sum == number):", is_armstrong)
