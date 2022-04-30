# The "easy" list consists of:
# - words that are on common to wordnik, wiki, and gutenberg
# - words that are common to wordnik and movies

gutenberg = []
with open("processed/gutenberg.txt", "r") as file:
  for line in file:
    gutenberg.append(line.strip())

wiki = []
with open("processed/wiki.txt", "r") as file:
  for line in file:
    wiki.append(line.strip())

movies = []
with open("processed/movies.txt", "r") as file:
  for line in file:
    movies.append(line.strip())

gutenbergWiki = list(set(gutenberg).intersection(set(wiki)))
easy = list(set(gutenbergWiki).union(set(movies)))

with open("compiled/easy.txt", "w") as file:
  for word in easy:
    file.writelines(f"{word}\n")

# The "noneasy" list consists of all of the wordnik words that are not on the easy list

wordnik = []
with open("raw/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

noneasy = list(set(easy).symmetric_difference(set(wordnik)))

with open("compiled/noneasy.txt", "w") as file:
  for word in noneasy:
    file.writelines(f"{word}\n")
