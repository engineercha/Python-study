import requests
from bs4 import BeautifulSoup as bs
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

s=requests.Session()

login_data={
    'usr': '2070081',
    'pwd' : 'Sss3778608'
}

usr="2070081"
pwd="Sss3778608"

main_url=('https://cyber.ewha.ac.kr/')
log_url=('https://sso.ewha.ac.kr/SSO_IDP/swift/sso/loginForm.jsp?RSP=cyber.ewha.ac.kr&RelayState=%2FmakeSsoToken_php.jsp%3FretURL%3D%252F')

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get(main_url)            #해당 url 사이트를 pc화면에 실행함

def send_data(url, login):
    resp=s.post(url, data=login)
    print(resp)                 #HTTP 상태 코드 출력함 (200=요청성공, 404=실패)

def check_login(url):
    res=s.get(url)
    time.sleep(2)
    soup=bs(res.text, 'html.parser')
    name=[]
    for tag in soup.select('h4.popover-body'):
        name.append(tag.text)
        print(tag.text)
    if '이름' in name: print("로그인 성공")
    else: print("로그인 실패")


#유레카 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/a').click()
time.sleep(1)

#아이디 비밀번호 입력
elem=driver.find_element_by_id("login_id")
elem.send_keys(usr)
elem=driver.find_element_by_id("usr_pwd")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)                 #엔터 누르게 함
time.sleep(2)

#공지사항 창 닫기 버튼(X) 클릭
driver.find_element_by_xpath('//*[@id="notice_popup_276_2715366"]/div/div/div[1]/button').click()
# driver.find_element_by_xpath('//*[@id="notice_popup_276_2715366"]/div/div/div[3]/span').click()

#강좌 링크 저장
course=driver.find_elements_by_css_selector('div.course_box > a')
links=[i.get_attribute('href') for i in course]
del links[-1]                               #마지막 링크는 채플이라 삭제함
print(links)

#학습진도현황 링크 저장
#for i in links:
driver.get(links[0])
completion=driver.find_element_by_css_selector('ul.topmenu>li>ul>li>a')
link=[i.get_attribute('href') for i in completion]
print(completion, type(completion)

res=requests.get(links[0])
soup=bs(res.text, 'html.parser')
completion=soup.find(attrs={'title':'학습진도현황'})
print(completion)

driver.find_element_by_xpath('//*[@id="coursemos-course-menu"]/ul/li[1]/div/div[2]/ul/li[2]/ul/li[1]/a').click()
print(soup.find_all('a', {'title':'학습진도현황'}))

send_data(log_url,login_data)
check_login(main_url)
'''로그인 주소는 우클릭 > 검사 > Network > Doc > loginForm > Header 후 General에서 Request URL로 확인 가능함.
Status Code: 200 OK도 확인됨.'''