def can_sum(target, numbers):
    table = [False]*(target + 1)
    table[0] = True

    for index in range(target):
        if not table[index]:
                continue
        for item in numbers:
            if index + item > target:
                continue
            if index + item == target:
                return True
            table[index + item] = True

    return False



print(can_sum(7, [2,3]))
print(can_sum(7, [5,3,4,7]))
print(can_sum(7, [2,4]))
print(can_sum(8, [2,3,5]))
print(can_sum(300, [7,14]))
