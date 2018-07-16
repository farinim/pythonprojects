#!/usr/bin/python
##Takes input from user: an integer
##Compares the digits in the user enter integer value and the same integer value multiplied by 2
##Prints whether the two integer values contain same digits.
##If no user input provided, the input is defaulted to 142857

import sys
	
def getDigits(x):
	digits = set(str(x))	
	return digits

def main():
	if len(sys.argv) == 1:
		x=142857
	else:
		#print sys.argv
		x = int(sys.argv[1])

	a = getDigits(x)
	b = getDigits(x*2)
		
	#print a,b
	#print a.symmetric_difference(b)
	#print a ^ b

	if len(a^b) == 0:
		print "Same digits in ",x," & ",x*2
	else:
		print x," & ", x*2,"do not have same digits"
	

main()
