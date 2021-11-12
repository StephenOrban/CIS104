example = list()
def chop(lst):
    lst.pop(0)
    lst.pop(len(lst)- 1)
example = [1,2,4,6,7,9,123]
chop(example)
print(example)

def middle(lst):
    nlist = list()
    for number in lst:
        nlist.append(number)
    nlist.pop(0)
    nlist.pop(len(nlist)-1)
    return (nlist)
tlst = middle(example)
print(tlst)
print(example)
