import requests
from bs4 import BeautifulSoup

lotto_url = ('https://dhlottery.co.kr/gameResult.do?method=byWin')
raw = requests.get(lotto_url)
# print(raw)

soup = BeautifulSoup(raw.text, 'html.parser')
# print(soup)

box = soup.find('div', {'class' : 'nums'})
# print(box)
numbers = box.find_all('span')
# for number in numbers: 
#     print(number)
for number in numbers:
    print(number.text)