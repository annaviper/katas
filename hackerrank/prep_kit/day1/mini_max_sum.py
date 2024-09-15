#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mini_max_sum(arr):
	sorted_arr = sorted(arr)
	min_sum = sum(sorted_arr[:-1])
	max_sum = sum(sorted_arr[1::])
	print(min_sum, max_sum)


if __name__ == '__main__':
	arr = list(map(int, input().rstrip().split()))
	mini_max_sum(arr)
