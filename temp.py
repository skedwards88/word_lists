a=[1,2,3]
b=[2,3,4,5]
c=[2,3,6]

print(list(set(a).intersection(b)))
print(list(set(a).intersection(b).intersection(c)))

print(list(set(a).symmetric_difference(b)))


commonOld = []
with open("common.txt", "r") as file:
  for line in file:
    commonOld.append(line.strip())

commonNew = []
with open("common_wiki_gutenberg_wordnik.txt", "r") as file:
  for line in file:
    commonNew.append(line.strip())

common = list(set(commonOld).symmetric_difference(commonNew))

with open("temp.txt", "w") as file:
  for word in common:
    file.writelines(f"{word}\n")