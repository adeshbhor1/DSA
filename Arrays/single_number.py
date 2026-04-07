#Brute Force Approach Tc = O(n^2), Sc = O(1) 
def singleNumber(nums):
    
    for i in range(len(nums)):
        count = 0
        
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        
        if count == 1:
            return nums[i]

nums = [2,2,1,3,1]
print(singleNumber(nums))

#Optimized Approach Tc = O(n), Sc =O(1)
def singleNumbers(nums):
    
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [1,1,3,3,4]
print(singleNumbers(nums))