print  "\t\t\t\tRules"
print """\n 1.You have to drink either of 1,2,3 or 4 vodka shots\n 2.There are in all 21 vodka shots.\n 3.You have to drink vodka shots in alternate with computer.\n 4.The person to drink the 21st shot dies\n\n."""
name=raw_input("Enter your name: ")
sum=0
while sum<21:
	a=int(raw_input("How many shots are you drinking ?? "))
	b=5-a
	print "Computer drank "+str(b)+" shots"
	sum=a+b+sum
if sum==21:
	print name+" Loose"

