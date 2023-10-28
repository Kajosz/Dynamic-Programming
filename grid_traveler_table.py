def create_matrix(rows, columns, placeholder = 0):
  table = []
  for r in range(rows):
    new_row = []
    for c in range(columns):
        new_row.append(placeholder)
    table.append(new_row)
  return table

def grid_traveler(rows, columns):
    max_row = rows + 1
    max_col = columns + 1
    table = create_matrix(max_row, max_col)
    table[1][1] = 1

    for r in range(max_row):
        if r == 0:
            continue
        for c in range(max_col):
            if c == 0:
                continue
            if c < columns:
                table[r][c + 1] += table[r][c]
            if r < rows:
                table[r + 1][c] += table[r][c]
        
    return table[rows][columns]


print(grid_traveler(1,1))
print(grid_traveler(2,3))
print(grid_traveler(3,2))
print(grid_traveler(3,3))
print(grid_traveler(18,18))



