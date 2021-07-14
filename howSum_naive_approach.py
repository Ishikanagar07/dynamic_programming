def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        ans = howSum(targetSum-num, numbers)
        if ans != None:
            ans = ans + [num]
            return ans
    return None

print(howSum(7,[2,3]))
print(howSum(7, [5,3,4,7]))
