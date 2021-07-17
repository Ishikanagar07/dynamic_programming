def canConstruct(target, wordBank, memo=None):
    if memo == None:
        memo = dict()

    if target in memo:
        return memo[target]

    if target == "":
        return True
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True
              
    memo[target] = False
    return False
  
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))
  
  
  #Time complexity => O(n*m*m)
  #Space complexity => O(m*m) => O(m^2)
