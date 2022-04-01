with open("enwiki-20210820-words-frequency.txt", "r") as file, open("wiki_stripped.txt", "w") as outfile:
  for line in file:
    word = line.split(" ")[0]
    if not word.isalpha():
      continue
    if " 500\n" in line:
      break
    outfile.writelines(f'{word.upper()}\n')
