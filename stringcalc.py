def add(numbers):
	if (numbers == ""):
		return 0
	else:
		sum = 0
		for num in numbers:
			sum += int(num)
		return sum

