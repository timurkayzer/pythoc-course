import csv

# with open('files/username.csv') as file:
#     reader = csv.reader(file, delimiter=';')
    
#     with open('files/new.csv', 'w') as new_csv:
#         writer = csv.writer(new_csv, delimiter='A')

#         for line in reader:
#             writer.writerow(line)

with open('files/username.csv') as file:
    reader = csv.DictReader(file,delimiter=';')

    with open('files/username_updated.csv', 'w') as file_upd:
        header = ["Username", "Identifier", "First name", "Last name"]
        writer = csv.DictWriter(file_upd,fieldnames=header)
        writer.writeheader()
        for line in reader:
            writer.writerow(line)