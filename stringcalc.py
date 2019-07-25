def add(numbers):
  cleanString = ""
  numList = []
  if (numbers.startswith("//")):
    # find delimiter
    delim = numbers[2:(numbers.find('\n'))]
    # clean numbers string
    cleanString = numbers.replace(delim, "0").replace("//", "0").replace("\n", "0")
  else:
    # clean numbers string
    cleanString = numbers.replace(",", "0").replace("\n", "0")
    
  numList = [int(c) for c in cleanString]   # turn string to list of ints
  return sum(numList)