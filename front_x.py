#B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
#def front_x(words):
  # +++your code here+++
words = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
xstring_lst = []
cnt = 0
words_sort1 = sorted(words)
print 'this the 1st sorted words: ', words_sort1

for string in words_sort1:
	char_fst = string[0]
    if (char_fst == 'x')
      xstring_lst += words_sort1.pop(cnt)
    cnt += 1
xstring_lst = sorted(xstring_lst)
words_final = xstring_lst + words_sort1
print 'this is the final sortd words: ', words_final

