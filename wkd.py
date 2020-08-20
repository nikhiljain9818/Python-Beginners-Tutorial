x = 1
y = 1
z= 1
n = 2
##ar = []
##p = 0
##for i in range(X+1):
##   for j in range(Y+1):
##      if i+j != N:
##         ar.append([i,j])
##         
##         p += 1
##print(ar)

##lol = [[i,j] for i in range(x+1) for j in range(y+1) if ((i+j) != n)]
##print(lol)

##lol = []
##for i in range(X+1):
##   for j in range(Y+1):
##      for k in range(Z+1):
##         if i+j+k != N:
##            lol.append([i,j,k])
##print(lol)


##lol = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z) if X+Y+Z != N]
##print(lol)
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
       
   
