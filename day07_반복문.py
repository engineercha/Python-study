# 구구단
#1
for i in range(2,10):
    for j in range(1,10):
        print("%dX%d=%2d"%(i,j,i*j),end='  ')
    print()

#2
i=2
while i<=9:
    j=1
    while j<=9:
        print(f'{i}X{j}={i*j:2}', end='  ')
        j+=1
    print()
    i+=1

#3
for a in range(2,10): print(str(a)+"단",end='\t')
print()

for i in range(1,10):
    for j in range(2,10):
        print(f'{j}X{i}={i*j:2}',end='  ')
    print()

#4
i=int(input("구구단 단을 입력하시오: "))
for j in range(1,10): print('{}X{}={:2}'.format(i,j,i*j),end='  ')
print()


# 오늘의 문제
#1: 1~100 중 7의 배수가 아닌 짝수의 개수 출력하기
num=0
for i in range(1,101):
    if i%2==0 and i%7!=0:
        if i==100: print(i)
        else:
            print(i,end=", ")
        num+=1
print("총 %d개"%num)

#2: 0 입력 전까지 받은 숫자들의 합 출력하기
sum=0
while True:
    n=int(input("숫자를 입력하세요(종료:0): "))
    if n==0: break
    sum+=n
print(sum)