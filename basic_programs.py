# Print numbers from 1 to N
n=int(input("enter a number: "))
if n>0:
    for i in range(1,n+1):
        print(i)

# Sum of first N numbers
n=int(input("enter a number: "))
if n>0:
    sum=0
    for i in range(1,n+1):
        sum+=i
    print("Sum of first",n,"numbers is:",sum)

#Check even or odd
s=int(input("enter a number:"))
if s%2==0:
    print(s,"is an even number")
else:
    print(s,"is an odd number")

# Check positive, negative, or zero
x=int(input("enter a number: "))
if x>0:
    print(x,"is a positive number")
elif x<0:
    print(x,"is a negative number")
else:
    print(x,"is zero")

# Find largest of 3 numbers
a=int(input("enter first number: "))
b=int(input("enter second number: "))   
c=int(input("enter third number: "))
if a>=b and a>=c:
    print(a,"is the largest number")
elif b>=a and b>=c:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")

#Check leap year
Y=int(input("enter a year: "))
if (Y%4==0 and Y%100!=0) or (Y%400==0):
    print(Y,"is a leap year")
else:
    print(Y,"is not a leap year")

# Multiplication table
m=int(input("enter a number: "))
for i in range(1,10):
    print(m,"x",i,"=",m*i)

# Factorial
n=int(input("enter a number: "))
if n==0:
    print("Factorial of",n,"is 1")
else:
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print("Factorial of",n,"is",factorial)

# Count digits in a number
num=int(input("enter a number: "))
count=0
while num>0:
    num//=10
    count+=1
print("Number of digits is:",count)

# Reverse a number
num=int(input("enter a number: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print("Reverse of the number is:",reverse)

# Sum of digits
num=int(input("enter a number: "))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num//=10
print("Sum of digits is:",sum) 

# Check palindrome number
num=int(input("enter a number: "))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
if original==reverse:
    print(original,"is a palindrome number")
else:
    print(original,"is not a palindrome number")

# Check Armstrong number
num=int(input("enter a number: "))
order=len(str(num))
sum=0
temp=num
while temp>0:               # checktemp>0
    digit=temp%10           #  digit=temp%10=last digit
    sum+=digit**order       
    temp//=10               
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

# Check prime number
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if (count==2):
    print(n,"prime")
else:
    print(n,"not prime")

# Print all primes from 1 to N
for n in range(1, 25):
    count=0  
    for i in range(1, n+1):
        if n%i==0:
            count+=1
    if count==2:  
        print(n)

# GCD/HCF of two numbers
a =int(input("Enter first number: "))
b =int(input("Enter second number: "))
while b!= 0:
    a,b=b,a%b
print("GCD/HCF of", a, "is", a)
# LCM of two numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a==0 or b==0:
    print("Please enter non-zero numbers")
else:
    lcm=max(a, b)
    while True:
        if lcm % a==0 and lcm%b==0:
            print("LCM =", lcm)
            break
        lcm+=1

# Fibonacci series
# first two terms
nterms=int(input("How many terms? "))
n1=0
n2=1
count=0
# check if the number of terms is valid
if nterms<=0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms==1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
#  generate fibonacci series
else:
    print("Fibonacci series:")
    while count < nterms:
        print(n1)
        nth=n1+n2
# update values
        n1=n2
        n2=nth
        count+=1

# Power of a number (a^b)
l=int(input("enter a number:"))
m=int(input("enter a number:"))
n=l**m
print(n)

# Decimal to Binary
dec_num=int(input('Enter a decimal number: '))
print(bin(dec_num),"in binary.")

