#Brute Force Approach Tc = O(n^2), Sc = O(1)
def productExceptSelf(nums):
    n = len(nums)
    answer = []

    for i in range(n):
        product = 1

        for j in range(n):
            if i != j:
                product *= nums[j]

        answer.append(product)

    return answer


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))