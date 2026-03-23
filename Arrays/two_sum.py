# Brute Force Approach O(n^2)
def two_sum_bruteforce(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]
    return []


# Optimized Approach O(n)
def two_sum_optimized(num, target):
    seen = {}  

    for i in range(len(num)):
        remaining = target - num[i]

        if remaining in seen:
            return [seen[remaining], i]

        seen[num[i]] = i   

    return []


num = [2, 4, 7, 8, 1]
target = 10

print(two_sum_bruteforce(num, target))
print(two_sum_optimized(num, target))