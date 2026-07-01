#leetcode--2574
# nums=[10,4,8,3]
# left=0
# right=0
# total=sum(nums)
# n=len(nums)
# l=[]
# for i in nums:
#     right=total-left-i
#     l.append(abs(left-right))
#     left+=i
# print(l)
nums=[10,4,8,3]
l=[]
for i in range(len(nums)):
    left=sum(nums[:i])
    r=sum(nums[i+1:])
    l.append(abs(left-r))
print(l)

