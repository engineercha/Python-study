import requests
from bs4 import BeautifulSoup as bs
import random
import time

#회차 및 당첨번호 크롤링
raw=requests.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin')
soup=bs(raw.text, 'html.parser')
box=soup.find('div', {'class' : 'win_result'})

times=box.find('strong'); print(times.text)
nums=box.find_all('span')
win_nums=[]
for num in nums:
    win_nums.append(num.text)


#로또 구매 개수 입력
amount=int(input("몇 개 구매하시겠습니까? "))

#로또번호(수동) 및 보너스(자동) 입력
my_nums=[]
while True:
    line=input(f'번호 6개를 띄어쓰기로 나눠 입력하세요: ').split(' ')
    if len(line)!=6 or len(line)!=len(set(line)):
        print("다시",end=' ')
        continue
    bonus=str(random.randrange(1,46))
    if bonus not in line:
        line.append(bonus); my_nums.append(line)
    if len(my_nums)==amount: break


#로또 줄 구별 코드
label=[]
for i in range(65,91): label.append(chr(i))

#로또 출력
print("\n\t        Lotto 6/45")
print("----------------------------------------")
for i in range(amount):
    print(label[i], my_nums[i])
print("----------------------------------------")
print(f'금액\t\t\t      ₩{1000*amount}\n')

#대기 출력
print("당첨 확인 중",end='')
for i in range(3):
    time.sleep(1)
    print("·",end='')

#당첨번호 출력
print(win_nums)

#당첨번호 비교 및 등수 출력
print("\n")
for i in range(amount):
    count=0
    for j in range(6):
        if my_nums[i][j]==win_nums[j]: count+=1
    if win_nums[6]==bonus: bonus=0

    if count==6: print('1등입니다!')
    elif count==5 and bonus==0: print('2등입니다!')
    elif count==5: print('3등입니다!')
    elif count==4: print('4등입니다!')
    elif count==3: print('5등입니다!')
    else: print('꽝!')