# matrix lists 
M = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
N = [[16,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[16,1,2,3]]
L = []

# creates correctly sized empty 'matrix' for answer 'matrix'
for g in range (0,len(M)):
    L.append([])
    for h in range (0,len(N[0])):
        L[g].append(0)

# calculates the answer of multiplying matrix M and N of any correct size     
for a in range (0,len(M)):
    for b in range (0,len(N[0])):
        x = 0
        for c in range(0,len(M[0])):
            x += (M[a][c]*N[c][b])
            L[a][b] = x

# prints answer
print(L)
