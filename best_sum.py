def best_sum(target, numbers, stored = None):
    if stored is None:
        stored = {}
    if target == 0:
        return []
    if target < 0:
        return None

    if not stored.get(target) is None:
        return stored[target]
    
    best_result = None
    result = []
    for item in numbers:
        diff = target - item
        result = best_sum(diff, numbers, stored)

        if result is None:
            continue

        result += [item]
        new_length = len(result)

        if best_result is None:
            best_length = new_length
            best_result = result
            continue

        if new_length < best_length:
            best_length = new_length
            best_result = result

    if best_result is None:
        stored[target] = []
        return None
    
    stored[target] = list(best_result)
    if sum(best_result) == target:     
        return best_result
            
print(best_sum(8,[2,3,5]))
print(best_sum(300, [14,7]))
print(best_sum(2,[3,6,7]))
print(best_sum(8,[1,4,5]))
