# # [반복문] 1~100 중 3의 배수이면서 2의 배수는 아닌 수 개수 출력하기
# sum=0
# for i in range(1,101):
#     if i%3==0 and i%2!=0:
#         sum+=1
# print(sum)


# # [반복문] 비밀번호 설정 후 맞는 비밀번호가 입력될 때까지 입력하기
# password=1886
# while True:
#     a=int(input("비밀번호 4자리를 입력하세요: "))
#     if a==password:
#         print("맞았습니다!")
#         break
#     else: print("틀렸습니다!")


# # [비교연산자,조건문] 시험점수 입력받고 점수에 따른 학점 출력하기
# while True:
#     score=int(input("점수를 입력하세요: "))
#     if score>0 and score<=100: break
#     else: print("다시 입력하세요.")

# if score>=90:
#     print("당신의 학점은 A 입니다.")
# elif score>=80:
#     print("당신의 학점은 B 입니다.")
# elif score>=70:
#     print("당신의 학점은 C 입니다.")
# elif score>=60:
#     print("당신의 학점은 D 입니다.")
# else: print("당신의 학점은 F 입니다.")


# # [비교연산자,조건문] 연도 입력받고 윤년인지 판단하기
# '''4로 나누어 떨어지고, 100으로 나누어 떨어지지 않는 해는 윤년임.
# 400으로 나누어 떨어지는 해는 무조건 윤년임'''
# year=int(input("연도를 입력하세요: "))
# if year%400==0 or year%4==0 and year%100!=0:
#     print(str(year)+"년은 윤년입니다.")
# else: print(str(year)+"년은 윤년이 아닌 평년입니다.")


# # [함수] 짝수 홀수 판단하는 함수 만들기
# #1
# def evenodd(a):
#     if a%2==0:
#         return "짝수입니다!"
#     else: return "홀수입니다!"

# num1=int(input("정수를 입력하세요: "))
# print(evenodd(num1))

# #2
# def oddeven(a):
#     if a%2==0:
#         print("짝수입니다!")
#     else: print("홀수입니다!")

# num2=int(input("정수를 입력하세요: "))
# oddeven(num2)


# # [리스트] 7개 정수를 입력받고 합 구하기
# numbers=[]
# print(type(numbers))
# sum=0
# for i in range(7):
#     a=int(input())
#     numbers.insert(i,a) #두 줄을 numbers.append(int(input())로 생략 가능
#     sum+=numbers[i]
# print("합계:",sum)


# [리스트] 조건에 따른 계산기 만들기
line=input("띄어쓰기 없이 정수,덧셈,뺄셈으로 이루어진 수식을 입력하세요: ")
#숫자 리스트
nums=line.replace('+',' ').replace('-', ' ').split() #+와 -를 공백으로 변환한 뒤 split으로 숫자만 받음.
#연산자 리스트
cals=[]
for i in line:
    if i=='+' or i=='-':
        cals.append(i)
#연산
result=int(nums[0])
for i in range(len(cals)):
    if cals[i]=='+': result+=int(nums[i+1])
    elif cals[i]=='-': result-=int(nums[i+1])
#결과 출력
print(result)