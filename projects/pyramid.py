def pyramid(n):
    list_1 = []
    for x in range(1, n+1):
        new_list = [1] * x
        list_1.append(new_list)
    return list_1

print(pyramid(4))
