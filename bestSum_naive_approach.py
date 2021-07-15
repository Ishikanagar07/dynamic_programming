def howSum(targetSum, numbers):

    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    minAns = None

    for num in numbers:
        ans = howSum(targetSum-num, numbers)
        if ans != None:
            ans = ans + [num]
            if minAns == None or len(minAns) > len(ans):
                minAns = ans

    return minAns

print(howSum(8,[2,3,5]))
print(howSum(200, [7,14]))
