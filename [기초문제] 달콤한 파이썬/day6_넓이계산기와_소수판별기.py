"""도형별 넓이 계산기
메뉴에 있는 도형을 선택하고 길이를 입력받아 넓이를 구할 수 있는 코드를 작성해보세요.
1) 도형은 원, 삼각형, 직사각형, 정사각형이 존재
2) 도형의 넓이 계산은 무조건 함수로 정의
3) 도형 별로 필요한 길이를 입력 (원 → 반지름, 삼각형 → 밑변,높이, 직사각형 → 가로,세로, 정사각형 → 한 변의 길이)"""

#넓이 계산 함수
def circle(r):
    area=3.14*r**2
    print("반지름의 길이가 %d인 원의 넓이는 약 %.2f입니다." %(r,area))
def triangle(a,h):
    area=0.5*a*h
    print("밑변이 %d이고 높이가 %d인 삼각형의 넓이는 %d입니다." %(a,h,area))
def rectangle(a,b):
    area=a*b
    print("가로가 %d고 세로가 %d인 직사각형의 넓이는 %d입니다." %(a,b,area))
def square(a):
    area=a**2
    print("한변의 길이가 %d인 정사각형의 넓이는 %d입니다." %(a,area))

print("==============도형 목록==============")
print("1.원  2.삼각형  3.직사각형  4.정사각형")
print("====================================")

#메인함수
while True:
    choose=int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력하세요: "))
    if choose in [1,2,3,4]: break

if choose==1:
    radius=int(input("원의 반지름 길이를 입력하세요: "))
    circle(radius)
elif choose==2:
    base=int(input("삼각형의 밑변 길이를 입력하세요: "))
    height=int(input("삼각형의 높이를 입력하세요: "))
    triangle(base,height)
elif choose==3:
    length=int(input("직사각형의 가로 길이를 입력하세요: "))
    height=int(input("직사각형의 세로 길이를 입력하세요: "))
    rectangle(length,height)
elif choose==4:
    side=int(input("한변의 길이를 입력하세요: "))
    square(side)


"""뒤집은 소수
여러 숫자를 입력받고, 각 숫자가 뒤집었을 때 소수이면 출력을 하는 프로그램을 만들어보세요.
1) 숫자를 뒤집었을 때 소수이면 출력 (ex. 32를 뒤집었을 때 23이고, 23은 소수이므로 출력)
2) 최소 두 개 이상의 함수를 사용"""
print()

#소수 판별 함수
def check_prime(n):
    if n==1: return False               #1은 소수가 아님
    for i in range(2,n):
        if n%i==0: break; return False  #1과 자기자신 외 나눠지는 수가 있으면 소수가 아님
        else: return True

#수 뒤집는 함수
def reverse(n):
    n,N=str(n),""
    for i in range(len(n)-1,-1,-1): N+=str(n[i])    #역순으로 문자열 저장
    return int(N)

#전역변수 선언
nums=[]
count=0

#메인함수
ea=int(input("입력받을 숫자의 개수를 입력하세요: "))
for i in range(ea):
    n=int(input(f'수 입력({i+1}/{ea}): '))
    nums.append(n)                      #nums에 입력받은 정수들 저장

for i in range(ea):
    if check_prime(nums[i])==True:      #소수면 리버스, 카운트
        print("%d번째로 입력한 수 %d는 뒤집었을 때 소수 %d입니다." %(i+1,nums[i],reverse(nums[i])))
        count+=1
if count==0: print("입력한 수 중 뒤집어서 소수가 되는 수는 없습니다.")