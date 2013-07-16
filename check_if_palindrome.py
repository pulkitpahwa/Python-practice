a=raw_input("Enter a string to check whether it is pallindrome or not: ")
l=len(a)-1
c=[]
while l>=0:
	c.append(a[l])
	l=l-1
	
reverse_string=''.join(c)
print reverse_string
if reverse_string==a:
	print "pallindrome"
else:
	print "not pallindrome"
