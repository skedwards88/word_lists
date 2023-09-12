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

  brysbaert = []
  with open("processed/brysbaert.txt", "r") as file:
    for line in file:
      brysbaert.append(line.strip())

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

  # Take words that are included in Guttenburg AND wiki
  common = list(set(gutenberg).intersection(set(wiki)))
  # And words that are included in movies
  common = list(set(common).union(set(movies)))
  # And words that are included in brysbaert
  common = list(set(common).union(set(brysbaert)))
  # And words that are included in notActuallyUncommon
  common = list(set(common).union(set(notActuallyUncommon)))

  # Remove words from notActuallyCommon, sorted alphabetically then sorted by length
  culledCommon = list(set(common).difference(set(notActuallyCommon)))
  culledCommon.sort()
  culledCommon.sort(key=len)

  return culledCommon

def getAllWords():
  wordnik = []
  with open("processed/wordnik.txt", "r") as file:
    for line in file:
      wordnik.append(line.strip())

  return wordnik

def writeWords(path, words):
  with open(path, "w") as file:
    json.dump(words, file, indent=2)
    file.writelines("\n")

def writeWordsByLength(basePath, words):
  len2 = []
  len3 = []
  len4 = []
  len5 = []
  len6 = []
  len7 = []
  len8plus = []

  for word in words:
    if len(word) <= 2:
      len2.append(word)
    elif len(word) == 3:
      len3.append(word)
    elif len(word) == 4:
      len4.append(word)
    elif len(word) == 5:
      len5.append(word)
    elif len(word) == 6:
      len6.append(word)
    elif len(word) == 7:
      len7.append(word)
    else:
      len8plus.append(word)

  writeWords(f"{basePath}Len2.json", len2)
  writeWords(f"{basePath}Len3.json", len3)
  writeWords(f"{basePath}Len4.json", len4)
  writeWords(f"{basePath}Len5.json", len5)
  writeWords(f"{basePath}Len6.json", len6)
  writeWords(f"{basePath}Len7.json", len7)
  writeWords(f"{basePath}Len8plus.json", len8plus)

common = getCommonWords()
all = getAllWords()
uncommon = list(set(common).symmetric_difference(set(all)))
uncommon.sort()
uncommon.sort(key=len)

writeWords("compiled/commonWords.json", common)
writeWords("compiled/uncommonWords.json", uncommon)
writeWordsByLength("compiled/commonWords", common)
writeWordsByLength("compiled/uncommonWords", uncommon)
