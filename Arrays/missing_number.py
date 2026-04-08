#Brute Force Approach Tc = O(n^2), Sc = O(1) 
def missingNumber(nums):
    
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
        
nums = [5,4,3,0,1]

print(missingNumber(nums))

#Optimized Approach Tc = O(n), Sc =O(1)

def missingNumbers(nums):
    
    xor = 0
    
    for i in range(len(nums) + 1):
        xor ^= i
        
    for num in nums:
        xor ^= num
    
    return xor

nums = [3,2,0]
print(missingNumbers(nums))