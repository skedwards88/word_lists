root = "src/common/wordLists/"

wordnik = []
with open(f"{root}processed/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

gutenberg = []
with open(f"{root}raw/gutenberg.txt", "r") as inFile:
  for line in inFile:
    word = line.strip()
    if not word.isalpha():
      continue
    gutenberg.append(word.upper())

common = list(set(gutenberg).intersection(set(wordnik)))
common.sort()

with open(f"{root}processed/gutenberg.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")
