a=input("enter a character")
if '0'<=a<='9':
    print("it is a digit")
else:
    print("it is not a digit")


a=input("enter a character")
if 'a'<=a<='z' or 'A'<=a<='Z' or '0'<=a<='9':
     print("it is a digit or character")
else:
     print("it is special character")


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

        


