#area of rectangle
l=56
b=43
area=l*b
print("area of rectangle is",area)
#area of square
s=6
area=s*s
print("area of square is",area)
#area of triangle
base=14
height=10
area=0.5*base*height
print("area of triangle is",area)
#area of circle
pi=3.14
r=9
area=pi*r*r
print("area of circle is",area)
#area of parallelogram
b=12
h=8
area=b*h
print("area of parallelogram is",area)
#area of rhombus
d1=12
d2=8
area=0.5*d1*d2
print("area of rhombus is",area)
#area of trapezium
h=9
p1=6
p2=4
area=0.5*(p1+p2)*h
print("area of trapezium is",area)
#Equilateral Triangle
side=6
area=(3**0.5/4)*side*side
print("area of equilateral triangle is",area)
#Sector of a Circle
angle=45
r=7
area=(angle/360)*pi*r*r
print("area of sector of a circle is",area)
#Semicircle
r=5
area=1/2*(pi*r*r)
print("area of semicircle is",area)
# Perimeter 
# Perimeter of rectangle
l=26
b=12
perimenter=2*(l+b)
print("perimeter of rectangle is",perimenter)
# Perimeter of square
s=8
perimenter=4*s
print("perimeter of square is",perimenter)
# Perimeter of triangle
l=5
b=7
t=10
perimeter=l+b+t
print("perimeter of triangle is",perimeter)
# Perimeter of circle
r=4
perimeter=2*pi*r
print("perimeter of circle is",perimeter)
# Perimeter of parallelogram
l=10
b=6
perimeter=2*(l+b)
print("perimeter of parallelogram is",perimeter)
# Perimeter of rhombus
side=5
perimeter=4*side
print("perimeter of rhombus is",perimeter)
# Perimeter of regular pentagon
side=5
perimeter=5*side
print("perimeter of regular pentagon is",perimeter)
# Perimeter of regular hexagon
side=6  
perimeter=6*side
print("perimeter of regular hexagon is",perimeter)
#Trapezium
side1=5
side2=7     
side3=6
side4=8
perimeter=sum([side1, side2, side3, side4])
print("perimeter of trapezium is",perimeter)
# Perimeter of Equilateral Triangle
side=6
perimeter=3*side
print("perimeter of equilateral triangle is",perimeter)
#cube
s=5
volume=s**3
print("volume of cube is",volume)
#TSA of cube
s=4
tsa=6*s*s
print("TSA of cube is",tsa)
#LSA of cube
s=3
lsa=4*s*s
print("LSA of cube is",lsa)
# Cube of a Number
N=5
cube=N**3
print("cube of a number is",cube)
# Perfect Cube Condition:A number is a perfect cube if its cube root is an integer
n=8
if n**(1/3) % 1 == 0:
    print(n, "is a perfect cube.")
else:
    print(n, "is not a perfect cube.")
# Sum of Cubes of Two Numbers
e=3
f=4
g=e**3
h=f**3
sum_of_cubes=g+h
g+h==(e+f)*(e**2-e*f+f**2)
print("sum of cubes of two numbers is",sum_of_cubes)
#Difference of Cubes of Two Numbers
l=4
m=2
n=l**3
o=m**3
difference_of_cubes=n-o
n-o==(l-m)*(l**2+l*m+m**2)
print("difference of cubes of two numbers is",difference_of_cubes)
#Cubes from 1 to N:1³, 2³, 3³, …, N³
k=5
for i in range(1, k+1):
    print(i**3)
# Cube Root of a Number
n=8
cube_root=n**(1/3)
print("cube root of a number is",cube_root)

# Largest Cube ≤ N
n=40
largest_cube=0
i=1
while i**3<= n:
    largest_cube =i**3
    i+=1
print("largest cube less than or equal to",n,"is",largest_cube)
