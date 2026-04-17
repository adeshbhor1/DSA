# Brute Force Approach Tc = , Sc = 
def thirdMaximumNumber(num):
    
    temp = []
    
    for k in num:
        if k not in temp:
            temp.append(k)
            
    for i in range(len(temp)):
        for j in  range(i + 1, len(temp)):
            if temp[i] < temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
    
    if len(temp) >= 3:
        return temp[2]
    else:
        return temp[0]
    
print(thirdMaximumNumber([3,2,1]))      
print(thirdMaximumNumber([1,2]))        
print(thirdMaximumNumber([2,2,3,1])) 