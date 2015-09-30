import sys
import os

def List(dir):
	filenames = os.listdir(dir)
	print filenames

# Define a main() function
def main():
	List(sys.argv[1])

#call the function
if __name__=='__main__':
    main()
