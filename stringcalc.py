def add(numbers):
	sum = 0
	for num in numbers:
		if ((num != '\n') and (num != ',')):
			sum += int(num)
	return sum

