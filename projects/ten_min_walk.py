def is_valid_walk(walk):
    #determine if walk is valid
    lapse = [0, 0]
    if len(walk) != 10:
        return False
    for x in walk:
        if x == 'n':
            lapse[0] += 1
        if x == 's':
            lapse[0] -= 1
        if x == 'e':
            lapse[1] += 1
        if x == 'w':
            lapse[1] -= 1
    if lapse == [0, 0]:
        return True
    else:
        return False

print(is_valid_walk(['n', 'e', 's', 'w', 'n', 's', 'e', 'w', 'n', 's', 's', 'n']))