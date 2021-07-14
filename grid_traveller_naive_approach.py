def gridTraveller(row,col):
    if row==0 or col==0:
        return 0
    if row == 1 and col == 1:
        return 1
    else:
        return gridTraveller(row-1,col) + gridTraveller(row,col-1)

print(gridTraveller(3,3))
