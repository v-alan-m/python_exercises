def insertion_sort(to_sort):
    """(Instrumented) Implementation of insertion sort."""
    print("\033[31;1mGot list {}\033[0m".format(to_sort))
    total_moves = 0
    total_cmps = 0

    for i in range(1, len(to_sort)):
        print("\tStarting pass {}/{}...".format(i, len(to_sort) - 1))
        pass_moves = 0
        pass_cmps = 0

        tmp = to_sort[i]    # Take a copy of the item being considered
        j = 0
        # The two conditions here mean we don't need a 'break'.
        # They cause the loop to stop if we reach the start of the list,
        # or if we reach an item in the 'sorted' part that is less that the item being considered.
        while (j < i and to_sort[i - j - 1] > tmp):
            print("\t\t\033[33mComparing indices {} and {} ({} > {}?)\033[0m".format(i - j - 1, i, to_sort[i - j - 1], tmp))
            pass_cmps += 1
            # Move the item to the right by one space
            to_sort[i - j] = to_sort[i - j - 1]
            print("\t\t\t\033[33mMoved index {} right. List post-move: {}\033[0m".format(i - j - 1, to_sort))
            pass_moves += 1
            j += 1

        if j == i:
            print("\t\t\033[33mReached start of list.\033[0m")
        else:
            print("\t\t\033[33mCompared indices {} and {} ({} > {}?)\033[0m".format(i - j - 1, i, to_sort[i - j - 1], tmp))
            pass_cmps += 1

        # Now put the item being considered into the correct spot
        to_sort[i - j] = tmp
        print("\t\t\t\033[33mInserted item '{}' into new position. List post-insertion: {}\033[0m".format(tmp, to_sort))
        pass_moves += 1
        print("\t\033[33;1mPass {}/{} complete. {} cmps, {} moves.\n\tCurrent list: {}\033[0m".format(i, len(to_sort) - 1, pass_cmps, pass_moves, to_sort))

        total_cmps += pass_cmps
        total_moves += pass_moves

    print("\033[32;1mSort complete. {} passes, {} cmps, {} moves.\nList: {}\033[0m".format(i + 1, total_cmps, total_moves, to_sort))


if __name__ == '__main__':
    from sys import argv
    test_lists = [3, 1, 0, 4, 2], [3, 1, 2, 0, 5, 7, 9, 4, 8, 6], [4, 3, 2, 1]

    for tl in test_lists:
        insertion_sort(tl)
