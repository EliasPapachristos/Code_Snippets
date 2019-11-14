def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 3, 7
print((subtract if a > b else add)(a, b))