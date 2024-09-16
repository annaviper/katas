# https://www.codewars.com/kata/58641f6eb359c4611c0001f2/train/python

import random


def is_palindrome(s):
	return s == s[::-1]


if __name__ == '__main__':
	word = "billy"
	result = is_palindrome(word)
	print(result)
