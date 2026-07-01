# to find the unique element in a list
# l=[1,2,3,2,1]
# for i in range(len(l))
#     count=0
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             count+=1
# print(l.count(1))
# or
# if len(l)>1:
#     for i in range(len(l)):
#         count=0
#         for j in range(len(l)):
#             if l[i]==l[j]:
#                 count+=1
#         if count==1:
#             print(l[i])
# or
# for i in len(l):
#     if l.count(l[i])==1:
#         print(l[i])
# or
# for i in l:
#     if l.count(i)==1:
#         print(i)
# bitwise method
# l=[2,3,2,1,1]
# xor=l[0]
# for i in range(1, len(l)):
#     xor=xor^l[i]
# print(xor)
# i=0
# xor=0
# while i<len(l):
#     xor=xor^l[i]
#     i+=1
# print(xor)
# perfect number:
# n=28
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("perfect number")
# else:
#     print("not a perfect number")
    
# i=1
# sum=0
# for i in range(1,5000):
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             sum+=j
#     if sum==i:
#         print(i)

