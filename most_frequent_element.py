def most_frequent_element(list):
    return max(set(list), key=list.count)


numbers = [1, 3, 5, 7, 7, 2, 4]
most_frequent_element(numbers)