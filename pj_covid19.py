import time
import requests
from bs4 import BeautifulSoup

print(time.localtime())
print("코로나바이러스감염증-19 (COVID-19)")

covid19_url = ("https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EA%B5%AD%EB%82%B4+%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90+%ED%98%84%ED%99%A9&oquery=%ED%81%AC%EB%A1%A4%EB%A7%81+for+number&tqi=huh4Msp0JXossExdgw4ssssstHs-369932&acq=%ED%99%95%EC%A7%84%EC%9E%90+%ED%98%84%ED%99%A9&acr=1&qdt=0")
raw = requests.get(covid19_url)
soup = BeautifulSoup(raw.text, 'html.parser')

# box1 = soup.find('div', {'class' : 'csp_infoCheck_area._togglor_root'})
times = soup.find('span', {'class' : '_update_time'})
print(times)

box = soup.find('div', {'class' : 'status_info'})
numbers = box.find_all('p')
i=0

for number in numbers:
    if i==0:
        cases_in=number.text
    elif i==1:
        test_in=number.text
    elif i==2:
        lift_in=number.text
    else: deaths_in=number.text
    i+=1

# cases_ex = 107778431
# deaths_ex = 2368525

print("\n<국내현황>")
print("확진환자", cases_in)
print("검사중  ", test_in)
print("격리해제", lift_in)
print("사망자  ", deaths_in)

# print("\n<세계현황>")
# print("확진환자", cases_ex)
# print("사망자  ", deaths_ex)

# print("\n세계 대비 국내 확진환자 비율:",cases_in/cases_ex*100,"%")
# print("세계 대비 국내   사망자 비율:",deaths_in/deaths_ex*100,"%")

# drate_in = deaths_in/cases_in*100
# drate_ex = deaths_ex/cases_ex*100
# print('\n국내 치명률: %.3f'%drate_in,"%") 
# print('세계 치명률: %.3f'%drate_ex,"%")

if drate_in > drate_ex:
    print("국내 치명률은 세계 치명률 보다 약",drate_in - drate_ex,"% 높습니다")
elif drate_in < drate_ex:
    print("국내 치명률은 세계 치명률 보다 약",drate_ex - drate_in,"% 낮습니다.")
else: print("국내 치명률은 세계 치명률과 같습니다.")