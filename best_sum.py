def shortest_sum(sums):
    if len(sums) == 0:
        return None
    shortest = 213742069
    best = []
    for proposition in sums:
        if proposition is None:
            continue
        length = len(proposition)
        if length == 1:
            return proposition
        if length < shortest:
            shortest = length
            best = proposition
    if len(best) > 0:
        return best
    return None

def best_sum(target, numbers, so_far = None, stored = None):
    if so_far is None:
        so_far = []
    if stored is None:
        stored = {}

    if not stored.get(target) is None:
        return stored[target]
    
    if target < 0:
        return None
    
    if target == 0:
        return so_far

    sums = []
    for item in numbers:
        sums.append(best_sum(target - item, numbers, so_far + [item], stored))

    stored[target] = shortest_sum(sums)
    return stored[target]


            
            
print(best_sum(8,[2,3,5]))
print(best_sum(300, [14,7]))
print(best_sum(2,[3,6,7]))
