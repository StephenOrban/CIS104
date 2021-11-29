import re
name = input("Enter regular expression:")
handle = open("mbox-short.txt")
count = 0
for line in handle:
    expression = re.findall (name,line)
    if len (expression) > 0:
        count = count + 1
print ("the file had", count, "lines that matched", name)
