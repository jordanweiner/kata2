def add(numbers):
  if (numbers == ""):
    return 0
  elif (len(numbers) < 2):
    return int(numbers)
  else:
    if (numbers[0] == '/' and numbers[1] == '/'):
      end = numbers.find('\n')
      delim = numbers[2:end]

      charsList = numbers[(end+1):].split(delim)
      numList = [int(c) for c in charsList]
      return sum(numList)
    else:
    	total = 0
    	for num in numbers:
    		if ((num != '\n') and (num != ',')):
    			total += int(num)
    	return total

