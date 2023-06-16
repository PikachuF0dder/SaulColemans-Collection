from random import randint

x = randint(1,5)

match int(x):
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("too high")
