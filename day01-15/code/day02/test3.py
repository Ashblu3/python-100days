def t3(year):
	if year % 4 != 0:
		return False
	else:
		if year % 100 != 0:
			return True
		else:
			if year % 400 == 0:
				return True
			else:
				return False



year = int(input('year = '))
if t3(year):
	print("%d is Leap year" % (year))
else:
	print("%d isn't Leap year" % (year))
