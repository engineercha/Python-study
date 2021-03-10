import time
import datetime
from datetime import datetime
from datetime import timedelta

print("=== 종강 디데이 계산기 ===")
day=int(input("기준년월일 예)20210304 : "))

today=datetime.today()
now=datetime(today.year, today.month, today.day, today.hour, today.minute, today.second)
end=datetime(day//10000, (day%10000)//100, day%100)

d_day=end-now
print(f'종강까지 {d_day} 남았습니다.')



#6:30~ 
#time 모듈
'''time함수를 호출하면 1970년 1월 1일 0시 0분 0초 이후 경과 시간을 초단위로 반환함.
>> time.time()

localtime함수를 사용하면 날짜와 시간 형태로 반환함.
>> time.localtime(time.time())     #초에 time.time()이 들어갔으므로 현재 시간이 출력됨.
time.struct_time(tm_year=, mon=, mday=, min=, sec=, wday=, yday=, isdst

time.strftime함수는 날짜와 시간을 원하는 포맷으로 출력함.
>> time.strftime('%y %m %d', time.localtime(time.time()))
2021-03-05
>> time.strftime('%c', time.localtime(time.time()))
Fri March 5 10:59:46 2021

A: 요일, a: 요일 줄임말, B: 월, Y: 4자리 연도, b: 월 줄임말, m: 월(숫자), d: 일, H: 24시, I: 12시, M: 분, S: 초'''


#datetime모듈
'''datetime클래스의 today메서드로 현재 날짜와 시간을 구함.
>> datetime.datetime.today()
datetime.datetime(2021, 3, 5, 11, 9, 42, 536110)

datetime.datetime()에 연,월,일, 시,분,초,마이크로초를 넣어 객체를 만들 수 있음.
>> d=datetime.datetime(2021, 3, 5)
>> d
datetime.datetime(2021, 3, 5, 0, 0)

strptime()을 사용하면 문자열을 객체로 만들 수도 있음.
>> d=datetime.datetime.strptime('2021-03-05', '%Y-%m-%d') *포맷을 지정해야 함.
>> d
datetime.datetime(2021, 3, 5, 0, 0)

datetime.timedelta()는 두 날짜와 시간 사이의 차이를 계산함.
>> d=datetime(2021, 3, 5)
>> from datetime import timedelta
>> d - timdelta(days=2)
datetime.timedelta(2018, 3, 3, 0, 0)'''