import datetime
try:
    now = datetime.datetime.now()
    age = int(input("enter your birthday : "))
    year = now.year
    rx = year - age
    print('your age is :',rx)
except ValueError:
    print("[-] please the program just take numbers")