import csv

# read csv file

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # print(csv_reader)  # >>> object consisting of list of each_line

# >>> ['first_name','last_name','email'] ['John','Doe','john-doe@gmail.com']

    for line in csv_reader:
        print(line)
    # >>> ['first_name', 'last_name','email']
    # >>> ['John', 'Doe', 'john-doe@guseemail.com']
    # >>> ['mary','smith','smith-mary@gmail.com']
# To get only email of the person (line[2])  or only name (line[0], line[1])
        print(line[2].lstrip())     # To remove unwanted space's from begin and end  of  string
    # >>> ['email']
    # >>> [ 'john-doe@guseemail.com']
    # >>> ['smith-mary@gmail.com']
####################################################
# To Get only ['email']
    ###################################################
with open('name.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    print('The email address of persons are :')
    for line in csv_reader:
        print(line[2].lstrip())


#####
# Reading by useing DictReader
######

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print('The email of the person by DictReader')

    for line in csv_reader:
        print(line[' email'].strip())

# We can see line['email'] is more meaningful than line[2] because we can know what we are printing either first name,last name or email
