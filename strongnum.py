# n=int(input("enter value: "))
# fact=1
# sum=0
# for i in range(1,n+1):
#         fact*=i
#         sum+=fact
#         print("fact of number",fact)
# print(sum)
# #armstrong number
# num=int(input("enter a number: "))
# order=len(str(num))

# sum=0
# temp=num
# while temp>0:               # checktemp>0
#     digit=temp%10           #  digit=temp%10=last digit
#     sum+=digit**order       
#     temp//=10               
# if num==sum:
#     print(num,"is an Armstrong number")
# else:
#     print(num,"is not an Armstrong number")

n=int(input("enter a value:"))
power=n**2
sum=0
while(power>0):
     temp=power%10
     sum+=temp
     power//=10
print(sum)
          
#           print()
     








# find length of the number
# separate each number
# power each number with length-->1pow3+5pow3+9pow3
# step


# auto marphic number
# any value pow 2-->
# n=25
# 25pow 2=625
# 5->25->125