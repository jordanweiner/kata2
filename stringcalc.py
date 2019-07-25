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
    
  if (noNegatives(cleanString)):
    numList = [int(c) for c in cleanString]   # turn string to list of ints
    return sum(numList)

def noNegatives(string):
  negList = []
  if '-' not in string:
    return 1

  for i, c in enumerate(string):
    if (c == '-'):
      negList.append("-" + string[i+1])

  exceptionStr = "negatives not allowed: " + " ".join(negList)
  raise Exception(exceptionStr)
  return 0
