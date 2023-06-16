
shapeAtt = str(input("Enter shape and attribute: "))

match shapeAtt.split():
    case ["circle","area"]:
        print("circle area")
    case _:
        print("error")