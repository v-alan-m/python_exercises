def ascending(a, b):
    return b > a


def descending(a, b):
    return b < a


def ascending_prefer_evens(a, b):
    if a % 2 == b % 2:
        return b > a
    else:
        return a % 2


def descending_prefer_evens(a, b):
    if a % 2 == b % 2:
        return b < a
    else:
        return a % 2


def descending_prefer_odds(a, b):
    if a % 2 == b % 2:
        return b < a
    else:
        return b % 2


def ascending_prefer_odds(a, b):
    if a % 2 == b % 2:
        return b > a
    else:
        return b % 2


def find_item(to_search, ordered=ascending):
    desired_index = 0
    for i in range(1, len(to_search)):
        if not ordered(to_search[i], to_search[desired_index]):
            desired_index = i

    return desired_index, to_search[desired_index]


def bubble_custom_order(to_sort, ordered=ascending):
    """Implementation of the naive bubble sort for a list of integers."""
    swap_made = True
    for i in range(len(to_sort)):
        if not swap_made:
            break
        swap_made = False
        for j in range(len(to_sort) - 1):
            if not ordered(to_sort[j], to_sort[j + 1]):
                tmp = to_sort[j]
                to_sort[j] = to_sort[j + 1]
                to_sort[j + 1] = tmp
                swap_made = True
    print("\033[32;1mSort complete: {}\033[0m".format(to_sort))


if __name__ == "__main__":
    test_list = [3, 1, 5, 9, 2, 4, 13, 8, 11]
    print(test_list)

    print(find_item(test_list))
    print(find_item(test_list, descending))
    print(find_item(test_list, ascending_prefer_evens))
    print(find_item(test_list, ascending_prefer_odds))
    print(find_item(test_list, descending_prefer_evens))
    print(find_item(test_list, descending_prefer_odds))

    bubble_custom_order(test_list[:])
    bubble_custom_order(test_list[:], descending)
    bubble_custom_order(test_list[:], ascending_prefer_evens)
    bubble_custom_order(test_list[:], ascending_prefer_odds)
    bubble_custom_order(test_list[:], descending_prefer_evens)
    bubble_custom_order(test_list[:], descending_prefer_odds)
