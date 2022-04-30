wordnik = []
with open("raw-ish/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

movies = []
with open("raw-ish/movies.txt", "r") as file:
  for line in file:
    word = line.strip()
    if not word.isalpha():
      continue
    movies.append(word.upper())


common = list(set(movies).intersection(wordnik))

with open("common/wordnik/common_movie_wordnik.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")

# with open("raw-ish/movies.txt", "r") as file, open("processed/movies_processed.txt", "w") as outfile:
#   for line in file:
#     word = line.strip()
#     if not word.isalpha():
#       continue
#     outfile.writelines(f'{word.upper()}\n')
