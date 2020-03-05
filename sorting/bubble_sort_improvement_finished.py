def bubble_sort_finished(arr):

    passes = 0
    comparisions = 0
    swaps = 0
    changed = True      # Improvement: Stop the process if there are no swaps made (i.e. the list has been sorted)

    if changed:
        for i in range(len(arr) - 1):       # Improvement: The value in the first index position will be sorted, if all other values are sorted correctly_finished
            passes += 1
            print(f"\n-------- Start: pass {i + 1} ---------\n")
            changed = False

            for j in range(len(arr) - 1 - i):       # Improvement: The number of comparisions can be reduced, by not comparing the sorted values
                comparisions += 1
                print(f"Comparing: {arr[j]} and {arr[j + 1]}")

                if arr[j] > arr[j + 1]:
                    swaps += 1
                    
                    stored = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j+1] = stored

                    changed = True

                    print(f"*Swapped: {arr[j]} and {arr[j + 1]}")
                    print(f"\n{arr}\n")

            if changed == False:
                break


    print("\n------------------------------------")
    print(f"\nNumber of passes: {passes} \nNumber of comparisons: {comparisions} \nNumber of swaps: {swaps}")
    print(f"\nSorted List: {arr}")


if __name__ == "__main__":

    arr = [8,9,4,5,6,7,2,3]

    bubble_sort_finished(arr)