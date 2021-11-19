file = input("Enter file:")
if len(file) < 1:
    file = "mbox-short.txt"
handle = open(file)
counts = dict()
for line in handle:
    wlist = line.split()
    if line.startswith("From:"):
        name = wlist[1]
        counts[name] = counts.get(name, 0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print (bigword, bigcount)
