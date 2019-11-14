def merge_dictionaries(a, b):
    return {**a, **b}


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dictionaries(a, b))
