List ([]):
A list is an ordered, mutable collection.
Example:
fruits = ["apple", "banana", "mango"]
Properties:
✅ Ordered
✅ Mutable
✅ Allows duplicates
Common methods:
append()
insert()
remove()
pop()
sort()
reverse()

append() → Adds element at end:
nums = [10, 20, 30]
nums.append(40)
print(nums)   # [10, 20, 30, 40]
insert() → Adds at specific index:
nums.insert(1, 15)
print(nums)   # [10, 15, 20, 30, 40]
remove() → Removes first matching value:
nums.remove(20)
print(nums)   # [10, 15, 30, 40]
pop() → Removes by index:
nums.pop()
print(nums)   # [10, 15, 30]
sort() → Sorts ascending:
nums.sort()
print(nums)    #[10, 20, 30]
reverse() → Reverses list:
nums.reverse()  #[30, 20, 10]
print(nums)
index() → Finds position:
nums = [10, 20, 30]
print(nums.index(20))  #1
count() → Counts occurrences:
nums = [10, 20, 20, 30]
print(nums.count(20))   # 2
extend() → Adds multiple elements:
nums = [10, 20]
nums.extend([30, 40])
print(nums)   # [10, 20, 30, 40]
clear() → Removes all elements:
nums = [10, 20, 30]
nums.clear()
print(nums)   # []
copy() → Creates a copy:
nums = [10, 20, 30]
new_nums = nums.copy()
print(new_nums)   # [10, 20, 30]
Set:
A set is an unordered collection of unique elements.
It does not allow duplicate values.
nums = {10, 20, 30}
print(nums) #{10, 20, 30}
Properties of Set:
✅ Unordered → Elements have no fixed position
nums = {10, 20, 30}
# Cannot access like nums[0]
Mutable → Can add or remove elements
nums.add(40)
print(nums)
Output:
{10, 20, 30, 40}
✅ No duplicates allowed
nums = {10, 20, 20, 30}
print(nums)
Output:
{10, 20, 30}
✅ Fast searching
nums = {10, 20, 30}
print(20 in nums)
Output:
True
Set Methods
add() → Adds an element
nums = {10, 20, 30}
nums.add(40)
print(nums)
Output:
{10, 20, 30, 40}
remove() → Removes element:
nums = {10, 20, 30}
nums.remove(20)
print(nums)
Output:
{10, 30}
discard() → Removes safely:
nums = {10, 20, 30}
nums.discard(20)
print(nums)
Output:
{10, 30}
pop() → Removes random element
nums = {10, 20, 30}
nums.pop()
print(nums)
Output:
{20, 30}
clear() → Removes all elements
nums = {10, 20, 30}
nums.clear()
print(nums)
Output:
set()
copy() → Creates a copy
nums = {10, 20, 30}
new_nums = nums.copy()
print(new_nums)
Output:
{10, 20, 30}
union() → Combines sets
a = {10, 20}
b = {20, 30}
print(a.union(b))
Output:
{10, 20, 30}
intersection() → Common elements
a = {10, 20}
b = {20, 30}
print(a.intersection(b))
Output:
{20}
difference() → Unique elements
a = {10, 20}
b = {20, 30}
print(a.difference(b))
Output:
{10}
symmetric_difference() → Non-common elements
a = {10, 20}
b = {20, 30}
print(a.symmetric_difference(b))
Output:
{10, 30}
update() → Adds all elements from another set
a = {10, 20}
b = {30, 40}
a.update(b)
print(a)
Output:
{10, 20, 30, 40}
issubset() → Checks if set is inside another set
a = {10, 20}
b = {10, 20, 30}
print(a.issubset(b))
Output:
True
issuperset() → Checks if set contains another set
a = {10, 20, 30}
b = {10, 20}
print(a.issuperset(b))
Output:
True
isdisjoint() → Checks no common elements
a = {10, 20}
b = {30, 40}
print(a.isdisjoint(b))
Output:
True
Tuple:
A tuple is an ordered and immutable collection of elements.
It allows duplicate values.

Example:
nums = (10, 20, 30)
print(nums)

Output:

(10, 20, 30)
Properties of Tuple

✅ Ordered → Elements maintain their order

nums = (10, 20, 30)
print(nums[0])

Output:

10

✅ Immutable → Cannot change values

nums = (10, 20, 30)
# nums[0] = 100   ❌ Error

✅ Allows duplicates

nums = (10, 20, 20, 30)
print(nums)

Output:

(10, 20, 20, 30)

✅ Can store different data types

data = (10, "Python", 3.5, True)
print(data)

Output:
(10, 'Python', 3.5, True)
Tuple Methods

Tuple has only 2 built-in methods
count() → Counts occurrences of an element
nums = (10, 20, 20, 30)
print(nums.count(20))
Output:
2
index() → Finds the position of an element
nums = (10, 20, 30)
print(nums.index(20))
Output:
1
Other Operations on Tuple
len() → Finds length
nums = (10, 20, 30)
print(len(nums))
Output:
3
max() → Finds largest value
nums = (10, 20, 30)
print(max(nums))
Output:
30
min() → Finds smallest value
nums = (10, 20, 30)
print(min(nums))
Output:
10
sum() → Adds all values
nums = (10, 20, 30)
print(sum(nums))
Output:
60
Slicing
nums = (10, 20, 30, 40)
print(nums[1:3])
Output:
(20, 30)
Concatenation
a = (1, 2)
b = (3, 4)
print(a + b)
Output:
(1, 2, 3, 4)
Repetition
nums = (1, 2)
print(nums * 3)
Output:
(1, 2, 1, 2, 1, 2)
Dictionary:
A dictionary is a collection of data stored in key-value pairs.
Each key must be unique.

Example:
student = {
    "name": "John",
    "age": 20,
    "city": "New York"
}
print(student)

Output:

{'name': 'John', 'age': 20, 'city': 'New York'}
Properties of Dictionary

✅ Ordered (Python 3.7+) → Maintains insertion order

student = {"name": "John", "age": 20}
print(student)

Output:

{'name': 'John', 'age': 20}

✅ Mutable → Can change values

student["age"] = 21
print(student)

Output:

{'name': 'John', 'age': 21}

✅ Unique Keys

student = {"name": "John", "name": "Mike"}
print(student)

Output:

{'name': 'Mike'}

✅ Different data types allowed

data = {
    "name": "Python",
    "version": 3.12,
    "active": True
}
print(data)

Output:

{'name': 'Python', 'version': 3.12, 'active': True}
Dictionary Methods
student = {"name": "John", "age": 20}
keys() → Returns all keys
print(student.keys())

Output:

dict_keys(['name', 'age'])
values() → Returns all values
print(student.values())

Output:

dict_values(['John', 20])
items() → Returns key-value pairs
print(student.items())

Output:

dict_items([('name', 'John'), ('age', 20)])
get() → Gets value by key
print(student.get("name"))

Output:

John
update() → Updates or adds new values
student.update({"age": 21})
print(student)

Output:

{'name': 'John', 'age': 21}
pop() → Removes a specific key
student.pop("age")
print(student)

Output:

{'name': 'John'}
popitem() → Removes last inserted item
student = {"name": "John", "age": 20}
student.popitem()
print(student)

Output:

{'name': 'John'}
clear() → Removes all items
student.clear()
print(student)

Output:

{}
copy() → Creates a copy
student = {"name": "John", "age": 20}
new_student = student.copy()
print(new_student)

Output:

{'name': 'John', 'age': 20}
fromkeys() → Creates dictionary from keys
keys = ("a", "b", "c")
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)

Output:

{'a': 0, 'b': 0, 'c': 0}
setdefault() → Gets value, inserts if key not found
student = {"name": "John"}
student.setdefault("age", 20)
print(student)

Output:

{'name': 'John', 'age': 20}
Accessing Dictionary Values
By key
student = {"name": "John", "age": 20}
print(student["name"])
Output:
John
Looping through Dictionary
for key, value in student.items():
    print(key, value)
Output:
name John
age 20
Nested Loop:
A nested loop means a loop inside another loop.
The inner loop runs completely for each iteration of the outer loop.

Syntax:
for i in range(3):
    for j in range(2):
        print(i, j)

Output:

0 0
0 1
1 0
1 1
2 0
2 1

Explanation:

Outer loop runs 3 times
Inner loop runs 2 times for each outer loop

Total = 3 × 2 = 6 times

Examples of Nested Loop
1. Print numbers
for i in range(1,4):
    for j in range(1,4):
        print(i, j)

Output:

1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3

2. Multiplication table
for i in range(1,4):
    for j in range(1,6):
        print(i * j, end=" ")
    print()

Output:

1 2 3 4 5
2 4 6 8 10
3 6 9 12 15

3. Pattern printing
Square pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

Output:

* * *
* * *
* * *
Triangle pattern
for i in range(1,4):
    for j in range(i):
        print("*", end=" ")
    print()

Output:

*
* *
* * *
4. Nested loop with list
matrix = [[1,2],[3,4],[5,6]]

for row in matrix:
    for item in row:
        print(item)

Output:

1
2
3
4
5
6
