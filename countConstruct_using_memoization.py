def countConstruct(target, wordBank, memo = None):
    if memo == None:
        memo = dict()

    if target in memo:
        return memo[target]

    if target == "":
        return 1

    totalCount = 0
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            totalCount += countConstruct(suffix, wordBank, memo)
        
    memo[target] = totalCount
    return totalCount

print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))

#Time complexity => O(n*m*m)
#Space complexity => O(m*m)
