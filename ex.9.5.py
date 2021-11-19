file = input("Enter file:")
if len(file) < 1:
    file = "mbox-short.txt"
handle = open(file)
counts = dict()
for line in handle:
    wlist = line.split()
    if line.startswith("From:"):
        name = wlist[1]
        dpos = name.find ("@") + 1
        name = name[dpos:]
        counts[name] = counts.get(name, 0) + 1
print (counts)
