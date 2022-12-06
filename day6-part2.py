inputFile = open("day6-input.txt", "r")
inputString = inputFile.readlines()[0]

def checkRepeats(string):
  result = False
  for x in string:
    if (string.count(x) > 1):
      result = True
      break
  return result

i = 13
noRepeats = False
while (not noRepeats):
  i += 1
  packet = inputString[i - 14 : i]
  noRepeats = not checkRepeats(packet)

print(i)
