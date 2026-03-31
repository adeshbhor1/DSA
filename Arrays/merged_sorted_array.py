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