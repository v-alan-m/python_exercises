def quick_sort(arr):
    
    quick_sort_helper(arr,0,len(arr) - 1)

    
def quick_sort_helper(arr,first,last):
    
    if first < last:
        split_point = split(arr,first,last)
        
        quick_sort_helper(arr,first,split_point - 1)
        quick_sort_helper(arr,split_point + 1,last)

        
def split(arr,first,last):
    
    pivot_value = arr[first]
    
    left_mark = first + 1
    right_mark = last
    
    done = False
    
    while not done:
        
        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark += 1
            
        while right_mark >= left_mark and arr[right_mark] >= pivot_value:
            right_mark -= 1
        
        # Exit the main while loop
        # Return right_mark to create a new pivot_value for the new split
        if right_mark < left_mark:
            done = True
            
        else: # Make the swap if:
            # The left mark is greater than the pivot_value, and
            # The right mark is less than the pivot_value
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]
            
    # Make the right_mark the new pivot_value
        # So that the pivot_value is in the centre of the current partion, and
            # The smallest swapped value is moved to the beginning of the list
    arr[first], arr[right_mark] = arr[right_mark], arr[first]
    
    return right_mark

if __name__ == '__main__':
    arr = [2,5,4,6,7,3,1,4,12,11]
    quick_sort(arr)
    print(arr)