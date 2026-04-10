#Brute Force Approach Tc = O(n^2), Sc = O(1)
def majorityElement(num):
    
    
    for i in range(len(num)):
        count = 0
        for j in range(len(num)): 
            if num[i] == num[j]:
                count += 1
        
        if count > len(num) // 2:
            return num[i]
    return "no majority element"

num = [1,2,3,4,0,0]
print(majorityElement(num))

#Optimal Approach Tc = O(n), Sc = O(1)

def majorityElements(nums):
    
    count = 0
    candidate = None
    
    for i in nums:
        if count == 0:
            candidate = i
       
        if i == candidate:
            count += 1
        else:
            count -= 1
        
    if nums.count(candidate) > len(nums) // 2:
            return candidate
        
    return "No majority elements"
 
nums = [1,2,3,4,1,1,1]
 
print(majorityElements(nums))
