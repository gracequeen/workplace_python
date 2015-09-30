words = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
xstring_lst = []
other_lst = []
cnt = 0
for string in words:
	print 'iteration', cnt, ':'
	if(string[0] == 'x'):
		#words.remove(string)
		xstring_lst.append(string)
		#print 'now words is: ', words
		print 'now xstring_lst is: ', xstring_lst
		
	else:
		other_lst.append(string)
		print 'no x in current string'
	cnt += 1

xstring_lst = sorted(xstring_lst) + sorted(other_lst)

print xstring_lst


