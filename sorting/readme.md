# Sorting
This set of exercises will have you develop a set of sorting algorithm implementations in Python. In each case, the parameters are as follows:
 - Each sorting algorithm should be implemented as a function which takes a Python *list* as its sole parameter.
 - The input data will always be a list of *integer* values.
 - These functions should sort the numbers in *ascending* order.
 - These functions should return the sorted list only.

Your solutions should all exist on their own branches for ease of management.


## Exercise 1: Bubble Sort
Implement a bubble sort in python. Bubble sort is a very simple, slow sort. The algorithm can be surmised as follows:
 - Compare the first and second numbers in the list; swap them if they're out of order.
 - Compare the second and third numbers; swap if they're out of order.
 - Repeat until you reach the end of the list.
 - This marks the end of the first pass, and guarantees that the largest number is at the end of the list, leaving one fewer numbers in the 'unsorted' part.
 - Pass through the list repeatedly until all the numbers have been sorted.

## Exercise 2: Improving Bubble Sort
Before starting this exercise, add some instrumentation to your existing bubble sort code. For the test cases you've tried, record:
 - The number of passes made through the list
 - The total number of comparisons made
 - The total number of swaps made

There are three different optimisations possible on the most naive version of bubble sort. Consider how you can save time in each of the following situations:
 1. An already sorted list, or a list that is sorted after only a handful of passes.
 2. Recall that each pass guarantees the (next) largest item has been sorted into the correct place - is there any benefit to continuing eg the 15th pass into the top 14 items?
 3. If there are `n` items in the list and `n - 1` are sorted...

These situations have been listed in order of the scale of their expected impact.
Try implementing changes to your bubble sort to handle each one and use your instrumenting code to investigate the impact of each change.

Can you work out mathematical expressions for the maximum amount of work done by the bubble sort? (Max number of swaps, max number of comparisons, etc).
How about the minimum?
Can you work out what the 'average' behaviour might be like?

Try using your instrumented code to see if you've got these expressions right.

### Test data for Ex2
[This test data can also be used to verify your solution to Ex1]
 1. `[3, 1, 0, 4, 2]`
   a. Naive BS: 5 passes, 20 comparisons, 5 swaps
   b. Improvement 1: 3p, 12c, 5s
   c. Improvement 2: 5p, 10c, 5s
   d. Improvement 3: 4p, 16c, 5s
   e. All improvements: 3p, 9c, 5s

 2. `[3, 1, 2, 0, 5, 7, 9, 4, 8, 6]`
   a. Naive BS: 10p, 90c, 12s
   b. Improvement 1: 4p, 36c, 12s
   c. Improvement 2: 10p, 45c, 12s
   d. Improvement 3: 9s, 81c, 12s
   e. All improvements: 4p, 30c, 12s

 3. `[4, 3, 2, 1]`
   a. Naive BS: 4p, 12c, 6s
   b. Improvement 1: 4p, 12c, 6s
   c. Improvement 2: 4p, 6c, 6s
   d. Improvement 3: 3p, 9c, 6s
   e. All improvements: 3p, 6c, 6s


## Exercise 3: Selection and Insertion Sorts
For all its simplicity, bubble sort is typically hideously slow. Selection and Insertion sorts are usually a big improvement for relatively little extra complexity.
The can be considered two variants on the same fundamental process, which is why they're often introduced together.
Each has advantages and disadvantages, which you shall investigate below.

### Ex 3 a: Selection Sort
The selection sort algorithm can be surmised as follows:
 - Scan through the list, searching for the largest value.
 - Once identified, swap it with the last item in the list.
 - Repeat until sorted - though only search for the largest item in the *unsorted part*, and swap with the last item in the *unsorted part*.

### Ex 3 b: Insertion Sort
The intertion sort algorithm can be surmised as follows:
 - Split the list into 'sorted' and 'unsorted' parts; initially the 'sorted' part is just the first item.
 - Take the first number from the 'unsorted' part and compare it to the last 'sorted' value.
 - If the two are out of order, move the 'sorted' one space to the right.
 - Repeatedly compare the 'test' value with the next 'sorted' value until it is larger.
 - Insert the 'test' value in the slot freed by the last move.
 - The 'sorted' part is now one item longer; repeat until the full list is sorted.
 - NB: 'right' refers to position in the list if written with index 0 on the left, ie what you see when you `print(test_list)`

### Ex 3 c: Instrumentation
Add similar instrumentation to that used for the bubble sorts to the selection and insertion sorts so you can compare their behaviour.
Can you apply any of the optimisations from the bubble sort to these algorithms?
What effect do they have on their performance?

As with the bubble sort, can you work out what the minimum, maximum, and average 'work' (passes, comparisons, swaps) is for each of these algorithms?

What does all this mean for the relative performance of selection sort and insertion sort?
In what situation(s) would it make sense to pick one over the other?

### Ex 3 d: Min/max item
A critical part of the selection sort algorithm is locating the largest item in the list.
 1. Write a dedicated function to find the largest item in a list; it should return both the largest value, and its position in the list.
 2. Modify your function to allow it to search for the largest *or smallest* item.
 3. Modify your function to allow it to use a custom comparison function to find a specific item, eg given
    ```Python
    def largest_even(a, b):
        if a % 2 == b % 2:
            return b > a
        else:
            return a % 2
    ```
    And the list `[3, 1, 5, 9, 2, 7, 13, 8, 11]`, your function should return `8` as the largest value, and its index '7'.

## Exercise 4: Merge Sort
Merge sort brings a step change in performance over the previous sorts. It achieves this by approaching the problem in a fundamentally different way.

### Ex 4 a: Recursion: Factorials and Fibonacci
Merge sort is a *recursive* algorithm, meaning it calls itself.
To introduce that concept in a simpler setting, we will first examine classic example of recursion.

Recursion is simply the process of a function calling itself, and these two examples should demonstrate its power and some of the pitfalls.

 1. Write a function to calculate the factorial of its input (which must be a non-negative integer).
     - n! = n * (n-1) * (n-2) * (n-3) * ... * 2 * 1
     - n! = n * (n-1)!
     - As a function therefore, `fact(n) -> n * fact(n-1)`
     - Note: be **careful** of the termination condition! *Infinite recursion* is no fun!
 2. Write a function to calculate the nth Fibonacci number.
     - The Fibonacci numbers are defined by `fib(n) = fib(n-1) + fib(n-2)`, with `fib(0) = fib(1) = 1`

### Ex 4 b: Basic Merge Sort
The merge sort algorithm can be surmised as follows:
 - Split the list in half.
 - Apply merge sort to the left half.
 - Apply merge sort to the right half.
 - Merge the two halves back together. Merging two lists proceeds as follows:
     - Compare the next item from the left and right lists
     - Output the smaller one
     - Repeat until one list is empty, then output the remaining items from the other.
 - Note: A list containing one item and an empty list are *already* sorted.

### Ex 4 c: Instrumentation
As with the other sorts, add some instrumentation to your merge sort.
You have to be more careful here, as the recursive nature of the algorithm means it's harder to track things properly across the multiple calls.

Analyse your merge sort with the help of your instrumentation code.
What does its best-, worst-, and average-case performance look like?

## Exercise 5: Quicksort
Quicksort is an excellent, standard algorithm.
Like merge sort, quicksort is a recursive algorithm.
Unlike merge sort (where most of the work is done by the merge step on the way back *up*), most of the work of quicksort is done during the process of breaking the list *down* into two parts.

The algorithm can be surmised as follows:
 - Select a 'pivot'
 - Create a list containing all items smaller than the pivot (the 'left' part), and another containing all other items except the pivot itself (the 'right' part)
 - Apply quicksort to the left part
 - Apply quicksort to the right part
 - The sorted input is obtained by appending the pivot to the left part, then appending the right part to that.

Note: various optimisations are possible, which reduce the amount of copying this algorithm requires. Can you think of any?
