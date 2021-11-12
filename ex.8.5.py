fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
lst = list()
count = 0
for line in fh:
    if line.startswith("From:"):
        linelst = list()
        linelst = line.split()
        lst.append(linelst[1])
        count = count + 1
for word in lst:
    print(word)

print("There were", count, "lines in the file with From as the first word")
