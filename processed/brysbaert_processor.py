wordnik = []
with open("processed/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

minPKnown = 0.96
brysbaert = []
with open("raw/brysbaert.txt", "r") as inFile:
  for line in inFile:
    word, pKnown = line.split(",")[:2]
    if float(pKnown) < minPKnown:
      break
    brysbaert.append(word.upper())

common = list(set(brysbaert).intersection(set(wordnik)))
common.sort()

with open("processed/brysbaert.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")
