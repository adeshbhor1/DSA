# Brute Force Approach Tc = O(n), Sc = O(n) 
def removeElements(nums, val):
    temp = []

    for num in nums:
        if num != val:
            temp.append(num)

    for i in range(len(temp)):
        nums[i] = temp[i]

    return len(temp)

nums = [3,2,2,3]
val = 3

#Optimized Approach Tc = O(n), Sc = O(1)
def removeElement(nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

nums = [0,1,2,2,3,0,4,2]
val = 2
k = removeElement(nums, val)

print(k)
print(nums[:k])