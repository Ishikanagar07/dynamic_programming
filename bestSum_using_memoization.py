def howSum(targetSum, numbers, memo=None):

    if(memo == None):
        memo = dict()
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    minAns = None

    for num in numbers:
        ans = howSum(targetSum-num, numbers, memo)
        if ans != None:
            ans = ans + [num]
            if minAns == None or len(minAns) > len(ans):
                minAns = ans
            
    memo[targetSum] = minAns
    return minAns

print(howSum(8,[2,3,5]))
print(howSum(300, [1,2,5,25]))
