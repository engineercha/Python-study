#전역변수 선언
seats=[[0 for j in range(4)] for i in range(3)]    #[[0,0,0,0],[0,0,0,0],[0,0,0,0]]와 동일
line={0:"A", 1:"B", 2:"C"}
find={"A":0, "B":1, "C":2}

#좌석출력 함수
def status(a):
    print(" \t1\t2\t3\t4")
    for i in range(3):
        print(line[i],end='\t')
        for j in range(4):
            if a[i][j]==0: print("□",end='\t')
            elif a[i][j]==1: print("■",end='\t')
        print()

#메인함수
print("\t<자리 예매 프로그램>")
print(status(seats))

while True:
    print("\n1.예매    2.예매 취소    3.종료"); print(">>",end=' ')
    choice=int(input())

    if choice==1:
        while True:
            print("자리를 선택해주세요. ex) A3"); print(">>", end=' ')
            seat=input()
            if (seat[0] in "ABC") and (seat[1] in "1234"): break
        i=find[seat[0]]
        j=int(seat[1])-1
        print("예매가 완료되었습니다.") if seats[i][j]==0 else print("이미 예약된 자리입니다.")
        seats[i].remove(0); seats[i].insert(j,1)
        print(status(seats))

    elif choice==2:
        while True:
            print("취소할 자리를 선택해주세요. ex) B2"); print(">>", end=' ')
            seat=input()
            if (seat[0] in "ABC") and (seat[1] in "1234"): break
        i=find[seat[0]]
        j=int(seat[1])-1
        print("예약이 취소되었습니다.") if seats[i][j]==1 else print("비어있는 자리입니다.")
        seats[i][j]=0
        print(status(seats))
    
    elif choice==3: print("프로그램을 종료합니다"); break
    else: print("메뉴를 잘못 선택하셨습니다"); continue