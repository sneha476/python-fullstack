l=[10,20,30,40,50,60]
max1=max(l)
l.remove(max1)
max2=max(l)
l.remove(max2)
max3=max(l)
print("3rd max value: ",max3)

l=[10,20,30,40,50,60]
max1=0
max2=0
max3=0
for i in l:
    if i>max1:
        max3=max2
        max2=max1
        max1=i
    elif i>max2:
        max3=max2
        max2=i
    elif i>max1:
        max3=i
print("3rd max value:",max3)