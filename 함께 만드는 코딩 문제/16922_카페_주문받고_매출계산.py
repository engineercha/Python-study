import random

people=30
count=0
income=0
drinks=['에스프레소', '아메리카노', '카페라떼','녹차라떼','레몬에이드']
sum=[6,6,6,6,6]

for n in range(people):
    drink=random.choice(drinks)

    for i in range(5):
        if drinks[i]==drink and sum[i]>0:
            print("[주문접수완료]",end=' ')
            sum[i]-=1
            count+=1
            income+=4000
        elif drinks[i]==drink and sum[i]==0: print("[주문접수불가]",end=' ')
    
    print(f'{n+1:2}번째 손님: {drink}',end='\t')
    for i in range(5):
        if drink==drinks[i]: print('(잔량:%d)'%sum[i])

print(f'오늘의 판매 음료는 총 {count}잔, 총 매출은 {income//1000},000원입니다.')


#try1: 10:15~10:33
'''random 함수 쓰면서 import 안 함.
random.choice()에서 괄호 부분 안 씀.
sum[i]-=1 for문에 if문 쓰면 되는데 if drink=='에스프레소': 하나하나 다 씀. (디버깅 전 수정)
range(6)으로 잘못 설정함.
[주문접수] 후 다음 줄로 넘어감.'''

#try2: ~11:05
'''잔량 출력하도록 21~21 코드 추가함.
매출액에 콤마(,) 출력하도록 버림나눗셈 연산자 추가함.'''