def canConstruct(target, wordBank):
    table = [False]*(len(target)+1)
    table[0] = True

    for i in range(len(target)+1):
        if table[i] == True:
            for word in wordBank:
                #if the word matches the characters starting at position i
                if target[i:i+len(word)] == word:
                    table[i+len(word)] = True

    return(table[-1])

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))

#Time complexity => O(n*m*m)
#Space complexity => O(m)
