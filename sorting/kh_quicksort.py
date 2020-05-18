def quicksort(to_sort):
	# Algorithm: copy all values less than pivot to one list, other to another
	# Recurse
	# Concatenate

	if (len(to_sort) < 2):
		return to_sort

	pivot = to_sort[0]

	# List comprehension for left part
	left_part = [val for val in to_sort if val < pivot]

	# Equivalent for loop for right part
	right_part = []
	for val in to_sort[1:]:
		if val >= pivot:
			right_part.append(val)

	# NB: Would be more efficient to use a single loop to construct both parts

	left_part = quicksort(left_part)
	right_part = quicksort(right_part)

	to_sort = left_part[:]
	to_sort.append(pivot)
	to_sort.extend(right_part)

	return to_sort


if __name__ == '__main__':
	l = [3, 1, 4, 2, 8, 5, 9, 0, 6, 7]
	l = quicksort(l)
	print(l)
