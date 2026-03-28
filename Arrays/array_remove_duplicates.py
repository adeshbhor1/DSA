#Brute Force Approach Tc = O(n^2), Sc = O(n)
def removeDuplicates(nums):
    unique = []
    
    for num in nums:
        if num not in unique:
            unique.append(num)
    
    for i in range(len(unique)):
        nums[i] = unique[i]
        
    return len(unique)

nums = [1,1,2]
k = removeDuplicates(nums)

print("k:", k)
print("unique elements:", nums[:k])

#Optimized Approach Tc = O(n), Sc = O(1)
def removeDuplicate(nums):
    i = 0
    
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1

nums = [1,1,2]

k = removeDuplicate(nums)

print("count:", k)
print("unique element:", nums[:k])