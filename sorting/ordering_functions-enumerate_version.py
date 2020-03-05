def max(a, b):
    return b > a

def min(a, b):
    return b < a

def largest_even(a, b):
    if a % 2 == b % 2:
        return b > a
    else:
        return a % 2

def smallest_even(a, b):
    if a % 2 == b % 2:
        return b < a
    else:
        return a % 2

def find(l, ordering=max):
    largest_idx, largest_val = 0, l[0]

    for i, v in enumerate(l[1:]):
        if ordering(largest_val, v):
            largest_idx, largest_val = i + 1, v

    return largest_idx, largest_val


def main():
    tl = [3, 1, 5, 9, 2, 7, 13, 8, 11]
    print("test list: {}\nlargest @ idx {} - val {}".format(tl, *find(tl)))
    print("smallest @ idx {} - val {}".format(*find(tl, min)))
    print("largest even @ idx {} - val {}".format(*find(tl, largest_even)))
    print("smallest even @ idx {} - val {}".format(*find(tl, smallest_even)))


if __name__ == "__main__":
    main()
