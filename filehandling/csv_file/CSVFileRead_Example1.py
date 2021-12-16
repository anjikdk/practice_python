import csv

with open('emp.csv','r') as file:
    csvReader = csv.reader(file)
    data = list(csvReader)
    # print(data)
    for row in data:
        # print(row)
        for column in row:
            print(column,'\t',end='')
        print()
