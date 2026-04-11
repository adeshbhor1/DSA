#BruteForce Approach Tc = O(n), Sc = O(1)
def findPeakElement(num):
    
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return i
    return len(num) - 1

num = [1,2,3,1]

print(findPeakElement(num))

#Optimal Approach Tc = O(log n), Sc = O(1)

def findPeakElements(nums):
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

nums = [3,2,1,4,3]
print(findPeakElements(nums))
        