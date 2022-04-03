with open("gutenberg.txt", "r") as file, open("gutenberg_processed.txt", "w") as outfile:
  for line in file:
    word = line.strip()
    if not word.isalpha():
      continue
    outfile.writelines(f'{word.upper()}\n')
