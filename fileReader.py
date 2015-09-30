
dictA = {}
count = 0
fileX = open('wordtest.txt', 'rU')

for line in fileX:
	fileWord = line.split()
	for word in fileWord:
	#print 'the word now is: ', word
	#print word is str
		word = word.lower()
		if word not in dictA:
			dictA[word] = 1
		else:
			dictA[word] += 1


print 'the dict is: ', dictA
print 'the keys are: ', dictA.keys()

cnt = 0
for key in dictA.keys():
	cnt += 1
print cnt




