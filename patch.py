#rawdata from https://www.contextures.com/xlsampledata01.html

# import csv

# with open('mycsv.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=' ')

#     for row in csv_reader:
#         print(row)


# exit()



f = open('rawdata.txt', 'r')
rawdata = f.readlines()
#rawdata = f.readline()
f.close()

# print(rawdata.replace("\n", ""))

# exit()
all = []
row = []
count = 0
for i in rawdata:
    if  i == "\n":
        continue
    
    if i != None and i != "\n":
        row.append(i.replace("\n", ""))
        count +=1

    if count >=7:
        count=0

    if count == 0:
        all.append(row)
        row = []
print(all)




# write to csv file
import csv

with open('mycsv.csv', mode='w', newline='') as mycsv:
    csv_writer = csv.writer(mycsv, delimiter=',')

    for i in all:
        csv_writer.writerow(i)



