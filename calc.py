try:
    num = int(input('enter the first number : '))
    op = input('enter oprator : ')
    num2 = int(input('enter second number : '))

    if op == '+':
        print(num + num2)
    elif op == '-':
        print(num - num2)
    elif op == '*':
        print(num * num2)
    elif op == '/':
        if num2 != 0:
            print(num / num2)
        else:
            print("[-] It cannot be divided by zero")
    else:
        print("[-] The operation entered is invalid, please enter + or - or * or /")

except ValueError:
    print("[-] please the program just take numbers")