# Part 1
inputFile = open("day2-input.txt", "r")
points = 0
for line in inputFile:
  if (line[2] == 'X'):
    points += 1
  if (line[2] == 'Y'):
    points += 2
  if (line[2] == 'Z'):
    points += 3
  if ((line[0] == 'A' and line[2] == 'Y') or (line[0] == 'B' and line[2] == 'Z') or (line[0] == 'C' and line[2] == 'X')):
    points += 6
  if ((line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Y') or (line[0] == 'C' and line[2] == 'Z')):
    points += 3
print(points)

# Part 2
inputFile = open("day2-input.txt", "r")
points = 0
for line in inputFile:
  if (line[2] == 'X'):
    if (line[0] == 'A'):
      points += 3
    if (line[0] == 'B'):
      points += 1
    if (line[0] == 'C'):
      points += 2
  if (line[2] == 'Y'):
    points += 3
    if (line[0] == 'A'):
      points += 1
    if (line[0] == 'B'):
      points += 2
    if (line[0] == 'C'):
      points += 3
  if (line[2] == 'Z'):
    points += 6
    if (line[0] == 'A'):
      points += 2
    if (line[0] == 'B'):
      points += 3
    if (line[0] == 'C'):
      points += 1
print(points)