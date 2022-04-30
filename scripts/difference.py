
common = []
with open("common/common_wiki_gutenberg_wordnik.txt", "r") as file:
  for line in file:
    common.append(line.strip())

wordnik = []
with open("raw-ish/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

moviesWordnik = []
with open("common/wordnik/common_movie_wordnik.txt", "r") as file:
  for line in file:
    moviesWordnik.append(line.strip())

gutenbergWordnik = []
with open("common/wordnik/common_gutenberg_wordnik.txt", "r") as file:
  for line in file:
    gutenbergWordnik.append(line.strip())

difference = list(set(common).symmetric_difference(wordnik))

with open("common/uncommon_wordnik.txt", "w") as file:
  for word in difference:
    file.writelines(f"{word}\n")

# ###

commonMovieGutenbergWordnik = []
with open("common/common_movie_gutenberg_wordnik.txt", "r") as file:
  for line in file:
    commonMovieGutenbergWordnik.append(line.strip())

commonWikiGutenbergWordnik = []
with open("common/common_wiki_gutenberg_wordnik.txt", "r") as file:
  for line in file:
    commonWikiGutenbergWordnik.append(line.strip())

differenceWikiMovie = list(set(commonMovieGutenbergWordnik).symmetric_difference(commonWikiGutenbergWordnik))

with open("common/uncommon_wiki_movie.txt", "w") as file:
  for word in differenceWikiMovie:
    file.writelines(f"{word}\n")

###

movieGutenbergDifference = list(set(moviesWordnik).symmetric_difference(gutenbergWordnik))

with open("common/wordnik/uncommon_movies_gutenberd.txt", "w") as file:
  for word in movieGutenbergDifference:
    file.writelines(f"{word}\n")

###

movieVsRest = list(set(moviesWordnik).difference(common))

with open("common/wordnik/movies_vs_rest.txt", "w") as file:
  for word in movieVsRest:
    file.writelines(f"{word}\n")
