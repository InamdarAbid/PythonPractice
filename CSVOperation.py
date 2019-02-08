import csv
with open('CSVdata.csv') as CSVFile:
    read = csv.reader(CSVFile,delimiter = ',')
    dates = []
    colors = []
    for row in read:
        print(row)
        date = row[0]
        color = row[1]
        dates.append(row[0])
        colors.append(row[1])
    print(dates)
    print(colors)