def selection_sort(to_sort):
    """(Instrumented) Implementation of selection sort."""
    print("\033[31;1mGot list {}\033[0m".format(to_sort))
    total_swaps = 0
    total_cmps = 0

    for i in range(len(to_sort) - 1):
        print("\tStarting pass {}/{}...".format(i + 1, len(to_sort) - 1))
        pass_swaps = 0
        pass_cmps = 0

        # Finding the index of the largest value
        largest_index = 0
        for j in range(1, len(to_sort) - i):
            print("\t\t\033[33mComparing indices {} and {} ({} > {}?)\033[0m".format(j, largest_index, to_sort[j], to_sort[largest_index]))
            pass_cmps += 1
            if to_sort[j] > to_sort[largest_index]:
                largest_index = j

        # Swapping the largest item with the last *unsorted* value.
        # We *could* check if the largest index is different from the 'end_index',
        # but that would add one extra cmp for each pass, at the cost of saving
        # a small number of swaps. Exercise for the reader: min/max/avg saving?
        tmp = to_sort[largest_index]
        end_index = len(to_sort) - 1 - i
        to_sort[largest_index] = to_sort[end_index]
        to_sort[end_index] = tmp
        print("\t\t\t\033[33mSwapped. List post-swap: {}\033[0m".format(to_sort))
        pass_swaps += 1

        print("\t\033[33;1mPass {}/{} complete. {} cmps, {} swaps.\n\tCurrent list: {}\033[0m".format(i + 1, len(to_sort) - 1, pass_cmps, pass_swaps, to_sort))
        total_cmps += pass_cmps
        total_swaps += pass_swaps

    print("\033[32;1mSort complete. {} passes, {} cmps, {} swaps.\nList: {}\033[0m".format(i + 1, total_cmps, total_swaps, to_sort))


if __name__ == '__main__':
    from sys import argv
    test_lists = [3, 1, 0, 4, 2], [3, 1, 2, 0, 5, 7, 9, 4, 8, 6], [4, 3, 2, 1]

    for tl in test_lists:
        selection_sort(tl)
