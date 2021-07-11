

#
# with open("binary",'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i])) # if a int it will make to zer
#         # so we write in list


with open("binary",'bw') as bin_file:
    bin_file.write(range(17)) # if a int it will make to zer
        # so we write in list



with open("binary","br") as binFile:
    for b in binFile:
        print(b)