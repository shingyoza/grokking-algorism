def binary_search(sorted_list, target):
    start = 0
    end = len(sorted_list) -1
    while (start <= end):
        mid_index = (start + end) // 2
        mid = sorted_list[mid_index]
        if (mid == target):
            return mid_index

        if (mid < target):
            start = mid_index + 1
        elif (mid > target):
            end = mid_index - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], -1))