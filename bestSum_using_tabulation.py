def camSum(target, numbers):
    table = [None]*(target+1)
    table[0] = []

    for i in range(target+1):
        if table[i] != None:
            for num in numbers:
                if i+num <= target:
                    combination = table[i] + [num]
                    if table[i+num] == None or len(combination) < len(table[i+num]):
                        table[i+num] = combination
                                            
    return table[-1]

print(camSum(7, [5,3,4,7]))
print(camSum(8, [2,3,5]))
print(camSum(8, [1,4,5]))
print(camSum(100, [1,2,5,25]))


#TargetSum = m
#Length of array = n
#Time complexity => O(n*m*m)
#Space complexity => O(m*m)
