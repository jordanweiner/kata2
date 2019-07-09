def add(numbers):
	if (numbers == ""):
		return 0
	elif (len(numbers) == 1):
		return int(numbers)
	else:
		sum = 0
		for num in numbers:
			sum += int(num)
		return sum

