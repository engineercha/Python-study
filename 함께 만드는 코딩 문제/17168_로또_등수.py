import requests
from bs4 import BeautifulSoup as bs
import random
import time


#당첨번호 가져오기(일반번호 6개 + 보너스번호 1개)
raw = requests.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin')
soup = bs(raw.text, 'html.parser')

box = soup.find('div', {'class' : 'nums'})
nums = box.find_all('span')
win_nums = []
for num in nums:
    win_nums.append(num.text)

#로또번호 입력 및 보너스(자동)
my_nums=input('번호 6개를 띄어쓰기로 나눠 입력하세요: ').split(' ')
bonus=my_nums.append(random.randrange(1,46))

#로또 출력
print("\n\t\tLotto 6/45")
print("----------------------------------------")
print("A",my_nums)
print("----------------------------------------")
print("금액\t\t\t\t₩1,000\n")

#당첨번호와 비교
print("당첨 확인 중·",end='')
time.sleep(1)
print("·",end='')
time.sleep(1)
print("·")
count=0
for i in range(6):
    if win_nums[i]==my_nums[i]: count+=1
if win_nums[6]==bonus: bonus=0

#등수 출력
if count == 6: print('1등입니다!')
elif count == 5 and bonus==0: print('2등입니다!')
elif count == 5: print('3등입니다!')
elif count == 4: print('4등입니다!')
elif count == 3: print('5등입니다!')
else: print('꽝! 다음 기회에.')

#당첨번호 출력
print(win_nums)