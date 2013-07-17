# !usr/bin/python

import fileinput

def main():
	print "This program will count the number of vowels in a string or in a file."
	print "Press 1 if you want to enter a string. "
	print "Press 2 if you want to open a file.    "		
	a=raw_input("Enter your choice > ")
# 2 cases are possible according to the choice of user. he may want to open a file or he may want to enter a string
	if a=="1":
		content=raw_input("Enter string: ")
	elif a=="2":
		b=raw_input("Enter File name: ")
		content=open(b).readlines()
		content=''.join(content)
	l=len(content)		#to find the length of the string or file 
#making all characters uppercase to make search easier and better
	content=content.upper()	
#variable to count the no=umber of vowels
	count=0	
	for i in range(0,l):
		if content[i]=="A" :
			count=count+1
                if content[i]=="E" :
                        count=count+1
                if content[i]=="I" :
                        count=count+1
                if content[i]=="O" :
                        count=count+1
                if content[i]=="U" :
                        count=count+1

	print "Number of vowels in ="+str(count)

if __name__=="__main__":
	main()
