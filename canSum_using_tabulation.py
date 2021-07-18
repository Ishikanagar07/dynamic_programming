def camSum(target, numbers):
    table = [False]*(target+1)
    table[0] = True
    for i in range(target+1):
        if table[i] == True:
            for num in numbers:
                if i+num <= target:
                    table[i+num] = True
    return table[-1]
print(camSum(7, [5,3,4]))

#TargetSum = m
#Length of array = n
#Time complexity => O(m*n)
#Space complexity => O(m)
