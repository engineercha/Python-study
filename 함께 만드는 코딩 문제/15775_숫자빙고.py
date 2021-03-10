import random

#빙고판 리스트
computer=[random.randrange(1,21) for i in range(9)]
player=[]

#플레이어 숫자 입력
count=0
while(True):
    if count==0: num=(int(input("1~20 사이의 수 9개를 엔터로 나눠 입력하세요.\n(잘못 입력했다면 0 입력 후 재입력): ")))
    else: num=(int(input()))

    if num==0: del player[-1]
    else: player.append(num)
    count+=1
    if len(player)==9: break

#빙고판 출력 함수
def board(lst):
    for i in range(9):    
        print(f'{lst[i]:2}',end=' ')
        if (i+1)%3==0: print()
    return

#Bingo 판별 함수
def result(computer,player):
    cwin=0
    pwin=0
    for i in range(9):
        #가로 빙고
        if i%3==0:
            if computer[i:i+3]==[' X',' X',' X']: cwin+=1
            if player[i:i+3]==[' X',' X',' X']: pwin+=1
        #세로 빙고
        if i>=0 and i<=2:
            if computer[i]==' X' and computer[i+3]==' X' and computer[i+6]==' X': cwin+=1
            if player[i]==' X' and player[i+3]==' X' and player[i+6]==' X': pwin+=1       
    #대각선 빙고
    if computer[0]==' X' and computer[4]==' X' and computer[8]==' X': cwin+=1
    elif computer[2]==' X' and computer[4]==' X' and computer[6]==' X': cwin+=1  
    if player[0]==' X' and player[4]==' X' and player[8]==' X': pwin+=1  
    elif player[2]==' X' and player[4]==' X' and player[6]==' X': pwin+=1
    return cwin, pwin


print("\n>> 숫자빙고를 시작합니다!\n<당신의 빙고판>\n===============")
board(player)
print("===============")

while(True):
    #플레이어 차례
    p=int(input("\n숫자를 입력하세요: "))
    for i in range(9):
        if player[i]==p: player[i]=' X'
        if computer[i]==p: computer[i]=' X'
    board(player)
    cwin, pwin=result(computer, player)
    if (cwin+pwin)>=1: break

    #컴퓨터 차례
    while(True):                        #컴퓨터가 숫자를 고를 때까지 random.choice 반복함.
        c=random.choice(computer)
        if c!=' X': break
    print(f'\n>> 컴퓨터: {c}!!\n')
    for i in range(9):
        if computer[i]==c: computer[i]=' X'
        if player[i]==c: player[i]=' X'
    board(player)
    cwin, pwin=result(computer, player)
    if (cwin+pwin)>=1: break

#결과 출력
if cwin > pwin: print("\n>> Computer wins!\n")
elif pwin > cwin: print(f'\n>> {pwin} Bingo! You win!\n')
else: print("\n>> draw!\n")

print("<컴퓨터 빙고판>\n===============")
board(computer)
print("===============")


#2021-03-05
#오후 10:10 가로,세로 Bingo! 출력까지 구현.
#오후 10:46 숫자 2개가 X 되는 현상 잡음. (원인: if computer[i]==n: player[i]=' X')
#오후 11:12 세로,대각선 Bingo 안 되는 오류 잡음. (원인: computer[0]=[' X'] 등으로 표기)
#오후 11:22 컴퓨터는 Bingo여도 break 안 되는 현상 발견, 컴퓨터가 이기면 컴퓨터 보드를 출력하도록 개선.

#2021-03-06
#오후 05:18 컴퓨터도 자기 보드 중에서 숫자를 고르고, 플레이어 보드에 같은 숫자가 있다면 같이 지워지도록 개선.
#오후 05:55 숫자 재입력 가능하도록 수정, break용 승리 횟수 변수 추가.
#오후 07:50 while문 내 print 전부 삭제, 마지막에 bingo 개수 출력하도록 개선.
#오후 08:12 컴퓨터 Bingo가 아니어도 draw 되는 현상 발견. (원인: elif pwin>pwin:)
#오후 08:17 draw 판별문을 첫 줄로 꺼냄.
#오후 08:23 플레이어 Bingo가 나왔음에도 컴퓨터 입력 받는 현상 발견.
#오후 09:23 Bingo 판별 코드 함수화 및 draw 변수 삭제, 정상 결과 출력 확인.