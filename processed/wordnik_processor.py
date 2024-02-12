wordnik = []
with open("raw/wordnik.txt", "r") as file:
    for line in file:
        wordnik.append(line.strip())

offensive = []
with open("raw/LDNOOBW.txt", "r") as file:
    for line in file:
        offensive.append(line.strip().upper())

minusOffensive = sorted(set(wordnik).difference(set(offensive)))

with open("processed/wordnik.txt", "w") as file:
    for word in minusOffensive:
        file.writelines(f"{word}\n")
