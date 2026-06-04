x=int(input("enter the value of x:"))
if x>=0:
    print(x ,"is a positive number")
else:
    print(x,"is a negative number")

char=input("Enter a character: ")

if 'A'<=char<='Z' or 'a'<=char<='z':
    print( char,"Uppercase Letter")
else :
    print(char,"Lowercase Letter")

S1=int(input("Enter the value of S1:"))
S2=int(input("Enter the value of S2:"))
S3=int(input("Enter the value of S3:"))
S4=int(input("Enter the value of S4:"))
S5=int(input("Enter the value of S5:"))
S6=int(input("Enter the value of S6:"))
if S1>=35 and S2>=35 and S3>=35 and S4>=35 and S5>=35 and S6>=35:
    print("pass")
else:
    print("fail")