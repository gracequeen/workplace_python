#create the handle-file and open it
fname=raw_input("Enter file name:")
fh=open(fname)
#create an empty list
lst=list()

for line in fh:
#create the words list for each line
    line=line.rstrip()
    words=line.split()
#check if each word is already in lst
    for i in range(len(words)):
        word=words[i]
        #print 'the ith word: ',i,word
        if word not in lst:
            lst.append(word)
    
lst.sort()
print lst
