inputFile = open("day5-input.txt", "r")
lineList = inputFile.readlines()
supplies = [] # Initializes 2D array representing the supplies

# Split input into supplies and moves
newLineIndex = lineList.index("\n")
suppliesLines = lineList[:newLineIndex]
movesLines = lineList[newLineIndex + 1:]

# print(str(newLineIndex) + "\nSupplies: " + str(suppliesLines) + "\nMoves: " + str(movesLines))
suppliesLines.reverse() # Reverses it so that the top items are at the end of the list
supplyLabels = suppliesLines.pop(0) # removes the first line with the number labels
for character in supplyLabels:
    if (character != " " and character != "\n"):
        tempIndex = supplyLabels.index(character)
        tempList = []
        for line in suppliesLines:
            if (line[tempIndex] != " "):
                tempList.append(line[tempIndex])
        supplies.append(tempList)
supplyCopy = supplies

def move(start, end, moves):
    for i in range(moves):
        supplies[end].append(supplies[start].pop(-1))

    

def betterMove(start, end, moves):
    # print("Initial Start: " + str(supplies[start]))
    # print("Initial end: " + str(supplies[end]))
    splitIndex = len(supplies[start]) - moves
    tempList = supplies[start][splitIndex:]
    # print("!!!!!" + str(tempList))
    supplies[start] = supplies[start][:splitIndex]
    # print("?????" + str(supplies[start]))
    supplies[end].extend(tempList)
    # print("#####" + str(supplies[end]))

# Part 2
print("Part 2: ")
# Reset list
for line in movesLines:
    splitMove = line.split()
    # print("Split Move: " + str(splitMove))
    betterMove(int(splitMove[3]) - 1, int(splitMove[5]) - 1, int(splitMove[1])) # List indexes start at 0, while input starts at 1
    
for line in supplies:
    print(str(line))
# Part 1
# Removes spaces while splitting into list of words/numbers
supplies = supplyCopy
print("Part 1: ")
for line in movesLines:
    splitMove = line.split()
    move(int(splitMove[3]) - 1, int(splitMove[5]) - 1, int(splitMove[1])) # List indexes start at 0, while input starts at 1

for line in supplies:
    print(str(line))

