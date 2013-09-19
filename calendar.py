a=int(raw_input("Enter date:   "))
month=int(raw_input("enter month : "))
year=int(raw_input("enter year: "))
print str(a)+"/"+str(month)+"/"+str(year)+" is :"
year=year-2000
a=a+year/4
def dayfinder(a):	
	if a%7==0:
		print "Friday"
	elif a%7==1:
		print "Saturday"
	elif a%7==2:
		print "Sunday"
	elif a%7==3:
		print "Monday"
	elif a%7==4:
		print "Tuesday"
	elif a%7==5:
		print "Wednesday"
	else :
		print "thursday"

if a>31:
	print "enter a valid date"
else:
	if month==1:
		a=a
	if month==2:
		a=a+31
	elif month==3:
		a=a+31+28
	elif month==4:
		a=a+31+28+31
	elif month==5:
		a=a+31+28+31+30
	elif month==6:
		a=a+31+28+31+30+31
	elif month==7:
		a=a+31+28+31+30+31+30
	elif month==8:
		a=a+31+28+31+30+31+30+31
	elif month==9:
		a=a+31+28+31+30+31+30+31+31
	elif month==10:
		a=a+31+28+31+30+31+30+31+31+30
	elif month==11:
		a=a+31+28+31+30+31+30+31+31+30+31
	elif month==12:
		a=a+31+28+31+30+31+30+31+31+30+31+30
	dayfinder(a)
 
	
	

