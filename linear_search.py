def linear_search(array, target):
    for i, a in enumerate(array):
        if a == target:
            return i
    return -1

print(linear_search([1, 3, 5, 7, 9], -1))
