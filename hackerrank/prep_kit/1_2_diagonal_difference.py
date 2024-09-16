"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1 + 5 + 9 = 15
The right to left diagonal = 3 + 5 + 9 = 17
Their absolute difference is |15 - 17| = 2
"""


def diagonal_difference(array, number) -> int:
	left_to_right = 0
	left_counter = 0

	right_to_left = 0
	right_counter = n-1

	for i in range(n):
		left_to_right += array[left_counter][i]
		left_counter += 1

		right_to_left += array[i][right_counter]
		right_counter -= 1

	return abs(left_to_right - right_to_left)


if __name__ == '__main__':
	n = 3
	a = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
	result = diagonal_difference(a, n)
	print(result)
