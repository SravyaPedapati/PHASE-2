#linear search
'''nums=[12,10,6,23,123]
target=123
flag=-1
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag == -1:
    print("not found")
else:
    print("Target found at:",flag)'''

#Binary search
nums=[12,10,6,23,123]
target=12
nums=sorted(nums)
left=0
right=len(nums)-1
flag=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        flag=mid
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1

if flag == -1:
    print("Target not found")
else:
    print("Target found at index:",flag)
