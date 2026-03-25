#Brute Force Approach Tc = O(n^2), Sc = O(1)
def maxSubarray_bruteforce(num):
    max_sum = float('-inf')
    
    for i in range(len(num)):
        sums = 0
        for j in range(i, len(num)):
            sums += num[j]
            max_sum = max(max_sum, sums)
            
    return max_sum

#Optimized Approach Tc = O(n), Sc = O(1)
def maxSubarray(num):
    max_sum = num[0]
    current_sum = num[0]
    
    for i in range(1, len(num)):
        current_sum = max(num[i], current_sum + num[i])
        max_sum = max(current_sum, max_sum)
        
    return max_sum

num = [5,4,-1,7,8]
print(maxSubarray_bruteforce(num))
print(maxSubarray(num))