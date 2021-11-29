import string
name = input("Enter file:")
if len(name) == 0:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    line = line.translate (str.maketrans ('','',string.punctuation))
    line = line.lower ()
    words = line.strip ()
    for word in words:
        letters = word.split ()
        for letter in letters:
            if letter.isalpha ():
                 count[letter] = count.get(letter, 0) + 1
lst = list()
for value,key in count.items ():
    lst.append ((key,value))
lst.sort(reverse = True)
for key,value in lst:
    print (value,key)
