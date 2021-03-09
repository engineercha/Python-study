import random
count=1             #게임 횟수
win=0               #승리 횟수

while True:
    #사용자 입력
    while (True):
        user=input(">> 가위, 바위, 보! (0 입력시 게임 종료)\n당신: ")
        if ('가위' in user) or ('바위' in user) or ('보' in user) or user=='0': break   #사용자가 가위바위보 중 하나 또는 0을 입력했으면 반복 중단
    
    #컴퓨터 입력(=난수)
    lst=['가위', '바위', '보']
    computer=random.randrange(3)
    print(f'>> 컴퓨터: {lst[computer]}')

    #승부 판단
    if user==lst[computer]: result="무승부!"
    elif user=='가위':
        if lst[computer]=='바위': result='패'
        else: result='승'
    elif user=='바위':
        if lst[computer]=='보': result='패'
        else: result='승'
    elif user=='보':
        if lst[computer]=='가위': result='패'
        else: result='승'
    print(f'{result}!\n')

    #전승 누적 및 게임 중단
    if result=='승': win+=1
    if user=='0':
        print(f'당신의 기록은 {count}전 {win}승입니다.')
        break
    count+=1