# 비교연산자
a=10
b=1
print(a>b,a>=b,a!=b)
print(a<b,a<=b,a==b)

# 논리연산자
x=100
y=True
print(x>10 and y==True)
print(x<10 or y==True)
print(not y)

# if문
line="Hello world"
if "World" in line:
    print("World가 있습니다")
else: print("World가 없습니다")

# 오늘의 문제
#1
first=int(input("첫 번째 과목의 점수를 입력하세요: "))
second=int(input("두 번째 과목의 점수를 입력하세요: "))
third=int(input("세 번째 과목의 점수를 입력하세요: "))

avg=(first+second+third)/3
if avg>=50:
    print("평균 점수는 %.2f"%avg+"점으로 합격입니다.")
else: print("평균 점수는 %.2f"%avg+"점으로 불합격입니다.")

#2
word=input("단어를 입력하세요: ")
sentence=input("문장을 입력하세요: ")
if word in sentence:
    print("단어가 있습니다.")
else: print("단어가 없습니다.")