
shapeInput = str(input("Enter shape and attribute: "))
shapeAtt =("")

substringShape = ["circle", "square"]
substringAtt = ["perimeter", "circumference", "area"]

for c in range (0,len(substringShape)):
    if substringShape[c] in shapeInput:
        shapeAtt += (f"{substringShape[c]} ")
        break

for d in range (0,len(substringAtt)):
    if substringAtt[d] in shapeInput:
        shapeAtt += (substringAtt[d])
        break
    
match shapeAtt.split():
    case ["circle","area"]:
        print("circle area ")
    case ["circle","circumference"]:
        print("circle circumference ")
    case ["square","area"]:
        print("square area ")
    case ["square","perimeter"]:
        print("square perimeter ")
    case ["square","circumference"]:
        checkInp = input("Did you mean 'find the perimeter of a square?' ")
        if checkInp == "yes":
            print("square perimeter ")
        else:
            checkInp = input("Did you mean 'find the circumference of a circle?' ")
            if checkInp == "yes":
                print("circle circumference ")
            else:
                print("Sorry, I didn't understand you ")
    case ["circle","perimeter"]:
        checkInp = input("Did you mean 'find the perimeter of a square?' ")
        if checkInp == "yes":
            print("square perimeter ")
        else:
            checkInp = input("Did you mean 'find the circumference of a circle?' ")
            if checkInp == "yes":
                print("circle circumference ")
            else:
                print("Sorry, I didn't understand you ")
    case _:
        print("error ")
        
