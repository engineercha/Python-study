# 입력과 자료형 변환


## input()
'''파이썬의 input()은 모든 입력값을 무조건 문자열로 저장함.'''

a = input("문자 입력: ")
print(a)
print(type(a))


## 자료형 변환: int(), float(), str()
# 숫자
print(int(3.0))
print(float(3))

a = int(input("숫자 입력: "))
print(a)
print(type(a))

# 문자
age=21
subject="python"
print("안녕 나는",subject,"공부하는",age,"살이야.")
print("안녕 나는 "+subject+" 공부하는 "+str(age)+" 살이야.")


# 오늘의 문제
birth = int(input("\n생년월일 8자리를 입력해주세요.: "))
print(birth//10000," 년")
print(birth%10000//100," 월")
print(birth%100," 일")