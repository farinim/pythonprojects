##Given an integer input, check if the number is a pallindrome, without making use of strings
def pallindrome(x):
	if(x<10):
		return "Y"
	else:
		r=x%10
		y=x
		i=0
		while(y>10):
			i += 1
			y /= 10
		if(y == r):
			z = x - y*pow(10,i)
			z /=  10
			#print "y =", y,"r=",r,"z=",z			
			return pallindrome(z)
		else:
			return "N"

print "1234 is a pallindrome ?", pallindrome(1234)
print "12321 is a pallindrome ?", pallindrome(12321)