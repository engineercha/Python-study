import random
A=[]
while True:
    A.insert(0,random.randrange(-1000,1001))
    A.insert(1,random.randrange(-1000,1001))
    if A[0]!=0 and A[1]!=0: break
if A[0]>0:
    if A[1]>0: print(1)
    elif A[1]<0: print(4)
elif A[0]<0:
    if A[1]>0: print(2)
    elif A[1]<0: print(3)
print(A)
