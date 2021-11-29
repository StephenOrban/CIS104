import re
handle = open("mbox-short.txt")
count = list()
for line in handle:
    expression = re.findall ("^New Revision: ([0-9]+)",line)
    if len (expression) > 0:
        expression[0] = int (expression[0])
        count.append (expression[0])
print (int (sum(count)/len(count)))
