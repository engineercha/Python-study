name=input("닉네임: ")
post=int(input("게시글 수: "))
comment=int(input("댓글 수: "))
attend=int(input("출석 수: "))
activity=post+comment+attend

if activity<10: print(f'{name}님은 코생아 입니다.')
elif activity<30: print(f'{name}님은 코린이 입니다.')
elif activity<60: print(f'{name}님은 코른이 입니다.')
else: print(f'{name}님은 코마스터 입니다.')