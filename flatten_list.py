def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(el):
    flat_list = []
    [flat_list.extend(deep_flatten(e)) for e in el] if isinstance(el, list) else flat_list.append(el)
    return flat_list


print(deep_flatten([1, [2], [[3], 4], 5, [6, 7, 8, 9], 10]))