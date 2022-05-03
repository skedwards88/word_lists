def getEasyWords():
  # The "easy" list consists of:
  # words that are on common to wordnik, wiki, and gutenberg
  # and words that are common to wordnik and movies
  # minus manually rejected words

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

  notActuallyEasy = []
  with open("compiled/notActuallyEasy.txt", "r") as file:
    for line in file:
      notActuallyEasy.append(line.strip())

  gutenbergWiki = list(set(gutenberg).intersection(set(wiki)))
  easy = list(set(gutenbergWiki).union(set(movies)))
  culledEasy = list(set(easy).difference(set(notActuallyEasy)))
  culledEasy.sort()

  return culledEasy

def getNonEasyWords():
  # The "noneasy" list consists of all of the wordnik words that are not on the easy list
  wordnik = []
  with open("raw/wordnik.txt", "r") as file:
    for line in file:
      wordnik.append(line.strip())

  easy = []
  with open("compiled/easy.txt", "r") as file:
    for line in file:
      easy.append(line.strip())

  noneasy = list(set(easy).symmetric_difference(set(wordnik)))
  noneasy.sort()

  return noneasy

def writeWords(path, words):
  with open(path, "w") as file:
    for word in words:
      file.writelines(f"{word}\n")


easy = getEasyWords()
writeWords("compiled/easy.txt", easy)
nonEasy = getNonEasyWords()
writeWords("compiled/noneasy.txt", nonEasy)
