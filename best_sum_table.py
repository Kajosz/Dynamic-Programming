def best_sum(target, numbers):
    table = [None]*(target + 1)
    table[0] = []

    for index in range(target):
        if  table[index] is None:
                continue

        for item in numbers:
            if index + item > target:
                continue

            if table[index + item] is None:
                table[index + item] = table[index] + [item]
                continue

            if len(table[index] + [item]) < len(table[index + item]):
                table[index + item] = table[index] + [item]

    return table[target]


print(best_sum(7, [2,3]))
print(best_sum(7, [5,3,4,7]))
print(best_sum(7, [2,4]))
print(best_sum(8, [2,3,5]))
print(best_sum(300, [7,14]))
print(best_sum(100, [5, 2, 25, 10]))
