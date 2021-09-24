def two_sort(array):
    new_list = []
    array = sorted(array)
    for x in array:
        new_list.append('***'.join(x))
    return new_list[0]


print(two_sort(['lpple', 'arrow', 'fEar', 'day', 'Goat', 'Hatttt', 'zoppe']))
