## program to edit a given file without actually opening the file in graphical mode

import fileinput, sys
input=raw_input("enter filename: ")
for line in fileinput.input(input, inplace=True):
line = line.replace(line_to_be_replaced,line_to_be_replaced_by)
    # sys.stdout is redirected to the file
    sys.stdout.write(line)
