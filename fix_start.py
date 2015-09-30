
  # +++your code here+++
s='babble'
startchar=s[0]
print 'start char is '+startchar

srep=s.replace(startchar,'*')
print 'srep is '+srep

snew=startchar+srep[1:]
print 'new s is '+snew
