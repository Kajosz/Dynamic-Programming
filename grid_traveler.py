def grid_traveler(rows, colums, stored = {}):
    if rows <= 0 or colums <= 0:
        return 0
    if rows == 1 or colums == 1:
        return 1
    
    key = str(rows) + 'x' + str(colums)
    if not stored.get(key) is None:
        return stored[key]

    stored[key] = grid_traveler(rows, colums - 1, stored) + grid_traveler(rows - 1, colums, stored)
    return stored[key]


print(grid_traveler(2, 3))
print(grid_traveler(2, 2))
print(grid_traveler(4, 3))
print('****')
print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))




