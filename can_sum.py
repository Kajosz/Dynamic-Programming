def can_sum(sum_value, array, stored = {}):
    if sum_value == 0:
        return True
    if sum_value < min(array):
        return False
    if not stored.get(sum_value) is None:
        return stored[sum_value]

    results = []
    for item in array:
        results.append(can_sum(sum_value - item, array, stored))
    
    stored[sum_value] = True in results
    return stored[sum_value]

print(can_sum(7, [2,3,4]))