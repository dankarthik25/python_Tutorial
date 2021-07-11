import csv

############################
# Using CSV.READER
###########################

print('Using csv.reader \n')
with open('name.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")

# for name in names:
#     print(name)
html_output = ''
names = []
html_output += f'<p> There are currently {len(names)} public contributors. Thansk You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'<\n\t<li>{name} <li>'

html_output += '\n</ul>'


print(html_output)


############################
# Using CSV.DictReader
###########################

print('Using csv.DictReader')
with open('name.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    for line in csv_data:
        if line['first_name'] == 'No Reward':
            break
        names.append(f"{line['first_name']} {' last_name'}")

# for name in names:
#     print(name)

html_output += f'<p> There are currently {len(names)} public contributors. Thansk You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'<\n\t<li>{name} <li>'

html_output += '\n</ul>'


print(html_output)
