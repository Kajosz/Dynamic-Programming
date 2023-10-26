def how_sum(target_sum, numbers, so_far = None, stored = None):
    if stored is None:
        stored = {}
    if so_far is None:
        so_far = []

    if not stored.get(target_sum) is None:
        return None

    if target_sum < 0:
        return None


    for item in numbers:

        if target_sum - item == 0:
            return so_far + [item]

        trying = how_sum(target_sum - item, numbers, so_far + [item], stored)
        if not trying is None:
            return trying

    stored[target_sum] = False
    return None

#print(how_sum(6, [2,3,5]))
# print(how_sum(6, [5,4,2]))
print(how_sum(7, [2,3]))
print(how_sum(7, [5,3,4,7]))
print(how_sum(7, [2,4]))
print(how_sum(8, [2,3,5]))
print(how_sum(300, [7,14]))



