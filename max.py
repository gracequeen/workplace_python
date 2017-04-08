largest = None
smallest = None


    
while True:
    num = raw_input("Enter a number: ")
   
    largest=max(num,largest)
    smallest=min(num,smallest)
    if num == "done" : break
    print num
    largest=num
    smallest=num
     try:
        t=int(num)
    except:
        print "please enter the integer number"
    
print "Maximum is", largest
print "Minimum is", smallest
