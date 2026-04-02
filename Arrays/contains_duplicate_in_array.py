# Brute Force Approach Tc = O(n^2), Sc = O(1)
def containsDuplicate(nums) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1,2,3,4,1]

print(containsDuplicate(nums))

#Optimized Approach Tc = O(n), Sc = O(n)
def containsDuplicates(nums):
    seen = set()
    
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False

nums = [1,2,3,4]

print(containsDuplicates(nums))