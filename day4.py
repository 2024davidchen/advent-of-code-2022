def parseLine(line, part):
    firstElf = set()
    secondElf = set()
    commaIndex = line.find(',')
    firstHalf = line[:commaIndex]
    firstDashIndex = firstHalf.find('-')
    firstStart = int(firstHalf[:firstDashIndex])
    firstEnd = int(firstHalf[firstDashIndex + 1:])
    for i in range(firstStart, firstEnd + 1):
        firstElf.add(i)
    
    secondHalf = line[(commaIndex + 1):]
    secondDashIndex = secondHalf.find('-')
    secondStart = int(secondHalf[:secondDashIndex])
    secondEnd = int(secondHalf[secondDashIndex + 1:])
    # print(str(secondStart) + ", " + str(secondEnd))
    for i in range(secondStart, secondEnd + 1):
        secondElf.add(i)
    firstElf = set(firstElf)
    secondElf = set(secondElf)
    if part == 1:
        return (firstElf.issubset(secondElf) or secondElf.issubset(firstElf))
    else:
        return (firstElf.isdisjoint(secondElf) or secondElf.isdisjoint(firstElf))

inputFile = open("day4-input.txt", "r")
part1 = 0
part2 = 0
for line in inputFile:
    if parseLine(line, 1):
        part1 += 1
    if not (parseLine(line, 2)):
        part2 += 1
print("Part 1: " + str(part1) + "\nPart 2: " + str(part2))
