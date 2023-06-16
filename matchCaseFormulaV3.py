
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

def calc(shapeAtt):
    match shapeAtt.split():
        case ["square","area"]:
            print("calculating the area of a square then...")
            sideLen = int(input("Enter the side length of the square: "))
            print(f"The area of your square is: {sideLen*sideLen}")
        case ["square","perimeter"]:
            print("calculating the perimeter of a square then...")
            sideLen = int(input("Enter the side length of the square: "))
            print(f"The perimeter of your square is: {sideLen*4}")
        case ["circle","area"]:
            print("calculating the area of a circle then...")
            cirRad = int(input("Enter the radius of the circle: "))
            print(f"The area of your circle is: {3.141592654*(cirRad**2)}")
        case ["circle","circumference"]:
            print("calculating the circumference of a circle then...")
            cirDim = int(input("Enter the diameter of the circle: "))
            print(f"The circumference of your circle is: {3.141592654*cirDim}")
 
def checkError(shapeAtt):
    if shapeAtt[0] == "c" or shapeAtt[0] == "s":
        checkInp = input("Did you mean 'find the perimeter of a square?' ")
        if checkInp == "yes":
            calc("square perimeter")
        else:
            checkInp = input("Did you mean 'find the circumference of a circle?' ")
            if checkInp == "yes":
                calc("circle circumference")
            else:
                print("Sorry, I didn't understand you ")

match shapeAtt.split():
    case ["square", ("perimeter" | "area") as att]:
        calc(shapeAtt)
    case ["circle", ("circumference" | "area") as att]:
        calc(shapeAtt)
    case ["square","circumference"] | ["circle","perimeter"]:
        checkError(shapeAtt)
    case _:
        print("sorry, I didn't understand you. ")
    

