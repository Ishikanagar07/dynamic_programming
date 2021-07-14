memo = {"1,1": 1}
def gridTraveller(m,n):
    global memo
    if m==0 or n==0:
        return 0
    cell = f"{m},{n}"
    if cell in memo:
        return memo[cell]
    cell = f"{n},{m}"
    if cell in memo:
        return memo[cell]
    memo[cell] = gridTraveller(m-1,n) + gridTraveller(m,n-1)
    return memo[cell]
