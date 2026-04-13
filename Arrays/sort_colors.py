#Brute Force Aproach Tc = O(n^2), Sc = O(1)
def sortColors(nums):
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
        
nums = [4,2,5,2,0,0,1]

print(sortColors(nums))

