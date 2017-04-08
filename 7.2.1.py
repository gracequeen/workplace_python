fname=raw_input("Enter file name: ")
fh=open(fname)
count=0
spam=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    line=line.rstrip()
    count=count+1
    
    if spam == 0:
        spam=float(line[19:])    
    else:
        spam=spam+float(line[19:])

avg=spam/count
print"Average spam confidence:",avg