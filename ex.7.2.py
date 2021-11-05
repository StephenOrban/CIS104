fname = input("Enter file name: ")
fh = open(fname)
tvalue = 0
cvalue = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        ipos = line.find(':')
        piece = line[ipos+1:]
        value= float(piece)
        tvalue = tvalue + value
        cvalue = cvalue + 1
avalue = tvalue/cvalue
print("Average spam confidence:",avalue)
