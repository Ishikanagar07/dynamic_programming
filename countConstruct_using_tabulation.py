def countConstruct(target, wordBank):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(target)+1):
        if table[i] != 0:
            for word in wordBank:
                #if the word matches the characters starting at position i
                if target[i:i+len(word)] == word:
                    table[i+len(word)] += table[i]

    return(table[-1])

print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))

#Time complexity => O(n*m*m)
#Space complexity => O(m)
