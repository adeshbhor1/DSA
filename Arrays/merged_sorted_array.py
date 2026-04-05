#Brute Force Approach Tc = O((m + n) log(m + n)), Sc = O(m + n)
def merge(nums1, m, nums2, n):
    temp = []

    for i in range(m):
        temp.append(nums1[i])

    for j in range(n):
        temp.append(nums2[j])

    temp.sort()

    for i in range(m + n):
        nums1[i] = temp[i]
    
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))

# Optimized Approach Tc =O(m+n) , Sc = O(1)
def mergeSortedArray(num1, m, num2, n):
    
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while i >= 0 and j >= 0:
        if num1[i] > num2[j]:
            num1[k] = num1[i]
            i -= 1
        else:
            num1[k] = num2[j]
            j -= 1
        k -= 1
        
    while j >= 0:
        num1[k] = num2[j]
        j -= 1
        k -= 1
    return num1

num1 = [1,2,3,0,0,0]
m = 3

num2 = [2,5,6]
n = 3

print(mergeSortedArray(num1, m, num2, n))