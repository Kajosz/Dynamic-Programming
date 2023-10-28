def best_sum(target, numbers, stored = None):
    print(stored)
    if stored is None:
        stored = {}
    if target == 0:
        return []
    if target < 0:
        return None

    if not stored.get(target) is None:
        return stored[target]
    
    best_result = None
    best_length = 42000006969
    result = []
    for item in numbers:
        diff = target - item
        result = best_sum(diff, numbers, stored)

        if result is None:
            continue

        result += [item]
        new_length = len(result)

        if new_length < best_length:
            best_length = new_length
            best_result = result

    if sum(best_result) == target:
        print(target)
        stored[target] = best_result     
  
    return best_result
            
# print(best_sum(8,[2,3,5]))
# print(best_sum(300, [14,7]))
# print(best_sum(2,[3,6,7]))
print(best_sum(8,[1,4,5]))
