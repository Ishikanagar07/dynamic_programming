#Method 1
def grid_traveller(row, col):
    table = [[0] * (col+1) for _ in range(row+1) ]
    table[1][1] = 1
    for i in range(1, row):
        for j in range(1, col):
            table[i][j + 1] += table[i][j]
            table[i + 1][j] += table[i][j]
    # right-most column
    for i in range(1, row):
        table[i + 1][-1] += table[i][-1]
    # bottom row
    for j in range(1, col):
        table[-1][j + 1] += table[-1][j]
    return table[row][col]

print(grid_traveller(3,3))



#Method 2
def grid_traveller(row, col):
    table = [[0] * (col+1) for _ in range(row+1) ]
    table[1][1] = 1
    for i in range(1, row+1):
        for j in range(1, col+1):
            if j<col:
                table[i][j + 1] += table[i][j]
            if i<row:
                table[i + 1][j] += table[i][j]

    return table[row][col]

print(grid_traveller(3,3))


#Time complexity => O(row*col)
#Space complexity => O(row*col)
