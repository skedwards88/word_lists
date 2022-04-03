
wiki = []
with open("wiki_stripped.txt", "r") as file:
  for line in file:
    wiki.append(line.strip())

gutenberg = []
with open("gutenberg_processed.txt", "r") as file:
  for line in file:
    gutenberg.append(line.strip())

wordnik = []
with open("wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())


common = list(set(wiki).intersection(gutenberg).intersection(wordnik))

with open("common_wiki_gutenberg_wordnik.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")