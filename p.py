# searches the whole directory for files of particular extension and prints them
# can be used to move all the files or delete all the files of a particular extension etc.



import os
for r,d,f in os.walk("."):
    for files in f:
        if files.endswith(".html"):
             print os.path.join(r,files)
