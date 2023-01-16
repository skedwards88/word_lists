root = "src/common/wordLists/"

wordnik = []
with open(f"{root}raw/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

offensive = []
with open(f"{root}raw/LDNOOBW.txt", "r") as file:
  for line in file:
    offensive.append(line.strip().upper())

minusOffensive = list(set(wordnik).difference(set(offensive)))
minusOffensive.sort()

with open(f"{root}processed/wordnik.txt", "w") as file:
  for word in minusOffensive:
    file.writelines(f"{word}\n")
