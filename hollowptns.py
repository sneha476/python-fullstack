#hollow square
print("---square pattern----")
x=5
for i in range(x):
    for j in range(x):
        if (i==0 or j==0 or i==x-1 or j==x-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#hollow rectangle
print("---rectangle ----")
x=5
y=3
for i in range(x):
    for j in range(y):
        if (i==0 or j==0 or i==x-1 or j==y-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#right angled triangle
print("---right angled triangle--")
x=5
for i in range(x):
    for j in range(i+1):
        if(j==0 or i==x-1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#reverese right angled
print("---- reverse right angled triangle")
x=5
for i in range(x-1,-1,-1):
    for j in range(i+1):
        if(j==0 or i==x-1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#Inverted right angled
print("----Inverted right angled---")
g=5
for i in range(g):
    for j in range(g):
        if(i==0 or j==g-1 or j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#pyramidal shape
print("---pyramidal shape---")
n=5
for i in range(n):                                                         
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        if(j==0 or i==n-1 or j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# 1. Square Pattern
print("---Square Pattern---")
x=5
for i in range(x):
    for j in range(x):
            print("*",end=" ")
    print()
# 2. Right Triangle
print("----Right Triangle----")
x=5
for i in range(x):
    for j in range(i+1):
            print("*",end=" ")
    print()
# 3. Number Triangle
print("----Number Triangle---")
r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
# 4. Repeated Number Triangle
print("---Repeated Number Triangle--")
r=5
for i in range(1,r+1):
    for j in range(i):
        print(i, end=" ")
    print()
# 5. Alphabet Triangle
print("---Alphabet Triangle---")
r=5
for i in range(1,r+1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()
# 6. Inverted Star Triangle
print("---Inverted star Triangle----")
x=5
for i in range(i+1):
    for j in range(j):
            print("*",end=" ")
    print()
# 7. Inverted Number Triangle
print("---Inverted Number Triangle----")
x=5
for i in range(x,0,-1):
    for j in range(1,i+1):
            print(j,end=" ")
    print()
# 8. Continuous Number Pattern
print("---continous Number pattern---")
n=5
val=1
for i in range(1,n+1):
    for j in range(i):
        print(val, end=" ")
        val+=1
    print()

# 9. Right-Aligned Star Triangle
print("-----Right-Aligned Star Triangle-----")
n=5
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*"* i)
####
print("-----triangle-----")
n=5
for i in range(n):
    for j in range(i+1):
        if(j==0 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,-1,-1):
    for j in range(i+1):
        if(j==0 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
###
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        if(j==0 or i==n-1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

