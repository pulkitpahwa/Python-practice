import csv
l = []

with open('newfile.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                    l.append([])
                    for num in range(0,16):
                            l[-1].append(row[num])
