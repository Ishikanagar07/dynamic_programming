def camSum(target, numbers):
    table = [None]*(target+1)
    table[0] = []
    for i in range(target+1):
        if table[i] != None:
            for num in numbers:
                if i+num <= target:
                    table[i+num] = table[i] + [num]
    return table[-1]

print(camSum(7, [5,3,4]))

#TargetSum = m
#Length of array = n
#Time complexity => O(n*m*m)
#Space complexity => O(m*m)
