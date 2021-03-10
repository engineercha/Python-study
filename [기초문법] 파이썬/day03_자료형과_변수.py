# 자료형과 변수


## 숫자
'''정수(integer)형 int //소수점이 없고 개수를 세는 데 사용함
실수(floating)형 float //소수점이 있는 실수로, 분수나 평균 계산에 많이 사용함'''

# type(__)
print(type(2021))
print(type(02.08))

# type("__")
print(type("2021"))
print(type("02.08 월"))

# 계산 출력
print(999 + 1)
print(0.6 + 0.4)

print("999 + 1")            # 따옴표("")로 묶은 것은 문자열이므로, 그대로 출력됨
print("0.6" + "0.4")        # 문자열을 더한 것은 띄어쓰기 없이 출력됨


## 불(boolean)
'''참과 거짓을 나타내어, 조건문에서 많이 사용됨'''

# True
print(True)
print(100 > 1)

# Flase
print(10 < 1)
print(type(10 < 1))


## 변수
'''데이터를 저장하는 컴퓨터 상 공간으로, 변수 안의 데이터는 가변성이 있음'''

first_name = "Cha"
job = "student"
print(job, first_name)

job = "engineer"
print(job, first_name)


## 문자열 인덱싱
'''문자열의 글자에 번호를 0부터 지정하고 가리키는 것임.
띄어쓰기와 특수문자도 번호가 부여되며, 음수 인덱스는 뒤에서 부터 가리킴.'''

im = "모각코 파이썬 기초문법 3기!"

print(im[0])
print(im[-2])

'''문자열[시작:끝]은 시작번호~끝번호-1의 문자를 슬라이싱 함.'''
print(im[4:7])
print(im[-8:]) # 마지막까지
print(im[:5],"이팅") # 처음부터

print(im[7])


## 오늘의 문제

year = 1886
major = 70.
grade = 2 < 4
id = "제 이름은 차수빈입니다."

print(type(year))
print(type(major))
print(type(grade))
print(type(id))
print(id[6:9])