def can_sum(sum_value, array, stored = None):
    if stored is None:
        stored = {} 

    if sum_value == 0:
        return True
    if sum_value < min(array):
        return False
    if not stored.get(sum_value) is None:
        return stored[sum_value]

    for item in array:
        if can_sum(sum_value - item, array, stored) == True:
            stored[sum_value] = True
            return True
    
    stored[sum_value] = False
    return False

print(can_sum(7, [2,3]))
print(can_sum(7, [5,3,4,7]))
print(can_sum(7, [2,4]))
print(can_sum(8, [2,3,5]))
print(can_sum(300, [7,14]))
