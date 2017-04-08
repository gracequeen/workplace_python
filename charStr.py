print "Python working properly..."

rangelist = range(10) 
print rangelist
for number in rangelist:
	if number in (3, 4, 7, 9):
		break
	else:
		continue
else:
	pass

if rangelist[1] == 2:
	print "the second is 2"
elif rangelist[1] == 3:
	print "the second is 3"
else:
	print "Dunno"

while rangelist[1] == 1:
	pass