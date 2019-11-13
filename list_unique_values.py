def unique_values(list):
    if len(list) == len(set(list)):
        print('All the elements of the list are unique')
    else:
        print('The list has some duplicates')


unique_values([1, 3, 5, 3, 1])