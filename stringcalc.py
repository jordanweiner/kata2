def add(numbers):
  cleaned = ""

  if (numbers.startswith("//")):
    delim = ""
    delimArray = []
    toReplace = ["//", "\n", "[", "]"]
    cleanedStr = numbers

    numbersWithDelim = numbers
    while (numbersWithDelim.find("[") != -1):
      # add delimeter to delimeter aray
      toReplace.append(numbersWithDelim.split('[')[1].split(']')[0])
      # cut that delimeter out of string
      numbersWithDelim = numbersWithDelim[(numbersWithDelim.find(']') + 1):]
    
    for delim in toReplace:
      cleanedStr = cleanedStr.replace(delim, ",")
    cleaned = cleanedStr.split(",")

  else:
    # clean numbers string
    cleaned = list(numbers.replace(",", "").replace("\n", ""))
    
  # turn string to list of ints
  numList = []
  if (noNegatives(cleaned)):
    numList = [stringToInt(c) for c in cleaned] 
    print("\n" + str(sum(numList)))
    return sum(numList)

# if empty string, turn it into a 0
# otherwise, return the int version if it's not over 1000
def stringToInt(c):
  if (c != "" and int(c) <= 1000):
    return int(c)
  return 0

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
