def add(numbers):
	sum = 0
	for num in numbers:
		if (num != '\n'):
			sum += int(num)
	return sum

