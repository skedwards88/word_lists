
wiki = []
with open("processed/wiki_stripped.txt", "r") as file:
  for line in file:
    wiki.append(line.strip())

gutenberg = []
with open("processed/gutenberg_processed.txt", "r") as file:
  for line in file:
    gutenberg.append(line.strip())

movies = []
with open("processed/movies_processed.txt", "r") as file:
  for line in file:
    movies.append(line.strip())

wordnik = []
with open("raw-ish/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())


common = list(set(wiki).intersection(gutenberg).intersection(wordnik))

with open("common/common_wiki_gutenberg_wordnik.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")

commonGutenbergWordnik = list(set(gutenberg).intersection(wordnik))

with open("common/common_gutenberg_wordnik.txt", "w") as file:
  for word in commonGutenbergWordnik:
    file.writelines(f"{word}\n")

commonMovieGutenbergWordnik = list(set(movies).intersection(gutenberg).intersection(wordnik))

with open("common/common_movie_gutenberg_wordnik.txt", "w") as file:
  for word in commonMovieGutenbergWordnik:
    file.writelines(f"{word}\n")

### Find words that appear on at least two of wiki/movie/guten?