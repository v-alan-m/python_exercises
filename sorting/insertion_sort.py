def insertion_sort(arr):
    
    passes = 0
    comparisions = 0
    swaps = 0


    for i in range(1, len(arr)):
        passes += 1
        current_value = arr[i]
        position = i
        
        while position > 0 and arr[position - 1] > current_value:
            comparisions += 1
            arr[position] = arr[position - 1]
            position -= 1
            
        arr[position] = current_value
        swaps += 1
    
    return passes, comparisions, swaps


if __name__ == "__main__":

    test_cases = [[3, 1, 0, 4, 2], [3, 1, 2, 0, 5, 7, 9, 4, 8, 6], [4, 3, 2, 1], [8, 7, 6, 5, 4, 3, 2, 1]]

    list_n = 0
    
    results = {}

    for test in test_cases:
        
        list_n += 1

        passes, comparisions, swaps = insertion_sort(test)

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