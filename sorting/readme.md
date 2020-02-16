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
