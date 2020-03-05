total_calls = 0
current_depth = 0
max_depth = 0
total_cmps = 0

def merge_sort(to_sort):
    """(Instrumented) Implementation of merge sort."""
    global total_calls
    global current_depth
    global max_depth
    global total_cmps

    call_cmps = 0

    total_calls += 1
    current_depth += 1
    current_call = total_calls
    if current_depth > max_depth:
        max_depth = current_depth

    if current_depth == 1:
        print("\033[31;1mGot list {} (depth {}, call {})\033[0m".format(to_sort, current_depth, current_call))
    else:
        print("\t\033[31mAt depth {} (call {}); sorting list part {}\033[0m".format(current_depth, current_call, to_sort))

    if len(to_sort) < 2:
        print("\t\033[32mAt depth {} (call {}); list {} is already sorted.\033[0m".format(current_depth, current_call, to_sort))
        current_depth -= 1
        return to_sort

    # Sort each half of the list
    mid_point = len(to_sort) // 2
    left_part = merge_sort(to_sort[:mid_point])
    right_part = merge_sort(to_sort[mid_point:])

    print("\t\033[33;1mBack at depth {}/call {}\033[0m".format(current_depth, current_call))

    # Now the meat of the work: merge the two parts together
    left_index = 0
    right_index = 0
    result_index = 0

    out_list = [None for i in range(len(to_sort))]  # Making sure the output is big enough
    # The reason for not using append() everywhere is that it would be slower
    # as a result of the regular copying and reassignment it would cause.

    while left_index < len(left_part) and right_index < len(right_part):
        call_cmps += 1

        print("\t\t\033[33m[{},{}]Comparing left_part[{}] = {} to right_part[{}] = {}".format(current_depth, current_call, left_index, left_part[left_index], right_index, right_part[right_index]))
        if left_part[left_index] <= right_part[right_index]:
            # If the next value from the left part is less than or equal
            # to the next 'right' value, copy it into the output list
            print("\t\t  \033[33m[{},{}]Outputting {}\033[0m".format(current_depth, current_call, left_part[left_index]))
            out_list[result_index] = left_part[left_index]
            left_index += 1

        else:
            # Otherwise, copy the value from the 'right' part into the output
            print("\t\t  \033[33m[{},{}]Outputting {}\033[0m".format(current_depth, current_call, right_part[right_index]))
            out_list[result_index] = right_part[right_index]
            right_index += 1

        result_index += 1

    # It's unlikely that both parts were completely exhausted by the above loop,
    # so now go through and copy and remaining items into the output list.

    if left_index < len(left_part):
        print("\t\t  \033[33m[{},{}]Outputting remaining left part {}\033[0m".format(current_depth, current_call, left_part[left_index:]))

    while left_index < len(left_part):
        out_list[result_index] = left_part[left_index]
        left_index += 1
        result_index += 1

    if right_index < len(right_part):
        print("\t\t  \033[33m[{},{}]Outputting remaining right part {}\033[0m".format(current_depth, current_call, right_part[right_index:]))

    while right_index < len(right_part):
        out_list[result_index] = right_part[right_index]
        right_index += 1
        result_index += 1

    print("\t\033[33m[{},{}] {} cmps this call.\033[0m".format(current_depth, current_call, call_cmps))

    current_depth -= 1
    total_cmps += call_cmps
    if current_depth == 0:
        print("Max depth: {}. Total calls: {}. Toal cmps: {}\033[0m".format(max_depth, total_calls, total_cmps))
        max_depth = 0
        total_calls = 0
        total_cmps = 0

    return out_list


if __name__ == '__main__':
    from sys import argv
    test_lists = [3, 1, 0, 4, 2], [3, 1, 2, 0, 5, 7, 9, 4, 8, 6], [4, 3, 2, 1]

    for tl in test_lists:
        print(merge_sort(tl))
