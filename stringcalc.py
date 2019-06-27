def add(numbers):
	sum = 0
	if (numbers == ""):
		return sum;
	else:
		# go thru chars in string
		for n in numbers:
			if ((n == "\n") or (n == ",")):
				continue
			else:
				sum = sum + int(n, 10)
		return sum
