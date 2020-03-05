def find_largest(to_search):
    """Find the largest item in the provided list."""

    largest_index = 0
    for i in range(1, len(to_search)):
        if to_search[i] > to_search[largest_index]:
            largest_index = i

    return largest_index, to_search[largest_index]


def find_smallest(to_search):
    """Find the smallest item in the provided list."""

    largest_index = 0
    for i in range(1, len(to_search)):
        if to_search[i] < to_search[largest_index]:
            largest_index = i

    return largest_index, to_search[largest_index]


def find_largest_or_smallest(to_search, smallest=False):
    """Find the largest or smallest item in the provided list."""

    largest_index = 0
    for i in range(1, len(to_search)):
        if smallest:
            if to_search[i] < to_search[largest_index]:
                largest_index = i
        else:
            if to_search[i] > to_search[largest_index]:
                largest_index = i

    return largest_index, to_search[largest_index]


def find_largest_or_smallest_2(to_search, smallest=False):
    """Find the largest or smallest item in the provided list."""

    largest_index = 0
    for i in range(1, len(to_search)):
        if smallest and to_search[i] < to_search[largest_index]:
            largest_index = i
        elif not smallest and to_search[i] > to_search[largest_index]:
            largest_index = i

    return largest_index, to_search[largest_index]


def find_largest_or_smallest_3(to_search, smallest=False):
    """Find the largest or smallest item in the provided list."""

    largest_index = 0
    for i in range(1, len(to_search)):
        if (smallest and to_search[i] < to_search[largest_index]) or \
            (not smallest and to_search[i] > to_search[largest_index]):
            largest_index = i

    return largest_index, to_search[largest_index]


if __name__ == "__main__":
    test_list = [3, 1, 5, 9, 2, 7, 13, 8, 11]

    print(find_largest(test_list))
    print(find_smallest(test_list))
    print(find_largest_or_smallest(test_list))
    print(find_largest_or_smallest(test_list, True))
    print(find_largest_or_smallest_2(test_list))
    print(find_largest_or_smallest_2(test_list, True))
    print(find_largest_or_smallest_3(test_list))
    print(find_largest_or_smallest_3(test_list, True))
