wordnik = []
with open("raw-ish/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

wiki = []
with open("raw-ish/enwiki-20210820-words-frequency.txt", "r") as file:
  for line in file:
    word = line.split(" ")[0]
    if not word.isalpha():
      continue
    if " 1000\n" in line:
      break
    wiki.append(word.upper())


common = list(set(wiki).intersection(wordnik))

with open("common/wordnik/common_wiki_wordnik.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")

# with open("raw-ish/enwiki-20210820-words-frequency.txt", "r") as file, open("processed/wiki_stripped.txt", "w") as outfile:
#   for line in file:
#     word = line.split(" ")[0]
#     if not word.isalpha():
#       continue
#     if " 1000\n" in line:
#       break
#     outfile.writelines(f'{word.upper()}\n')
