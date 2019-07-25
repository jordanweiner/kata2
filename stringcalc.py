def add(numbers):
  cleaned = ""
  numList = []
  if (numbers.startswith("//")):
    # find delimiter
    delim = numbers[2:(numbers.find('\n'))]
    # clean numbers string
    cleaned = numbers.replace("//", "").replace("\n", "").split(delim)
  else:
    # clean numbers string
    cleaned = list(numbers.replace(",", "").replace("\n", ""))
    # turn string to list of ints
    
  if (noNegatives(cleaned)):
    # if empty string, turn it into a 0
    numList = [(int(c) if c != "" else 0) for c in cleaned] 
    return sum(numList)

def noNegatives(cleaned):
  negList = []
  noNeg = True
  for i, c in enumerate(cleaned):
    if ('-' in c):
      negList.append(c)
      noNeg = False

  if (noNeg == False):
    exceptionStr = "negatives not allowed: " + " ".join(negList)
    raise Exception(exceptionStr)
  return noNeg
