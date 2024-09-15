import os

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def time_conversion(s):
	from datetime import datetime

	return str(datetime.strptime(s, '%I:%M:%S%p').time())


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	s = input()
	result = time_conversion(s)
	fptr.write(result + '\n')
	fptr.close()


"""MANUAL/BAD VERSION

def time_conversion(s: str) -> str:
	pm_map = {
		'01': '13',
		'02': '14',
		'03': '15',
		'04': '16',
		'05': '17',
		'06': '18',
		'07': '19',
		'08': '20',
		'09': '21',
		'10': '22',
		'11': '23',
	}

	am_map = {
		'12': '00'
	}

	hour = s[:2]
	if s.endswith('PM') and pm_map.get(hour) is not None:
		new_hour = pm_map[hour]
		s = s.replace(hour, new_hour)
	elif am_map.get(hour) is not None:
		new_hour = am_map[hour]
		s = s.replace(hour, new_hour)

	return s[:-2]
"""