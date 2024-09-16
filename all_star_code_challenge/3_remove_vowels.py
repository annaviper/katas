# https://www.codewars.com/kata/58640340b3a675d9a70000b9/train/python


def remove_vowels(strng):
	characters = [i for i in strng if i not in "aeiou"]
	return "".join(characters)


if __name__ == '__main__':
	s = ("drake")
	result = remove_vowels(s)
	print(result)
