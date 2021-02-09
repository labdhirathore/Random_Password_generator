#Mini Project

from random import randint
#All lowercase password
password = ""
for i in range(10):
    i = chr(randint(65,90)).lower()
    password= str(password)+i
print(password)
#All uppercase password
password = ""
for i in range(10):
    i = chr(randint(65,90))
    password= str(password)+i
print(password)

# upper and lower password
password = ""
for i in range(10):
    i = chr(randint(65,90))
    for j in range(5):
        j = chr(randint(65,90)).lower()
    password= str(password)+ i + j
print(password)
