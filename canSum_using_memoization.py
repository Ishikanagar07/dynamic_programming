def canSum(targetSum, numbers, memo = None):
    if memo == None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(7, [2,3]))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7,14]))


#Time complexity => O(m*n)
#Space complexity => O(m)

# https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/  
# above link provies the explanation for initializing memo as NONE when passed as argument


