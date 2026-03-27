#Brute Force Approach Tc = O(n), Sc = O(n)
def moveZeroes(num):
     temp = []
     
     for i in num:
        if i != 0:
            temp.append(i)
    
     while len(temp) < len(num):
        temp.append(0)
    
     return temp
 
num = [0,1,0,3,12]
print(moveZeroes(num))
 
#Optimized Approach Tc = O(n), Sc = O(1)
def moveZero(nums):
    j = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

nums = [0,1,0,3,12]
moveZero(nums)
print(nums)