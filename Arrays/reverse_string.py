#Brute Force Approach Tc = O(n), Sc = O(n)
def reverseString(s):
    temp = []

    for i in range(len(s) - 1, -1, -1):
        temp.append(s[i])

    for i in range(len(s)):
        s[i] = temp[i]
        
    return s
 
s = ["o","l","l","e","h"]
print(reverseString(s))

#Optimized Approach Tc = O(n), Sc = O(1)
def reverseString(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        
    return s

s = ["H","a","n","n","a","h"]
print(reverseString(s))