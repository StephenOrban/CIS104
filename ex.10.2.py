name = input("Enter file:")
if len(name) == 0:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if line.startswith ("From "):
        words = line.split ()
        time = words [5]
        time = time [:2]
        count [time] = count.get (time, 0) + 1
lst = list()
for key,value in count.items ():
    lst.append ((key,value))
lst.sort()
for key,value in lst:
    print (key,value)
