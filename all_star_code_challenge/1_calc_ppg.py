# https://www.codewars.com/kata/5863f97fb3a675d9a700003f/train/python

"""
Write a function, called sumPPG, that takes two NBA player
objects/struct/Hash/Dict/Class and sums their PPG

Examples:
	iverson = { 'team': '76ers', 'ppg': 11.2 }
	jordan =  { 'team': 'bulls', 'ppg': 20.2 }
	sum_ppg(iverson, jordan) # => 31.4
"""


def sum_ppg(player_one, player_two):
	return player_one['ppg'] + player_two['ppg']


if __name__ == '__main__':
	iverson = {'team': '76ers', 'ppg': 11.2}
	jordan = {'team': 'bulls', 'ppg': 20.2}
	sum_ppg(iverson, jordan)
