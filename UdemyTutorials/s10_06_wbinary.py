a= 65524    # FF FE
b= 65535    # FF FF
c= 65536    # 00 01 00 00
x= 2998302  # 02 2D C0 1E

with open("binay2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2,'big'))
    bin_file.write(b.to_bytes(2,'big'))
    # bin_file.write(c.to_bytes(2,'big'))
    bin_file.write(c.to_bytes(4,'big'))
    bin_file.write(x.to_bytes(4,'big'))
    bin_file.write(x.to_bytes(4,'little'))


with open("binay2","br") as bin_file:
    e = int.from_bytes(bin_file.read(2),'big')
    print (e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print (f)
    # g = int.from_bytes(bin_fiels(2), 'big')
    # print (g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print (h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print (i)
    j = int.from_bytes(bin_file.read(4), 'big')
    print (j)

# Error when read little to big it show as error