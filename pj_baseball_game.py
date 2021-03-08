import random

while True:
    #게임 시작 선택
    start=int(input("\n>> 숫자야구 게임을 시작합니다.\n0: exit, 1: start\n\t>> "))
    if start==0:
        print("게임을 종료합니다.")
        break
    elif start!=1: print(">> 잘못 입력하셨습니다.") #0도 1도 아니면 입력 반복
    
    #게임 레벨 선택
    while True:
        level=int(input("\n>> 숫자야구 레벨을 고르세요!\n0: EASY  1: NORMAL  2: HARD\n\t>> "))
        if level==0 or level==1 or level==2:
            digits=level+2                    #선택한 레벨에 따라 사용자가 맞혀야 할 숫자의 자릿수 결정
            break
        else: print(">> 잘못 입력하셨습니다.") #0,1,2 중 선택할 때까지 입력 반복

    #난수 생성
    while True:
        true=[random.randrange(10) for i in range(digits)]  #0~9 사이의 난수를 digits만큼 저장
        if len(true)==len(set(true)): break                 #true 안에 중복수가 없을 때까지 난수 생성 반복
    print(f'\n>> 컴퓨터가 숫자를 정했습니다. {digits}자리 숫자를 맞춰보세요!')
    # print(true)
    
    #사용자입력 및 결과 출력
    count=1                               #도전횟수 카운트
    while True:
        user=input(f'round{count}~!: ')
        ulst=user.replace('',' ').split() #사용자가 입력한 문자열의 각 문자 사이에 공백을 넣고, 각각을 분리하여 리스트에 저장
        strike=0
        ball=0
        #스트라이크/볼 판단
        for i in range(digits):
            if int(ulst[i])==true[i]: strike+=1 #수도 같고 자리도 같으면 strike
            elif int(ulst[i]) in true: ball+=1  #자리는 다르지만 같은 수가 있으면 ball
        #홈런 판단
        if strike==digits:
            print("Home Run~!!!")
            break
        else:
            print(f'{ball}B {strike}S') #홈런이 아니면 strike/ball수 출력 후 입력 반복        
            count+=1
    break