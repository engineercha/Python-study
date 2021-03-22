n=0
while 1:
    n=int(input("마름모의 높이: "))
    if n!=0: break

#ver1
if n%2!=0: star(n)
    for i in range((n+1)//2):
        for j in range((n-1)//2-i): print(" ",end='')
        for k in range(2*i+1): print("*",end='')
        print("")
    for i in range((n-1)//2):
        for j in range(i+1): print(" ",end='')
        for k in range(n-2*(i+1)): print("*",end='')
        print("")

#ver2
if n%2==1: i=1
else: i=2           # i=1 if n%2==1 else 2

for i in range(i, n+1, 2):
    print('{0}{1}{0}'.format(' '*((n-i)//2), '*'*i))
for i in range(i-2, 0, -2):
    print('{0}{1}{0}'.format(' '*((n-i)//2), '*'*i))