# Part 1
elves = []
inputFile = open("day1-puzzle1-input.txt", "r")
tempElfCalories = 0
for line in inputFile:
    if (line != "\n"):
        tempElfCalories += int(line)
    else:
        elves.append(tempElfCalories)
        tempElfCalories = 0
print(max(elves))

# Part 2
topThree = 0
for i in range(3):
    topThree += max(elves)
    elves.remove(max(elves))
print("The top three total to: " + str(topThree))