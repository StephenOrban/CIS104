fname = input("Enter file name: ")
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
fh = open(fname)
cvalue = 0
for line in fh:
    cvalue = cvalue + 1
print(cvalue)
