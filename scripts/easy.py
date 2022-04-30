both = []
with open("common/common_wiki_gutenberg_wordnik.txt", "r") as file:
  for line in file:
    both.append(line.strip())

with open("common/wordnik/common_movie_wordnik.txt", "r") as file:
  for line in file:
    word = line.strip()
    if not word.isalpha():
      continue
    both.append(word.upper())

bothUnique = set(both)

with open("common/game/easy.txt", "w") as file:
  for word in bothUnique:
    file.writelines(f"{word}\n")

###

wordnik = []
with open("raw-ish/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

difference = list(bothUnique.symmetric_difference(set(wordnik)))

with open("common/game/noneasy.txt", "w") as file:
  for word in difference:
    file.writelines(f"{word}\n")

