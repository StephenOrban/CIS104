fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    linelst = list()
    linelst = line.split()
    for word in linelst:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
