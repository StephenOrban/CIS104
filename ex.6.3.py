def lcount(word,character):
    count = 0
    for letter in word:
        if letter == character:
            count = count + 1
    print(count)
lcount("banana","n")
lcount("pineapple","p")
