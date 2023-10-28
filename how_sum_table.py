def how_sum(target, numbers):
    table = [None]*(target + 1)
    table[0] = []

    for index in range(target):
        if  table[index] is None:
                continue
        for item in numbers:
            if index + item > target:
                continue
            if index + item == target:
                return table[index] + [item]
            table[index + item] = table[index] + [item]

    return None



print(how_sum(7, [2,3]))
print(how_sum(7, [5,3,4,7]))
print(how_sum(7, [2,4]))
print(how_sum(8, [2,3,5]))
print(how_sum(300, [7,14]))
