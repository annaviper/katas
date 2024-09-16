"""
Given a list of numbers
with an odd number of elements,
find the median.

Example:
lst = [5, 3, 1, 2, 4]
find_median(lst) --> returns 3
"""


def find_median(lst: list) -> int:
	sorted_list = sorted(lst)
	return sorted_list[int(len(sorted_list) / 2)]


if __name__ == '__main__':
	arr = [5, 3, 1, 2, 4]
	result = find_median(arr)
	print(result)
