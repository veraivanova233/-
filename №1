f = open("/Users/veraivanova/Downloads/names.txt", 'r')
f1 = f.readlines()
names = []
for line in f1:
    for name in line.split("\",\""):
        names.append(name)
names[0] = names[0][1:]
names[-1] = names[-1][1:-1]
names = sorted(names)
alph = 'abcdefghijklmnopqrstuvwxyz'
names_sums = []
for name in names:
    num = 0
    for let in name:
        num += alph.index(let.lower()) + 1
    names_sums.append(num)
res = 0
for i in range(len(names_sums)):
    res += names_sums[i] * (i+1)
print(res)
f.close()

# Ответ: 871895359
