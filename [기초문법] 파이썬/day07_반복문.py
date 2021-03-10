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
print("\n\n")


# 오늘의 문제: 1~100 중 7의 배수가 아닌 짝수의 개수 출력하기
#1
num=0
print("before: ",end='')
for i in range(1,101):
    if i%2==0 and i%7!=0:
        print(i,end=", ")
        num+=1
print("\n총 %d개"%num)


#ver2:
nums=[]                     #7의 배수가 아닌 짝수를 담는 리스트
count=0
print("after: ",end='')
for i in range(1,101):
    if i%2==0 and i%7!=0:
        nums.append(i)
        count+=1            #개수 카운트

max=nums[-1]                #리스트의 가장 마지막 수
for i in range(len(nums)):
    if nums[i]!=max:
        print(nums[i],end=', ')
    else: print(max)        #100인 경우 ,를 출력하지 않음.
print("총 %d개\n"%count)



#2: 0 입력 전까지 받은 숫자들의 합 출력하기
sum=0
while True:
    n=int(input("숫자를 입력하세요(종료:0): "))
    if n==0: break
    sum+=n
print(sum)