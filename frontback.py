def front_back(a):
	if(len(a)%2 == 0):
		front_a = a[:len(a)/2]
    #back_a = a.strip(front_a)
  	else:
  		front_a = a[:(len(a)-1)/2+1]
  	
  	back_a = a.replace(front_a, '')
  	return 'front is: ', front_a, 'back is: ', back_a

print front_back('dictionary')
