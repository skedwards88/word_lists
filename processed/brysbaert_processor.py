wordnik = []
with open("processed/wordnik.txt", "r") as file:
    for line in file:
        wordnik.append(line.strip())

minCommonPKnown = 0.96
maxUncommonPKnown = 0.50
brysbaertCommon = []
brysbaertUncommon = []
with open("raw/brysbaert.txt", "r") as inFile:
  for line in inFile:
        word, pKnown = line.split(",")[:2]
        if float(pKnown) >= minCommonPKnown:
            brysbaertCommon.append(word.upper())
        if float(pKnown) <= maxUncommonPKnown:
            brysbaertUncommon.append(word.upper())

common = list(set(brysbaertCommon).intersection(set(wordnik)))
uncommon = list(set(brysbaertUncommon).intersection(set(wordnik)))
common.sort()
uncommon.sort()

with open("processed/brysbaert.txt", "w") as file:
    for word in common:
        file.writelines(f"{word}\n")

with open("processed/brysbaertUncommon.txt", "w") as file:
    for word in uncommon:
        file.writelines(f"{word}\n")
