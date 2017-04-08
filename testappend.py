
line='I don\'t know why I always get the none'
words=line.split()
print 'words:',words,'type',type(words),'length',len(words)

lst=list()
print 'lst:',lst,type(lst)
word=words[6]
print 'word:',word,type(word)
lst.append(word)
word1=words[5]
lst.append(word1)
print 'new lst:',lst,type(lst)

lst.sort()
print'the sorted lst:',lst,type(lst)
"""
word1='link'
lst1=list()
print 'word1',word1,type(word1)
print 'lst1',lst1,type(lst1)

lst1.append(word1)
print 'lst1',lst1,type(lst1)

lst2=list()
lst2.append('link')
print 'link',type('link')
print 'lst2',lst2, type(lst2)
"""

