try:
    pass
except Exception:
    pass
# else:
#     pass
# finally:
#     pass

try:
    f = open('textfile.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
    print("Sorry This file doesn't exisgt")
else:
    print(f.read())
    f.close()

finally:
    print('Executing Finallay.....')
