import sys

# int
a= 10
print(sys.getsizeof(a))   #28

##float
 
b=29.3287264
print(sys.getsizeof(b)) #24

##string

m="sneha Latha"
print(sys.getsizeof(m)) #60

p=" hello python programming"
print(sys.getsizeof(p))##74

##complex

c=6+20j
print(sys.getsizeof(c)) #32

##boolean

bool_g=False
print(sys.getsizeof(bool_g)) #28
t=[10,20,30,40]
i=0
