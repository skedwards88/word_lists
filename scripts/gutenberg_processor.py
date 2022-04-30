wordnik = []
with open("raw-ish/wordnik.txt", "r") as file:
  for line in file:
    wordnik.append(line.strip())

gutenberg = []
with open("raw-ish/gutenberg.txt", "r") as file:
  for line in file:
    word = line.strip()
    if not word.isalpha():
      continue
    gutenberg.append(word.upper())


common = list(set(gutenberg).intersection(wordnik))

with open("common/wordnik/common_gutenberg_wordnik.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")

# with open("raw-ish/gutenberg.txt", "r") as file, open("processed/gutenberg_processed.txt", "w") as outfile:
#   for line in file:
#     word = line.strip()
#     if not word.isalpha():
#       continue
#     outfile.writelines(f'{word.upper()}\n')
