#  [비교연산자, 조건문] 정수 3개 입력받고 가장 큰 수 출력하기 사진
a =int(input("첫번째 숫자 입력하시오: "))
b =int(input("두번째 숫자 입력하시오: "))
c =int(input("마지막 숫자 입력하시오: "))

if a<b:
    max=b
if a<c:
    max=c
else:
    max=a
print("가장 큰 수는",max,"입니다.")


#  [입력받기, 자료형변환] 입력받는 사칙연산 계산기 출력하기
print("a+b=",a+b,"\na-b=",a-b)
print("a*b=",a*b,"\na/b=",a/b)
print("a//b=",a//b,"\na%b=",a%b)



# [비교연산자, 조건문] 문자열 입력받고 조건에 따라 출력하기
#1
var=input("문자열 입력하시오: ")
sum=0
for i in range(len(var)):
    if var[i]=="모" and var[i+1]=="각" and var[i+2]=="코":
        sum+=1
if sum>=1:
    print("모각코 좋아요! X",sum,end=' ')
else: print("모각코 없어요")

#2
if "모각코" in var:
    print("모각코 좋아요!")
else:
    print("모각코 없어요")


#  [반복문] 마름모 출력하기
while True:
    n = int(input("숫자 입력하시오(0 입력시 종료): "))
    i=0
    j=0
    
    if n==0: break
    elif n%2==0:
        for i in range(int(n/2)):
            for j in range(int(n/2)-i):
                print(" ",end='')
            for j in range(i+1):
                print("**",end='')
            print("")

        for i in range(int(n/2)-1):
            for j in range(i+2):
               print(" ",end='')
            for j in range(int(n/2)-(i+1)):
                print("**",end='')
            print("")   

    elif n%2!=0:
        for i in range(int((n+1)/2)):
            for j in range(int((n+1)/2)-i):
                print(" ",end='')
            for j in range(2*i+1):
                print("*",end='')
            print("")
        
        for i in range(int((n+1)/2-1)):
            for j in range(i+2):
                print(" ",end='')
            for j in range(int(n)-2*(i+1)):
                print("*",end='')
            print("")