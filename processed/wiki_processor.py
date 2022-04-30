wordnik = []
with open("raw/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

wiki = []
with open("raw/wiki.txt", "r") as inFile:
  for line in inFile:
    word = line.split(" ")[0]
    if not word.isalpha():
      continue
    if " 1000\n" in line:
      break
    wiki.append(word.upper())

common = list(set(wiki).intersection(set(wordnik)))

with open("processed/wiki.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")
