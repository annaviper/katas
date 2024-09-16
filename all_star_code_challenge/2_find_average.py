"""
allStars = [1, 9, 2, 8, 10]
findAverage(allStars) # => 30/5 = 6
"""


def find_average(all_stars):
	return sum(all_stars) / len(all_stars)


if __name__ == '__main__':
	all_stars = [1, 9, 2, 8, 10]
	find_average(all_stars)
