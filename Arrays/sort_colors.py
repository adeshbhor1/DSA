#Brute Force Aproach Tc = O(n^2), Sc = O(1)
def sortColors(num):
    
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
    return num
        
num = [4,2,5,2,0,0,1]

print(sortColors(num))

# Optimized Approach Tc = O(n), Sc = O(1)
def sortColor(nums):
    n = len(nums)
    index = 0

    for i in range(n):
        if nums[i] == 0:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1

    for i in range(index, n):
        if nums[i] == 1:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
    
    return nums

nums = [2,0,2,1,1,0]
print(sortColor(nums))