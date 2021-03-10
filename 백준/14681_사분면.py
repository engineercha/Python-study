def Quadrant(x,y):
    if y>0:
        if x>0: return 1
        elif x<0: return 2
    elif y<0:
        if x<0: return 3
        elif x>0: return 4
        
x=int(input())
y=int(input())
print(Quadrant(x,y))