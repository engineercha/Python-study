#전역변수 선언
A=[0,0,0,0]
B=[0,0,0,0]
C=[0,0,0,0]

#좌석출력 함수
def status(A,B,C):
    print(" \t1\t2\t3\t4")
    print("A",end='\t')
    for i in range(4):
        if A[i]==0: print("□",end='\t')
        elif A[i]==1: print("■",end='\t')

    print("\nB",end='\t')
    for i in range(4):
        if B[i]==0: print("□",end='\t')
        elif B[i]==1: print("■",end='\t')

    print("\nC",end='\t')
    for i in range(4):
        if C[i]==0: print("□",end='\t')
        elif C[i]==1: print("■",end='\t')


# 메인함수
print("      <자리 예매 프로그램>")
print(status(A,B,C))

while True:
    print("\n1.예매    2.예매 취소    3.종료"); print(">>",end=' ')
    choice=int(input())

    if choice==1:
        while True:
            print("자리를 선택해주세요. ex) A3"); print(">>", end=' ')
            seat=input()
            if (seat[0] in "ABC") and (seat[1] in "1234"): break
        num=int(seat[1])-1
        if seat[0]=='A': A.remove(0); A.insert(num,1)
        elif seat[0]=='B': B.remove(0); B.insert(num,1)
        elif seat[0]=='C': C.remove(0); C.insert(num,1)
        print("예매가 완료되었습니다.")
        print(status(A,B,C))

    elif choice==2:
        while True:
            print("취소할 자리를 선택해주세요. ex) B2"); print(">>", end=' ')
            seat=input()
            if (seat[0] in "ABC") and (seat[1] in "1234"): break
        num=int(seat[1])-1
        if seat[0]=='A' and A[num]==1: A[num]=0; print("예약이 취소되었습니다.")
        elif seat[0]=='B' and B[num]==1: B[num]=0; print("예약이 취소되었습니다.")
        elif seat[0]=='C' and C[num]==1: C[num]=0; print("예약이 취소되었습니다.")
        else: print("비어있는 자리입니다.")
        print(status(A,B,C))
    
    elif choice==3: print("프로그램을 종료합니다"); break
    else: print("메뉴를 잘못 선택하셨습니다"); continue