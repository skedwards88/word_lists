terminalS = 0

with open("common/game/easy.txt", "r") as file:
  for line in file:
    word = line.strip()
    if word[-1] is "S":
        terminalS += 1

with open("common/game/noneasy.txt", "r") as file:
  for line in file:
    word = line.strip()
    if word[-1] is "S":
        terminalS += 1

print(terminalS)