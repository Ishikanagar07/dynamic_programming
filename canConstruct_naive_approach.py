def canConstruct(target, wordBank):
    if target == "":
        return True
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(target[suffix, wordBank) == True:
                return True
    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))

#Time complexity => O((n^m)*m)
#Space complexity => O(m*m) => O(m^2)

