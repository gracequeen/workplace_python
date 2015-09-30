from operator import add, sub

def a_plus_abs_b(a, b):

    if b < 0:
        f = sub 
    else:
        f = add
    return f(a, b)

def a_plus_abs_b_test():
	assert a_plus_abs_b(2, 3) == 5, '2 + abs(3) should be 5'
	assert a_plus_abs_b(-2, 3) == 1, '-2 + abs(3) should be 1'

#print a_plus_abs_b(-2, 7)
a_plus_abs_b_test()