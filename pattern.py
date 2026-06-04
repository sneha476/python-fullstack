# #patterns
#1.
n=3
for i in range(n+1):
    for j in range(n):
        print("*", end=" ")
    print()

r=3
c=4

for i in range(r):
    for j in range(c+1):
        print("*", end=" ")
    print()
#2.
n=3
for i in range(n):
    for j in range(n+1):
        print(i, j, end=" ")
    print()
# #3.
n=3
for i in range(n):
    for j in range(n+1):
        print(j, end=" ")
    print()

# #4.
n=3
for i in range(n):
    for j in range(n+1):
        print(j, end=" ")
    print()
# #5.
r=3
c=4
val = 1
for i in range(r):
    for j in range(c):
        print(val, end=" ")
        val+=1
    print()

# #6.
r=3
c=4
val=65
for i in range(r):
    for j in range(c):
        print(chr(val), end=" ")
        val+=1
    print()
# #7
r=3
c=4
val=65
for i in range(r):
    for j in range(c):
        print(chr(val), end=" ")
        val += 1
    print()

# #8
n=4
m=3
val=65
for i in range(n):
    for j in range(m):
        print(chr(val), end=" ")
    print()

# #9
r=3
c=4
for i in range(r):
    val=65+i
    for j in range(c):
        print(chr(val), end=" ")
        val+=r
    print()
# #10
w=4
c=5
for i in range(w):
    for j in range(c):
        print(i+j,end=" ")
    print()
# #11
s=4
l=5
for i in range(s):
    for j in range(l):
        print(j+1, end=" ")
    print()
# #12.
o=4
c=5
for i in range(o):
    ch = chr(65 + i)
    for j in range(c):
        print(ch,end=" ")
    print()

# #13.
# s= 4
c=5
for i in range(s):
    for j in range(c):
        print(chr(65 + j),end=" ")
    print()

#14.
n = 3
for j in range(n + 1):
    for i in range(n):
        print(i, j, end=" ")
    print()


l=[10,20,30,40,50,60]
i=0
n=len(l)
while (i<n):
    print(l[i])
    i+=1
    w=input("enter a charcter")
if 'a'<=w<='z' or 'A'<=w<='Z':
    print(chr(ord(w)+32))
  
# if alphabet then print ascii value, if digit then displaythe next character, if special character then store it is in list,

special_characters=[]
x=input("enter a character:")
if '0'<=x<='9':
    print(ord(x),x)
elif 'a'<=x<='z' or 'A'<=x<='Z':
    a=chr(ord(x)+1)
    print(x,a)
else:
    special_characters.append(x)
    print("special character stored in list:", special_characters)




    # if a given character is lower case then convert it into upper case and if it is upper case then convert it into lower case and if it is a digit then print the next character and if it is a special character then store it in a list.
y=input("enter a character:")
if 'a'<=y<='z':
    print(chr(ord(y)-32))
elif 'A'<=y<='Z':
    print(chr(ord(y)+32))
else:
    print("character is not an alphabet")



# NUMBER GUESSING GAME
import random
secret=random.randint(1,20)
guess=54
print("welcome to the number guessing game")
while secret!=guess:
     guess=int(input("enter a number:"))
     if guess==secret:
          print("congratulations! you guessed the number")
          break 
     elif guess<secret:
          print("too low! try again")
     else:
          print("too high! try again")



# guessing the secret password


import random
secret_password="lathaa"
my_password="sneha"
count=0
print("welcome to the password guessing game")
while secret_password!=my_password:
     my_password=input("enter the password:")
     count+=1
     if my_password==secret_password:
          print("congratulations! you guessed the password",count,"attempts")
          break 
     else:
          print("wrong password! try again")

# COOKIE AND PACKS

pack=3
cookie=4
while(pack<=3):
    print(pack,"pack of cookies")
    pack+=1
    while(cookie<=4):
        print(cookie,"cookie")
        cookie+=1
print("pack=",pack)
     
# PATTERN PRINTING

n=3
for i in range(n):
     for j in range(n):
          print(i,j,end=" ")
     print()    #output:0 0 0 1 0 2
                    #    10 11 12
                    #    1 2 2 3 2 4
1.
# A A A
# B B B
# C C C

n=3
for i in range(n):     #0<3   1<3   2<3
     for j in range(n): #65+0=65  65+1=66  65+2=67
          print(chr(65+i),end=" ")  #output: A A A  BBB  C C C
     print()
2.
# A B C
# A B C        
# A B C

n=3
for i in range(n):
     for j in range(n):
          print(chr(65+j),end=" ")  #output: A B C  A B C  A B C
     print()
3.
# A B C
# D E F
# G H I

n=3
VAL=65
for i in range(n):       
     for j in range(n):
          print(chr(VAL+i*n+j),end=" ")  #output: A B C  D E F  G H I
     print()

4
n=3
for i in range(n):
    for j in range(n+1):
        print("*",end=" ")     
print()

5
#   A A A A 
#   B B B B
#   C C C C
n=3
for i in range(n):
    for j in range(n+1):
        print(chr(65+i),end=" ")
    print()

# 6.
# A B C D
# E F G H


n=2
val=65
for i in range(n):
    for j in range(n+1):
        print(chr(val),end=" ")
        val+=1
    print()

7.
# A A
# A A
# A A

n=3
for i in range(n):
    for j in range(n):
        print("A",end=" ")
    print()


8.
# A B C D E F
# G H I J K L

n=2
val=65
for i in range(n):
    for j in range(n+4):
        print(chr(val),end=" ")
        val+=1
    print()

8.
# A B C D E
# F G H I J

n=2
val=65
for i in range(n):
    for j in range(n+3):
        print(chr(val),end=" ")
        val+=1
    print()

9.
# A B C D E F G H
# I J K L M N O P 

n=2
val=65
for i in range(n):
    for j in range(n+6):
        print(chr(val),end=" ")
        val+=1
    print()


#   10.
# A B C D E F G H  I
# J K L M N O P Q R 


n=2
val=65
for i in range(n):
    for j in range(n+7):
        print(chr(val),end=" ")
        val+=1
    print()


11.
# A B C D E F G H I J
# K L M N O P Q R S T

N=2
val=65
for i in range(N):
    for j in range(N+8):
        print(chr(val),end=" ")
        val+=1
    print()

12.
# A B C D E F G H I J K
# L M N O P Q R S T U

m=2
val=65
for i in range(m):
    for j in range(m+9):
        print(chr(val),end=" ")
        val+=1
    print()



