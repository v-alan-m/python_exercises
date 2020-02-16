def naive_bubble(to_sort):
    """(Instrumented) Implementation of the naive bubble sort."""
    print "\033[31;1mGot list {}\033[0m".format(to_sort)
    total_swaps = 0
    total_cmps = 0
    for i in range(len(to_sort)):
        print "\tStarting pass {}/{}...".format(i + 1, len(to_sort))
        pass_swaps = 0
        pass_cmps = 0
        for j in range(len(to_sort) - 1):
            # -1 because we compare to_sort[j] and [j+1] and we don't want to overrun.
            pass_cmps += 1
            print "\t\t\033[33mComparing indices {} and {} ({} > {}?)\033[0m".format(j, j + 1, to_sort[j], to_sort[j + 1])
            if to_sort[j] > to_sort[j + 1]:
                pass_swaps += 1
                tmp = to_sort[j]
                to_sort[j] = to_sort[j + 1]
                to_sort[j + 1] = tmp
                print "\t\t\t\033[33mSwapped. List post-swap: {}\033[0m".format(to_sort)
        print "\t\033[33;1mPass {}/{} complete. {} cmps, {} swaps.\n\tCurrent list: {}\033[0m".format(i + 1, len(to_sort), pass_cmps, pass_swaps, to_sort)
        total_cmps += pass_cmps
        total_swaps += pass_swaps
    print "\033[32;1mSort complete. {} passes, {} cmps, {} swaps.\nList: {}\033[0m".format(len(to_sort), total_cmps, total_swaps, to_sort)


def improvement_1_bubble(to_sort):
    """
    (Instrumented) Implementation of bubble sort with a single optimisation -
    terminates early if no swaps have been made in a given pass.
    """
    print "\033[31;1mGot list{}\033[0m".format(to_sort)
    total_swaps = 0
    total_cmps = 0
    swap_made = True
    i = 0
    while swap_made and i < len(to_sort):
        print "\tStarting pass {}/{}...".format(i + 1, len(to_sort))
        pass_swaps = 0
        # Yes, we could use this, but in general don't use instrumentation/debug code to enable functionality
        # ie, it should be possible to rip out the instrumentation code without breaking anything.
        pass_cmps = 0
        swap_made = False
        for j in range(len(to_sort) - 1):
            pass_cmps += 1
            print "\t\t\033[33mComparing indices {} and {} ({} > {}?)\033[0m".format(j, j + 1, to_sort[j], to_sort[j + 1])
            if to_sort[j] > to_sort[j + 1]:
                pass_swaps += 1
                tmp = to_sort[j]
                to_sort[j] = to_sort[j + 1]
                to_sort[j + 1] = tmp
                swap_made = True
                print "\t\t\t\033[33mSwapped. List post-swap: {}\033[0m".format(to_sort)
        print "\t\033[33;1mPass {}/{} complete. {} cmps, {} swaps.\n\tCurrent list: {}\033[0m".format(i + 1, len(to_sort), pass_cmps, pass_swaps, to_sort)
        total_cmps += pass_cmps
        total_swaps += pass_swaps
        i += 1
    print "\033[32;1mSort complete. {} passes, {} cmps, {} swaps.\nList: {}\033[0m".format(i, total_cmps, total_swaps, to_sort)


def improvement_2_bubble(to_sort):
    """
    (Instrumented) Implementation of bubble sort with a single optimisation -
    avoids checking the last k items after k passes.
    """
    print "\033[31;1mGot list{}\033[0m".format(to_sort)
    total_swaps = 0
    total_cmps = 0
    for i in range(len(to_sort)):
        print "\tStarting pass {}/{}...".format(i + 1, len(to_sort))
        pass_swaps = 0
        pass_cmps = 0
        for j in range(len(to_sort) - 1 - i):   # The extra '-i' does all the work here.
            pass_cmps += 1
            print "\t\t\033[33mComparing indices {} and {} ({} > {}?)\033[0m".format(j, j + 1, to_sort[j], to_sort[j + 1])
            if to_sort[j] > to_sort[j + 1]:
                pass_swaps += 1
                tmp = to_sort[j]
                to_sort[j] = to_sort[j + 1]
                to_sort[j + 1] = tmp
                print "\t\t\t\033[33mSwapped. List post-swap: {}\033[0m".format(to_sort)
        print "\t\033[33;1mPass {}/{} complete. {} cmps, {} swaps.\n\tCurrent list: {}\033[0m".format(i + 1, len(to_sort), pass_cmps, pass_swaps, to_sort)
        total_cmps += pass_cmps
        total_swaps += pass_swaps
    print "\033[32;1mSort complete. {} passes, {} cmps, {} swaps.\nList: {}\033[0m".format(len(to_sort), total_cmps, total_swaps, to_sort)


def improvement_3_bubble(to_sort):
    """
    (Instrumented) Implementation of bubble sort with a single optimisation -
    avoids making an extra pass since if n-1/n are sorted, the last must be in the right place.
    """
    print "\033[31;1mGot list{}\033[0m".format(to_sort)
    total_swaps = 0
    total_cmps = 0
    for i in range(len(to_sort) - 1):	# This -1 is all it takes (plus in a few other places for prints)
        print "\tStarting pass {}/{}...".format(i + 1, len(to_sort) -1)
        pass_swaps = 0
        pass_cmps = 0
        for j in range(len(to_sort) - 1):
            pass_cmps += 1
            print "\t\t\033[33mComparing indices {} and {} ({} > {}?)\033[0m".format(j, j + 1, to_sort[j], to_sort[j + 1])
            if to_sort[j] > to_sort[j + 1]:
                pass_swaps += 1
                tmp = to_sort[j]
                to_sort[j] = to_sort[j + 1]
                to_sort[j + 1] = tmp
                print "\t\t\t\033[33mSwapped. List post-swap: {}\033[0m".format(to_sort)
        print "\t\033[33;1mPass {}/{} complete. {} cmps, {} swaps.\n\tCurrent list: {}\033[0m".format(i + 1, len(to_sort) - 1, pass_cmps, pass_swaps, to_sort)
        total_cmps += pass_cmps
        total_swaps += pass_swaps
    print "\033[32;1mSort complete. {} passes, {} cmps, {} swaps.\nList: {}\033[0m".format(len(to_sort) - 1, total_cmps, total_swaps, to_sort)


def final_bubble(to_sort):
    """
    (Instrumented) Implementation of a fully-optimised bubble sort:
      - terminates early if no swaps are made on a given pass
      - avoids re-checking the already-sorted part of the list
      - doesn't perform a pointless final pass (n-1/n sorted -> all n are sorted)
    """
    print "\033[31;1mGot list{}\033[0m".format(to_sort)
    total_swaps = 0
    total_cmps = 0
    swap_made = True	# <- improvement 1
    i = 0
    while swap_made and i < len(to_sort) - 1:	# <- improvement 3
        print "\tStarting pass {}/{}...".format(i + 1, len(to_sort) - 1)
        pass_swaps = 0
        pass_cmps = 0
        swap_made = False
        for j in range(len(to_sort) - 1 - i):	# <- improvement 2
            pass_cmps += 1
            print "\t\t\033[33mComparing indices {} and {} ({} > {}?)\033[0m".format(j, j + 1, to_sort[j], to_sort[j + 1])
            if to_sort[j] > to_sort[j + 1]:
                pass_swaps += 1
                tmp = to_sort[j]
                to_sort[j] = to_sort[j + 1]
                to_sort[j + 1] = tmp
                swap_made = True
                print "\t\t\t\033[33mSwapped. List post-swap: {}\033[0m".format(to_sort)
        print "\t\033[33;1mPass {}/{} complete. {} cmps, {} swaps.\n\tCurrent list: {}\033[0m".format(i + 1, len(to_sort) - 1, pass_cmps, pass_swaps, to_sort)
        total_cmps += pass_cmps
        total_swaps += pass_swaps
        i += 1
    print "\033[32;1mSort complete. {} passes, {} cmps, {} swaps.\nList: {}\033[0m".format(i, total_cmps, total_swaps, to_sort)


if __name__ == "__main__":
    from sys import argv
    test_lists = [3, 1, 0, 4, 2], [3, 1, 2, 0, 5, 7, 9, 4, 8, 6], [4, 3, 2, 1]
    sorts = {'0': naive_bubble, '1': improvement_1_bubble,
             '2': improvement_2_bubble, '3': improvement_3_bubble,
             'f': final_bubble
             }

    if len(argv) == 2:
        alg = sorts.get(argv[1], naive_bubble)
    else:
        alg = naive_bubble

    for tl in test_lists:
        alg(tl)
