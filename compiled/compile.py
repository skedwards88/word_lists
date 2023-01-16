import json

root = "src/common/wordLists/"

def getCommonWords():

  gutenberg = []
  with open(f"{root}processed/gutenberg.txt", "r") as file:
    for line in file:
      gutenberg.append(line.strip())

  wiki = []
  with open(f"{root}processed/wiki.txt", "r") as file:
    for line in file:
      wiki.append(line.strip())

  movies = []
  with open(f"{root}processed/movies.txt", "r") as file:
    for line in file:
      movies.append(line.strip())

  notActuallyCommon = []
  with open(f"{root}compiled/notActuallyCommon.txt", "r") as file:
    for line in file:
      notActuallyCommon.append(line.strip())

  notActuallyUncommon = []
  with open(f"{root}compiled/notActuallyUncommon.txt", "r") as file:
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
  with open(f"{root}processed/wordnik.txt", "r") as file:
    for line in file:
      wordnik.append(line.strip())

  return wordnik

def writeWords(path, words):
  with open(path, "w") as file:
    json.dump(words, file, indent=2)
    file.writelines("\n")

common = getCommonWords()
all = getAllWords()
uncommon = list(set(common).symmetric_difference(set(all)))
uncommon.sort()
uncommon.sort(key=len)

writeWords(f"{root}compiled/commonWords.json", common)
writeWords(f"{root}compiled/uncommonWords.json", uncommon)
