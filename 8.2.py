fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line=line.rstrip()
    if not line.startswith('From'):
        continue
    elif line.startswith('From:'):
        continue
    words=line.split()
    
    count=count+1
    email=words[1]
    print email
    
    

print "There were", count, "lines in the file with From as the first word"
