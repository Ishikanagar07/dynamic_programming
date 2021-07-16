def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        if canSum(targetSum-num, numbers) == True:
            return True
    return False

print(canSum(7, [2,3]))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
#print(camSum(300, [7,14]))


# m => targetSum
# n => length of numbers array
#Time complexity => O(n^m)
#Space complexity => O(m)
