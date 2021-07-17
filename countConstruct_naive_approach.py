def countConstruct(target, wordBank):
    if target == "":
        return 1

    totalCount = 0
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            totalCount += countConstruct(suffix, wordBank)
    return totalCount

print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))


#Time complexity => O((n^m)*m)
#Space complexity => O(m*m)
