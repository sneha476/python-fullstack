<<<<<<< HEAD
# n=153
# l=len(str(n))
# print(l)
# for i in str(n):
#     print(int(i),end=" ")
# n=5
# l5=[]
# for i in range(1,n+1):
#     l5.append(i*10)
#     l5.append(i+10)
#     l5.append(i%10)
#     l5.append(i-10)
# print(l5)
# lm=[(val+10,val*10,val%10,val-10) for val in range(1,n+1)]
# print(lm)
# m=12
# l1=[val for val in range(1,m+1) if val%2==0]
# print(l1)
# l2=[val for val in range(1,m+1) if val&1==1]
# print(l2)
# l3=["even" if val%2==0  else "odd" for val in range(1,m+1) ]
# print(l3)
# n=5
# l4=[[val for val in range(1,11) if val%2==0],[val for val in range(1,11) if val%2==1]]
# print(l4)
# m=5
# l=[-1,2,3,-4,5,-6,-3]
# neg=[]
# pos=[]
# k=[neg.append(val) if val<0 else pos.append(val) for val in l]
# print(neg)
# print(pos)
# separete v and c in string "hi hello ravi garu"
# v-->aeiou
# c-->hhllrvgr
# l="hi hello ravi garu"
# p=[val for val in l if val in "aeiou"],[val for val in l if val not in "aeiou" ]
# print(p,sep="\n")
# d={"ravi","raju"}
# d1={val.upper() for val in d}
# print(d1)

# minimum value in list
l=[1,2,3,4,5]
min=min(l)
n=[val for val in range(len(l)) if min<val and min==val]
print(min)
## maximum value in list
l=[1,2,3,4,5]
max=max(l)
n=[val for val in range(len(l)) if max<val and max==val]
print(max)


=======
# # # Print numbers from 1 to N
print("<------Print numbers 1 to N------>")
n=1
for i in range(10):
    i+=1
    print(i,end=",")

print()

# Sum of first N numbers
print("<------Sum of first N numbers------>")
n=int(input("enter a value:"))
sum=n*(n+1)//2
print("sum =",sum)

# Check even or odd
print("<------Check even or odd------>")
n=int(input("enter a value:"))
if(n%2==0):
    print(n," is a even number")
else:
    print(n," is a odd number")

# Check positive, negative, or zero
print("<------Check positive, negative, or zero------>")
score=(int(input("enter a value:")))
if(score>0):
    print("score is a positive")
elif(score<0):
    print("score is a negitive")
elif(score==0):
    print("score is a zero")

#Find largest of 3 numbers
print("<------Find largest of 3 numbers------>")
a=int(input("enter a value:"))
b=int(input("enter a value"))
c=int(input("enter a value"))
if a>=b and a>=c:
    print("largest number a is:",a)
elif b>=c and b>=c:
    print("largest number b is:",b)
else:
    print("largest number c is:",c)

#Check leap year
print("<------Check leap year------>")
n=int(input("enter a value:"))
digit=n%4
if digit%4==0:
    print(n,"is a leap year")
else:
    print(n,"is a not leap year")

#Multiplication table
print("<------Multiplication table------>")
for i in range(1,11,1):
    print(2,"*",i,"=",2*i)

#Factorial
print("<-----Factorial------->")
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
    print("factorial:",fact)
 
#Count digits in a number  
print("<------count digits in a number------>")
n=1248
count=0
while(n>0):
     temp=n%10
     if temp!=0 and n%temp==0:
         count+=1
     n//=10
print("count of digit:",count)

#Reverse a number
print("<------Reverse a number------>")
n=123
sum=0 
while(n>0): #123>0---->/12>0--->/1>0--1
       temp=n%10 #123%10=3----->/12%10=2---->/1%10=1
       sum=(sum*10)+temp #(0*10)+3=3---->/(3*10)+2=32--->/(32*10)+1=321
       n=n//10 #123//10=12 --->/12//10=1--->/1//10=0
       print(sum)
       
#Sum of digits
print("<------Sum of digits------>")
n=int(input("enter a value:"))
s=0
while n>0:
    s+=n%10
    n//=10
print("sum =",s)

#Check palindrome number
print("<------Check palindrome number------>")
n=int(input("enter a value:"))
if(n%11==0):
    print(n,"is a palindromes")
else:
    print(n,"is not a palindrome")

#Check Armstrong number
print("<------Check Armstrong number------>")
n=int(input("enter a value:"))
m=n
sum=0
while n>0:
    temp=n%10
    sum=sum+temp**3
    n=n//10
if sum==m:
    print("amstrong number")
else:
    print("is not amstrong")
    
#Check prime number
print("<------Check prime number------>")
n=int(input("enter a value:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print(n,"prime number")
else:
    print(n,"not prime number")

#Print all primes from 1 to N
print("<------Print all primes from 1 to N------>")
n = int(input("enter a value: "))
for i in range(2, n+1):
    count = 0
    for j in range(1, i+1):
        if i%j== 0:
            count+=1
    if count == 2:
        print(i,"is a prime number") #30

#GCD/HCF of two numbers
print("<------GCD/HCF of two numbers------>")
a=int(input("enter number: "))
b=int(input("enter number: "))
gcd=1
for i in range(1, min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print("gcd/hcf =",gcd)

#LCM of two numbers
print("<------LCM of two numbers------>")
a=int(input("Enter number: "))
b=int(input("Enter number: "))
lcm=max(a, b)
while lcm%a!=0 or lcm%b!=0:
    lcm+=1
print("lcm=",lcm)

#Fibonacci series
print("<------Fibonacci series------>")
n = int(input("enter number: "))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c

# Power of a number (a^b)
print("<------power of a number (a^b)------>")
n=int(input("Enter n value: "))
m=int(input("Enter m value: "))
s=n**m
print(s)

#Decimal to Binary
print("<------Decimal to Binary------>")
n = int(input("Enter a number: "))
print(bin(n)[2:])
>>>>>>> 34a3ee03fee47b350207f0fc0a71d65f143705d3
