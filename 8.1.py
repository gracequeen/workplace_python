fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    print words
    for i in range(len(words)):
        print range(len(words))
        if words[i] not in lst:
            lst=lst.append(words[i])
        else:
            continue
       
lst=lst.sort()
print lst
