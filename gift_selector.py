import random

def main():
	print "\n\nWhat do you want to do ?? \n\tPress 1 to update some list of gift items?\n\tPress 2 to update shops for the gift items?\n\tPress 3 to search for gift items for a particular occasion?\n\tPress 4 to search for shops for purchasing gift items?\n\n"
	new_year=['Flowers','Bouqets','Roses','Antiques','Liquor','Beer']	
	birthdays=['Show piece','Flowers','Liquor','Garments','Fashion Accessories','Mobiles and tablets']


	a=raw_input("Enter your choice > ")
	if a=="3":
		print "\n\n\tPress 1 to look for New year gifts\n\tPress 2 for Birthdays"
		item=raw_input("Enter your choice > ")
		print "\n\n"
		if item=="1":
			for i in new_year:
				print i
		if item=="2":
			for i in birthdays:
				print i
		print "\n\n"
		
if __name__=="__main__":
	main()
