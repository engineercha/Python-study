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


# 오늘의 문제 : 생년월일 출력하기

birth = int(input("\n> 생년월일 8자리를 입력하시오: "))
print(birth//10000,"년", end=' ')
print(birth%10000//100,"월", end=' ')
print(birth%100,"일", end=' ')


# 오늘의 예제 : 생년월일을 영어로 출력하기

time = input("\n\n> 생년월일 8자리를 재입력하시오: ")

y=int(time[:4])
m=int(time[4:6])
d=int(time[6:])

#1
if m==1:
    print("January",end=' ')
elif m==2:
    print("February",end=' ')
elif m==3:
    print("March",end=' ')
elif m==4:
    print("April",end=' ')
elif m==5:
    print("May",end=' ')
elif m==6:
    print("June",end=' ')
elif m==7:
    print("July",end=' ')
elif m==8:
    print("August",end=' ')
elif m==9:
    print("September",end=' ')
elif m==10:
    print("October",end=' ')
elif m==11:
    print("November",end=' ')
else:
    print("December",end=' ')

print(d, y)

#2
month_dic = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
english_m=month_dic[m]
print(english_m, d, y)