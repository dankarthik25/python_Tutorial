import csv
import os

#
#       WRITING USING READER (csv.writer.writerow)
#
with open('name.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('copy_name.csv', 'w') as copy_file:
        csv_writer = csv.writer(copy_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
#
#       WRITING USING DICT READER
#


with open('name.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    os.remove("copy_name.csv")

    with open('copy_name.csv', 'w') as new_file:
        field_nms = ['first_name', ' last_name', ' email']
        # field_nms = ['first name', 'last name']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_nms, delimiter='\t')

        csv_writer.writeheader()      # Wrtie field names

        for line in csv_reader:
            # del line[' email']
            csv_writer.writerow(line)   # Write names
