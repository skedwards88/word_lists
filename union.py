
wiki = []
with open("wiki_stripped.txt", "r") as file:
  for line in file:
    wiki.append(line.strip())

wordnik = []
with open("wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())


common = list(set(wiki).intersection(wordnik))

with open("common.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")