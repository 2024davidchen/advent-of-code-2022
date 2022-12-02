inputFile = open("day2-input.txt", "r")
points = 0
for line in inputFile:
  if (line(2) == 'X'):
    points += 1
  if (line(2) == 'Y'):
    points += 2
  if (line(2) == 'Z'):
    points += 3
  if (line == "A Y" || line == "B Z" || line == "C X"):
    points += 6
  if (line == "A X" || line == "B Y" || line == "C Z"):
    points += 3
