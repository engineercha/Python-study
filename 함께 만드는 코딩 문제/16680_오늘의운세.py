import random

name=input("이름을 입력하세요: ")

hh=random.randrange(0,25)
mm=random.randrange(0,60)

place=['집','학교','기숙사','학원','독서실','병원','시내','여행지','침대','화장실']
obj=['공부','핸드폰','지우개','옷','돈','과자','게임','여권','이불','수건']
verb=['포기할','뿌릴','잃어버릴','버릴','주울','먹을','찾을','털','떨어뜨릴']

#ver1
print(f'{name}님은 오늘 {hh}:{mm}에 {random.choice(place)}에서 {random.choice(obj)}을(를) {random.choice(verb)} 것입니다.',end='\n\n')


import datetime

now=datetime.datetime.now()
today=now.strftime('%m월 %d일')

love=random.randrange(1,101)
people=random.randrange(1,101)
study=random.randrange(1,101)
money=random.randrange(1,101)

total=(love+people+study+money)//4

#ver2
print("애정운 %d점, 대인운 %d점, 학업운 %d점, 재물운 %d점으로,"%(love,people,study,money))
print(f'{today} {name}님의 총운은 {total}점입니다.')