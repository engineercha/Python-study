import re
import time
import requests
from bs4 import BeautifulSoup

print(time.localtime())
print("코로나바이러스감염증-19 (COVID-19)")

covid19_url = ("https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EA%B5%AD%EB%82%B4+%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90+%ED%98%84%ED%99%A9&oquery=%ED%81%AC%EB%A1%A4%EB%A7%81+for+number&tqi=huh4Msp0JXossExdgw4ssssstHs-369932&acq=%ED%99%95%EC%A7%84%EC%9E%90+%ED%98%84%ED%99%A9&acr=1&qdt=0")
res = requests.get(covid19_url)
soup = BeautifulSoup(res.text, 'html.parser')

times = soup.find_all('span', {'class':'_update_time'})
print(times[1].get_text(),"기준")

box = soup.find('div', {'class' : 'status_info'})
numbers = box.findAll('p')
box2 = soup.find('div', {'class' : 'status_info abroad_info'})
numbers_ex = box2.findAll('p')


cases_in=numbers[0].text
test_in=numbers[1].text
lift_in=numbers[2].text
deaths_in=numbers[3].text

cases_ex=numbers_ex[0].text
deaths_ex=numbers_ex[1].text

print("\n<국내현황>")
print("확진환자", cases_in)
print("검사중  ", test_in)
print("격리해제", lift_in)
print("사망자  ", deaths_in)

print("\n<세계현황>")
print("확진환자", cases_ex)
print("사망자  ", deaths_ex)


C=re.findall('\d',cases_in)
rtc=""
for n in C:
    rtc+=n
cases_in=int(rtc)

D=re.findall('\d',deaths_in)
rtd=""
for n in D:
    rtd+=n
deaths_in=int(rtd)

C2=re.findall('\d',cases_ex)
rtc2=""
for n in C2:
    rtc2+=n
cases_ex=int(rtc2)

D2=re.findall('\d',deaths_ex)
rtd2=""
for n in D2:
    rtd2+=n
deaths_ex=int(rtd2)


print("\n세계 대비 국내 확진환자 비율:",cases_in/cases_ex*100,"%")
print("세계 대비 국내   사망자 비율:",deaths_in/deaths_ex*100,"%")

rate_in = deaths_in/cases_in*100
rate_ex = deaths_ex/cases_ex*100
print('\n국내 치명률: %.3f'%rate_in,"%") 
print('세계 치명률: %.3f'%rate_ex,"%")

if rate_in > rate_ex:
    print("국내 치명률은 세계 치명률 보다 약",rate_in - rate_ex,"% 높습니다")
elif rate_in < rate_ex:
    print("국내 치명률은 세계 치명률 보다 약 %.3f"%(rate_ex - rate_in),"% 낮습니다.")
else: print("국내 치명률은 세계 치명률과 같습니다.")