inputFile = open("day6-input.txt", "r")
inputString = inputFile.readLines()[0]

i = 4
boolean noRepeats = False
while (not noRepeats):
  packet = inputString[i - 4 : i]
  i += 1
  noRepeats = not checkRepeats(packet)

def checkRepeats(string):
  result = false
  for x in string:
    if (string.count(x) > 1):
      result = true
      break
  return result

print(i)
