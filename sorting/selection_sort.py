def selection_sort(arr):
        
    for sorted_n in range(len(arr) - 1, 0, -1):
        current_max = 0
        
        for unsorted_n in range(1, sorted_n + 1):
            if arr[unsorted_n] > arr[current_max]:
                current_max = unsorted_n
        
        temp = arr[sorted_n]
        arr[sorted_n] = arr[current_max]
        arr[current_max] = temp
        
    print(arr)


if __name__ == "__main__":

    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    selection_sort(arr)