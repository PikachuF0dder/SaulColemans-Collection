L = [[2,3],[1,4],[1,4],[2,3]]
pathL = []

def checkNebur(cur,end,L):
    path = False
    for z in range (len(L[cur])):
        if L[cur][z] == end:
            path = True
    return path

def Round(pathL,cur,end,L):
    for q in range (len(L[cur])):
        path = checkNebur(q,end,L)
        if path == True:
            end = cur
            pathL.append(cur)
            return(path)

for r in range (len(L)):
    for s in range (len(L[r])):
        path = Round(pathL,r,4,L)
        if path == True:
            s = (len(L[r]))

print(pathL)
        
    
