"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example

`s = '12:01:00PM'`
Return '12:01:00'.

`s = '12:01:00AM`
Return '00:01:00'.

"""

import os


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