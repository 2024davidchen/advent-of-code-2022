inputFile = open("day6-input.txt", "r")
inputString = inputFile.readLines()[0]

def checkRepeats(string):
  result = false
  for x in string:
    if (string.count(x) > 1):
      result = true
      break
  return result

i = 3
noRepeats = False
while (not noRepeats):
  i += 1
  packet = inputString[i - 4 : i]
  noRepeats = not checkRepeats(packet)

print(i)
