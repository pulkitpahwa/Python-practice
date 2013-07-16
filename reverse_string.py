a=raw_input("Enter a string: ")
l=len(a)-1
c=[]
while l>=0:
	c.append(a[l])
	l=l-1

print ''.join(c)

