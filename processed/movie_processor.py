wordnik = []
with open("raw/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

movies = []
with open("raw/movies.txt", "r") as inFile:
  for line in inFile:
    word = line.strip()
    if not word.isalpha():
      continue
    movies.append(word.upper())

common = list(set(movies).intersection(set(wordnik)))

with open("processed/movies.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")
