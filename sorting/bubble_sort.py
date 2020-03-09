def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                stored = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = stored

if __name__ == "__main__":
    arr = [8,9,4,5,6,7,2,3]
    bubble_sort(arr)
    print(f"Sorted: {arr}")