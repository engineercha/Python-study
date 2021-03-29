#높이가 n인 직각이등변 삼각형 출력

n=int(input("삼각형의 높이를 입력하세요: "))
for i in range(n):
    for j in range(n-(i+1)): print('  ',end='')
    for j in range(i+1): print(f'* ', end='')
    print()

#3월 달력 출력
print('\t\t\t<3월>')
print('일\t월\t화\t수\t목\t금\t토')
for i in range(0,32,7):             #주: 0, 7, 14, 21, 28
    for j in range(i,i+7):          #일: 0~6, 7~13, 14~20, 21~27, 28~34
        if j==0: print('\t',end='')
        elif j>31: break
        else: print(f'{j}',end='\t')
    print()

#ver2
print('---------------------------------------------------')
for i in range(0,32):
    if i==0: print('\t',end=''); continue   #i==0이면 loop의 다음 순번으로 이동
    elif i%7==0: print()
    print(f'{i}',end='\t')          #i==0를 제외한 모든 경우에 i 출력