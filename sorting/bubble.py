def bubble(to_sort):
    """Implementation of the naive bubble sort for a list of integers."""
    for i in range(len(to_sort)):
        print "Starting pass {}...".format(i)
        for j in range(len(to_sort) - 1):
            # -1 in this range because we compare to_sort[j] with [j+1] and we don't want to over-run
            if to_sort[j] > to_sort[j + 1]:
                tmp = to_sort[j]
                to_sort[j] = to_sort[j + 1]
                to_sort[j + 1] = tmp
                print "\033[33m{}\033[0m".format(to_sort)
        print "\033[33;1mPass complete: {}\033[0m".format(to_sort)
    print "\033[32;1mSort complete: {}\033[0m".format(to_sort)

if __name__ == "__main__":
    test_list = [3, 1, 0, 2, 4, 8, 7, 9, 6, 5]
    bubble(test_list)
