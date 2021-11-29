file = input("Enter file:")
if len(file) < 1:
    file = "mbox-short.txt"
handle = open(file)
count = dict()
for line in handle:
    wlist = line.split()
    if line.startswith("From:"):
        name = wlist[1]
        count[name] = count.get(name, 0) + 1
lst = list()
for value,key in count.items ():
    lst.append ((key,value))
lst.sort(reverse = True)
for key,value in lst:
    print (value,key)
