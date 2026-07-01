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


