# Sorting
This set of exercises will have you develop a set of sorting algorithm implementations in Python. In each case, the parameters are as follows:
 - Each sorting algorithm should be implemented as a function which takes a Python *list* as its sole parameter.
 - The input data will always be a list of *integer* values.
 - These functions should sort the numbers in *ascending* order.
 - These functions should return the sorted list only.

Your solutions should all exist on their own branches for ease of management.


## Exercise 1: Bubble sort
Implement a bubble sort in python. Bubble sort is a very simple, slow sort. The algorithm can be surmised as follows:
 - Compare the first and second numbers in the list; swap them if they're out of order.
 - Compare the second and third numbers; swap if they're out of order.
 - Repeat until you reach the end of the list.
 - This marks the end of the first pass, and guarantees that the largest number is at the end of the list, leaving one fewer numbers in the 'unsorted' part.
 - Pass through the list repeatedly until all the numbers have been sorted.
