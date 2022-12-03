inputFile = open("day3-input.txt", "r")

charDict = {}
# Generates Dictionary
for i in range(26):
    charDict[(chr(ord('a') + i))] = (i + 1)
for i in range(26):
    charDict[(chr(ord('A') + i))] = (i + 27)

# Part 1
def splitCompartment(line):
    return int(len(line) / 2)
result = 0
for line in inputFile:
    compartmentLength = splitCompartment(line)
    firstHalf = line[:compartmentLength]
    secondHalf = line[compartmentLength:]
    found = -1
    for character in firstHalf:
        found = secondHalf.find(character)
        if (found != -1):
            result += charDict[character]
            break
print(result)

# Part 2
inputFile = open("day3-input.txt", "r")
result = 0
lineList = inputFile.readlines()
for i in range(int(len(lineList) / 3)):
    index = i * 3
    firstElf = lineList[index]
    secondElf = lineList[index + 1]
    thirdElf = lineList[index + 2]
    for character in firstElf:
        if (secondElf.find(character) != -1 and thirdElf.find(character) != -1):
            result += charDict[character]
            break
print(result)