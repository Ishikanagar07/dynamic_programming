def howSum(targetSum, numbers, memo = None):
    if memo == None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        ans = howSum(targetSum-num, numbers, memo)
        if ans != None:
            ans = ans + [num]
            memo[targetSum] = ans
            return ans
    memo[targetSum] = None
    return None

print(howSum(7,[2,3]))
print(howSum(7, [5,3,4,7]))
print(howSum(500,[7,8]))

#Time complexity => O(n*m*m)
#Space complexity => O(m*m)
