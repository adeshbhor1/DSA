# Brute Force Approach Tc = O(n log n), Sc = O(n) 
def sortedSquare(num):
    temp =[]
    for i in num:
         i = i * i
         temp.append(i)
    temp.sort()
    return temp

num = [-4,-1,0,3,10]

print(sortedSquare(num))


