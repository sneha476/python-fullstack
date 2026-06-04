l=[10,20,30,40]
l.append(50)
print(l)
l3=(1,2,3)
l.append(l3)
print(l)
l2=(6,7)
l.extend(l2)
print(l)
l.insert(9,"hello")
print(l)
print(l.pop(4))
print(l.remove(40))
print(l.remove(10))
l=[10,10,20,30,60,20]
print(l.count(10))
l2=l.copy
print(l)
l.clear()
# print(l)

l=[10,20,30,40,50,60]
max=0
for i in l:
    if i>max:
        max=i
print(max)
min=l[0]
for i in range(len(l)):
    if l[i]<min:
        min=l[i]
print(min)
sum=0
for i in l:
    sum+=i
    print(sum)

product=1
for i in l:
    product*=i
print(product)

l=[10,20,30,40,50,60,70,80,90]
print(l[0:5:1])                  #initial index=0,end index=5-1,step=1
print(l[:6:2])                   # by default initial index=0,end index=6-1,step=2
print(l[2::2])                   #initial index=2,by default end index =length of list-1,step=2
print(l[::3])                    #by default initial index=0, by default end index =length of list-1,step=3
print(l[1:8:3])                  #initial index=1,end index=8-1,step=3
print(l[-1:-5:-2])              #initial index=-1,end index=-5-1=-6,step=-2
print(l[3::-1])                  #initial index=3,by default end index =length of list-1,step=-1
print(l[-1::-2])              #initial index=-1,by default end index =length of list-1,step=-2
print(l[3::-1])                 #initial index=3,by default end index =length of list-1,step=-1
print(l[:-1:])                    #by default initial index=0, end index=-1, step=1