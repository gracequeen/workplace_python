largest = None
smallest = None


    
while True:
    num = raw_input("Enter a number: ")
  
    if num == "done" : break
    largest=max(num,largest)
    if smallest is None:
        smallest=num
    elif smallest > num:
        smallest=num
    else:
        smallest=smallest
    
    largest=num
    
    try:
        t=int(num)
    except:
        print "Invalid input"
    
print "Maximum is", largest
print "Minimum is", smallest
