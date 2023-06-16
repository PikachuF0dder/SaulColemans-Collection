import math

coor1 = [0,0]
coor2 = [0,0]

coor1[0] = int(input("Enter X1: "))
coor1[1] = int(input("Enter Y1: "))
coor2[0] = int(input("Enter X2: "))
coor2[1] = int(input("Enter Y2: "))

def lenFinder(coor1, coor2):
    lineLen = math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2)
    return lineLen

print(lenFinder(coor1, coor2))
    
