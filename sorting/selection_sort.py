def selection_sort(arr):
    
    passes = 0
    comparisions = 0
    swaps = 0

    for sorted_n in range(len(arr) - 1, 0, -1):
        passes += 1
        current_max = 0
        
        for unsorted_n in range(1, sorted_n + 1):
            comparisions += 1

            if arr[unsorted_n] > arr[current_max]:
                swaps += 1
                current_max = unsorted_n
        
        temp = arr[sorted_n]
        arr[sorted_n] = arr[current_max]
        arr[current_max] = temp
        

    return passes, comparisions, swaps


if __name__ == "__main__":

    test_cases = [[3, 1, 0, 4, 2], [3, 1, 2, 0, 5, 7, 9, 4, 8, 6], [4, 3, 2, 1], [8, 7, 6, 5, 4, 3, 2, 1]]

    list_n = 0
    
    results = {}

    for test in test_cases:
        
        list_n += 1

        passes, comparisions, swaps = selection_sort(test)

        results[(list_n, 'Passes')] = passes
        results[(list_n, 'Comparisions')] = comparisions
        results[(list_n, 'Swaps' )] = swaps


    inspect = (int(len(results)/3))
    print('\nP = Passes')
    print('C = Comparisons')
    print('S = Swaps\n')
    print('           P', '   C', '   S')
    print('        ----------------')

    for list_n in range(1, inspect + 1):
        print('List', list_n, ":", " ",results[(list_n, 'Passes')], " ",results[(list_n, 'Comparisions')], " ",results[(list_n, 'Swaps' )])