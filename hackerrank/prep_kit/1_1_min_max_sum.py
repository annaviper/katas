"""Given five positive integers, find the minimum
and maximum values that can be calculated
by summing exactly four of the five integers.

Example:
arr = [1, 3, 5, 7, 9]
The minimum sum is `1 + 3 + 5 + 7 = 16`
The maximum sum is `3 + 5 + 7 + 9 = 24`
The function prints: 16 24
"""


def mini_max_sum(arr):
	sorted_arr = sorted(arr)
	min_sum = sum(sorted_arr[:-1])
	max_sum = sum(sorted_arr[1::])
	print(min_sum, max_sum)


if __name__ == '__main__':
	arr = [1, 3, 5, 7, 9]
	mini_max_sum(arr)
