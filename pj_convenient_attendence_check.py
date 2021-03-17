import requests
from bs4 import BeautifulSoup as bs
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

s=requests.Session()

login_data={
    'usr': '학번',
    'pwd' : '유레카 비번'
}

log_url=('https://sso.ewha.ac.kr/SSO_IDP/swift/sso/loginForm.jsp?RSP=cyber.ewha.ac.kr&RelayState=%2FmakeSsoToken_php.jsp%3FretURL%3D%252F')
main_url=('https://cyber.ewha.ac.kr/')

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get(log_url)

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


usr="학번"
pwd="유레카 비번"

elem=driver.find_element_by_id("login_id")
elem.send_keys(usr)
elem=driver.find_element_by_id("usr_pwd")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)                 #엔터 누르게 함
time.sleep(3)

send_data(log_url,login_data)
check_login(main_url)

'''로그인 주소는 우클릭 > 검사 > Network > Doc > loginForm > Header 후 General에서 Request URL로 확인 가능함.
Status Code: 200 OK도 확인됨.'''