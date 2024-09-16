# https://www.codewars.com/kata/5864152183f7e6e834000160/train/python

import random


def random_movie(movies):
	return random.choice(movies)


if __name__ == '__main__':
	rocky_series = ["Rocky", "Rocky II", "Rocky III", "Rocky IV"]
	result = random_movie(rocky_series)
	print(result)
