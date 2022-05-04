import json

def getCommonWords():

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

  notActuallyCommon = []
  with open("compiled/notActuallyCommon.txt", "r") as file:
    for line in file:
      notActuallyCommon.append(line.strip())

  notActuallyUncommon = []
  with open("compiled/notActuallyUncommon.txt", "r") as file:
    for line in file:
      notActuallyUncommon.append(line.strip())

  gutenbergWiki = list(set(gutenberg).intersection(set(wiki)))
  common = list(set(gutenbergWiki).union(set(movies)).union(set(notActuallyUncommon)))
  culledCommon = list(set(common).difference(set(notActuallyCommon)))
  culledCommon.sort()
  culledCommon.sort(key=len)

  return culledCommon

def getAllWords():
  wordnik = []
  with open("raw/wordnik.txt", "r") as file:
    for line in file:
      wordnik.append(line.strip())

  return wordnik

def writeWords(path, words):
  with open(path, "w") as file:
    json.dump(words, file)

common = getCommonWords()
all = getAllWords()
uncommon = list(set(common).symmetric_difference(set(all)))
uncommon.sort()
uncommon.sort(key=len)

writeWords("compiled/commonWords.json", common)
writeWords("compiled/uncommonWords.json", uncommon)
