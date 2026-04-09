#Brute Force Approach Tc = O(n*k), Sc = O(1) 
def rotateArray(nums, k):
    
    n = len(nums)
    k = k % n
    
    for _ in range(k):
        last = nums[-1]
        for i in range(n -1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last
    return nums
            
nums = [5,4,3,0,1]
k = 3

print(rotateArray(nums, k))

#Optimized Approach Tc = O(n), Sc =O(1)

def rotateArrays(num, m):
    
    s = len(num)
    m = m % s
    
    def reverse(num, start, end):
        while start < end:
            num[start], num[end] = num[end], num[start]
            start += 1
            end -= 1
        
    reverse(num, 0, s - 1)
    
    reverse(num, 0, m - 1)
    
    reverse(num, m, s - 1)
    
    return num

num = [4,1,5,7,8]
m = 2

print(rotateArrays(num, m))

