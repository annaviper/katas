# https://www.codewars.com/kata/586405a639c5abc2db0000e8/train/python

def get_college(strng):
	return strng['college']


if __name__ == '__main__':
	curry = {
		"fname": "Steph",
		"lname": "Curry",
		"number": 30,
		"team": "Warriors",
		"college": "Davidson"}
	result = get_college(curry)
	print(result)
