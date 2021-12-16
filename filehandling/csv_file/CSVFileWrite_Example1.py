import csv

with open('emp.csv', 'w',newline='') as file:
    csvWriter = csv.writer(file)
    csvWriter.writerow(['Name','Age','Phone','Email'])
    data = [
        ['Ram','32', '1234','anji@gmail.com'],
        ['Sunny','32', '1234','anji@gmail.com'],
        ['Bunny','32', '1234','anji@gmail.com']
    ]
    csvWriter.writerows(data)
    print("Done")
