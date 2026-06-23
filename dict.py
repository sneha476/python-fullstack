# #built in methods
d={}
d.update({"A":1})  #adding values(inthe form item)
d.update({"A":2}) #update value if key exist
d.setdefault("B",3)#add 1 peram is key 2 parem is values
d.update({"B":4})
print(d)

d={"A":1}
l=[1,2,3,4]
y=d.fromkeys(l,0)
print(y)


l=[1,2,3,1,2,3,1,2,3,5]
d={}
for val in l:
     d[val]=d.get(val,0)+1 
     print(d) # d[val] is used to regitered
# get is used to get the value
d={1:0,2:0}
print(d)
print(d.get(1,0)+1)
print(d)

print(d)
d[1]=d.get(1,0)+1
print(d)
# always values are return  not keys because keys are immutable
l=[1,2,3,1,2,3,1,2,3,5]
d={}
for key in l:
    # print(key,"-->",d.get(key,0)+1)
    d[key]=d.get(key,0)+1 
print(d)
# if keys are not exist then register
#if keys are exist then add


#tuple 
l=(1,2,3,1,2,3,1,2,3,5)
t={}
for key in l:
    t[key]=t.get(key,0)+1
l1=tuple(t.items())
print(l1)

# finding a unique value

arr=[1,2,3,1,2,1,2,1]
freq={}
for n in arr:
    freq[n]=freq.get(n,0)+1
    counts=list(freq.values())
    for i in range(1,len(arr)):
            if(arr.count(arr[i])>1):
               print("False")
    print("True")





