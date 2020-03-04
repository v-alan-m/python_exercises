(for a list of n items)

Unoptimised bubble sort
	  | Best | Worst | Average
------|------|-------|-------------------------
Passes|	n	 |	n	 |	n
Swaps |	0	 |	(n-1)+(n-2)+(n-3)...=n(n+1)/2 | (n-1)/2+(n-2)/2+...=n(n+1)/4
Cmps  | n(n-1) | n(n-1) | n(n-1)

For unoptimised bubble sort get:
	- O(n) passes
	- O(n^2) swaps
	- O(n^2) cmp
	- O(n^2+n^2+n) total work = O(n^2)

	- Overall time cost/complexity: O(n^2)
	  -> The time taken to bubble sort a list will increase with the square of the list size

Fully optimised bubble sort
      | Best | Worst | Average
----------------------------------------------
Passes| 1    | n-1	| (n-1)/2
Swaps | 0    | n(n-1)/2 | n(n-1)/8
Cmps  | n-1  | (n-1)+(n-2)+(n-3)+...=n(n+1)/2 | n(n+1)/4

For optimised bubble sort get:
	- O(n) passes
	- O(n^2) swaps
	- O(n^2) cmp
	- O(n^2+n^2+n) total work = O(n^2)

	- Overall time cost/complexity: O(n^2)
	  -> The time taken to bubble sort a list will increase with the square of the list size
	- Even though it will be faster, it still has the same overall type of behaviour
