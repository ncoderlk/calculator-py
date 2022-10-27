def math(value):
    fh = open('history.txt', 'w')
    fh.write(value)
    fh.close()
    print(f"\n{value}\n")
    return eval(value)


def history():
    fh = open('history.txt', 'r')
    fr = fh.read()
    fh.close()
    print(fr, '=', eval(fr))


def start():
    print("\n-------Select The Option-------\n")
    print('\n1: Addition')
    print('2: Sustraction')
    print('3: Division')
    print('4: Multiplication')
    print('5: History')
    user_choice = str(input('\nEnter Your Choice:'))
    if user_choice != "5":
        if (user_choice == "1"):
            user_choice = "+"
        elif (user_choice == "2"):
            user_choice = "-"
        elif (user_choice == "3"):
            user_choice = "/"
        elif (user_choice == "4"):
            user_choice = "*"
        x = str(input('\nEnter the first number:'))
        y = str(input('\nEnter the second number:'))
        print(math(x+user_choice+y), "\n")
    else:
        history()


start()
