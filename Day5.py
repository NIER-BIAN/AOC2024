#=========================================================
# Pt1

all_rules = []
all_updates =[]

with open('input.txt', 'r') as file:
    
    for line in file:

        # Strip all lines and skip empty lines
        line = line.strip()
        if not line:
            continue

        # Gather rules
        if '|' in line:
            all_rules.append([int(i) for i in line.split('|')])
            continue

        # Gather updates
        all_updates.append([int(i) for i in line.split(',')])


def check_one_update_against_all_rules(array, rules):

    # Create indices dict for [75, 47, 61, 53, 29]
    # i.e. {75: 0, 47: 1, 61: 2, 53: 3, 29: 4}
    indices_dict = {num: array.index(num) for num in array}
    
    for a, b in rules:

        # irrelevant rule
        if (a not in indices_dict) or (b not in indices_dict):
            continue

        # broken rule
        if indices_dict[a] > indices_dict[b]:
            return 0
        
    return array[(len(array)-1)//2]

ans = 0
for update in all_updates:
    ans += (check_one_update_against_all_rules(update, all_rules))

print(ans)

#=========================================================
# Pt2 Assuming no cycles

all_rules = []
all_updates =[]

with open('input.txt', 'r') as file:
    
    for line in file:

        # Strip all lines and skip empty lines
        line = line.strip()
        if not line:
            continue

        # Gather rules
        if '|' in line:
            all_rules.append([int(i) for i in line.split('|')])
            continue

        # Gather updates
        all_updates.append([int(i) for i in line.split(',')])


def find_disordered_updates(array, rules):

    # Create indices dict for [75, 47, 61, 53, 29]
    # i.e. {75: 0, 47: 1, 61: 2, 53: 3, 29: 4}
    indices_dict = {num: array.index(num) for num in array}
    
    for a, b in rules:

        # irrelevant rule
        if (a not in indices_dict) or (b not in indices_dict):
            continue

        # broken rule
        if indices_dict[a] > indices_dict[b]:
            return array


disordered_updates = [result for result in (find_disordered_updates(update, all_rules) for update in all_updates) if result is not None]

# [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]

# Create a directed graph
graph = nx.DiGraph()

for rule in all_rules:
    graph.add_edge(rule[0], rule[1])

# Perform topological sort
ordered_numbers = list(nx.topological_sort(graph))
# [97, 75, 47, 61, 53, 29, 13]

ordered_numbers_indices_dict = {num: ordered_numbers.index(num) for num in ordered_numbers}
# {97: 0, 75: 1, 47: 2, 61: 3, 53: 4, 29: 5, 13: 6}

# Order the updates based on ordered_numbers_indices_dict
ans = 0
for update in disordered_updates:
    fixed_update = sorted(update, key=lambda x: ordered_numbers_indices_dict[x])
    ans += fixed_update[(len(fixed_update)-1)//2]
print(ans)


#=========================================================
# Pt2 Bubble sort (as there are cycles in all_rules)

import itertools


all_rules = []
all_updates =[]

with open('input.txt', 'r') as file:
    
    for line in file:

        # Strip all lines and skip empty lines
        line = line.strip()
        if not line:
            continue

        # Gather rules
        if '|' in line:
            all_rules.append([int(i) for i in line.split('|')])
            continue

        # Gather updates
        all_updates.append([int(i) for i in line.split(',')])


def find_disordered_updates(array, rules):

    # Create indices dict for [75, 47, 61, 53, 29]
    # i.e. {75: 0, 47: 1, 61: 2, 53: 3, 29: 4}
    indices_dict = {num: array.index(num) for num in array}
    
    for a, b in rules:

        # irrelevant rule
        if (a not in indices_dict) or (b not in indices_dict):
            continue

        # broken rule
        if indices_dict[a] > indices_dict[b]:
            return array


disordered_updates = [
    result for result in (find_disordered_updates(update, all_rules) for update in all_updates) if result is not None
]

# [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]

def bubble_sort_constrained(arrays, constraints):

    # setdefault(a, []): if key "a" exists, append(b)
    # if it doesn't exist, creates new key "a" with [] as value, and append(b)
    # if all_rules = [(1, 2), (1, 3), (2, 4)]
    # constraint_dict = {1: [2, 3], 2: [4]}. i.e. 1 before 2 and 3; 2 before 4.
    constraint_dict = {}
    for a, b in constraints:
        constraint_dict.setdefault(a, []).append(b)

    for array in arrays:
        n = len(array)
        for i in range(n-1):
            for j in range(n-i-1):

                # Cont: pair correctly orderd as array[j+1] is in constraint_dict[array[j]]
                if array[j] in constraint_dict and array[j+1] in constraint_dict[array[j]]:
                    continue

                # Swap: pair wrongly orderd as array[j] is in constraint_dict[array[j+1]]
                elif array[j+1] in constraint_dict and array[j] in constraint_dict[array[j+1]]:
                    array[j], array[j+1] = array[j+1], array[j]

    return arrays

sorted_arrays = bubble_sort_constrained(disordered_updates, all_rules)

ans = 0
for update in sorted_arrays:
    ans += update[(len(update)-1)//2]
print(ans)
