#ver1
meter=int(input("나무 높이: "))
up=int(input("낮 동안 오를 높이: "))
down=int(input("밤 동안 내릴 높이: "))
sum=0       #달팽이가 오른 높이
count=0     #날짜 카운트

while(True):
    if down>=up:
        print("달팽이는 평생 오르지 못 합니다.\n")
        break
    sum+=up
    sum-=down
    count+=1
    if sum>=meter:
        print(f'달팽이는 {count}일을 소요하여 나무에 올랐습니다.\n')
        break


#ver2
def get_days(m,u,d):
    real_up=u-d             #하루에 실제로 오르는 높이
    if u!=d:        
        days=m//real_up     #소요일(*소수점 버림)

    if real_up<=0: return print("달팽이는 평생 오르지 못 합니다.")
    if m%real_up==0:
        return print(f'달팽이는 {days}일을 소요하여 나무에 올랐습니다.')
    elif m%real_up>0:
        return print(f'달팽이는 {days+1}일을 소요하여 나무에 올랐습니다.')     #나머지가 있는 경우, 소수점 올림함.


#ver3
meter, up, down=input("나무 높이, 오를 높이, 내릴 높이를 스페이스로 띄어서 입력하세요:\n").split()
meter=int(meter)
up=int(up)
down=int(down)
get_days(meter,up,down)


#try1: 6:28~31
'''break 조건을 sum==meter로 잘못 둚.(디버깅 전 수정)
up<down인 경우 높이 - 된다며 if sum<0: sum=0 했음.'''
#try2: ~6:41 ver1성공
#try3: 6:42~45 ver2성공
#try4: 7:5~19 ver3성공
'''int() 안 묶어줌.'''
#try5: ~7:33 ver2_함수화 성공
'''def의 매개변수명이 전달하는 변수명과 같아도 둘은 별개임.
결과 출력할 때 print() 써서 None 출력됨.
ZeroDivisionError: integer division or modulo by zero; up==down인 경우 나누는 값 0 되면서 오류 뜸.'''