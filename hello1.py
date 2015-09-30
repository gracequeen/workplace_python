import sys

def hello(name):
    if name == 'alice' or name == 'Nick':
        print 'alert: alice here'
        name = name + '?'
    else:
        print 'else'
    name = name + '!!!'
    print 'hello', name
    
# Define a main() function
def main():
    hello(sys.argv[1])

#call the function
if __name__=='__main__':
    main()
    
