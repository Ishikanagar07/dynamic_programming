#method 1
def fib(n):
    table = [0]*(n+1)
    table[1] = 1
    for i in range(n):
        table[i+1] += table[i]
        if i==n-1:    #to handle last element
            break
        table[i+2] += table[i]
    return table[n]
  
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))



#method 2
def fib(n):
    table = [0]*(n+1)
    table[1] = 1
    for i in range(n-1):
        table[i+1] += table[i]
        table[i+2] += table[i]
    table[-1] += table[-2]
    return table[-1]
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
