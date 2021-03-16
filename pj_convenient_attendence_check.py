import requests
from bs4 import BeautifulSoup as bs

s=requests.Session()

login_data={
    'id': '~~~여러분의 아이디~~~',
    'passwor' : '~~~여러분의 비번~~~'
}

log_url=('https://sso.ewha.ac.kr/SSO_IDP/swift/sso/loginForm.jsp?RSP=cyber.ewha.ac.kr&RelayState=%2FmakeSsoToken_php.jsp%3FretURL%3D%252F')
main_url=('https://cyber.ewha.ac.kr/')


def send_data(url, login):
    resp=s.post(url, data=login)
    print(resp)                     #HTTP 상태 코드 출력, 200=요청성공, 404=실패, 403=금지

def check_login(url):
    res=s.get(url)
    checker=bs(res.text, 'html.parser')
    # name=checker.find_all('li', {'class':'nav-item.user_department.hidden-xs'})
    # results=checker.find_all('li')

    box = checker.find('nav', {'class':'navbar_navbar-default_navbar-fixed-top_headroom'})
    name = box.findAll('li')
    print(name)

    if '~~~여러분의 이름~~~' in str(name): print("로그인 성공")
    else: print("로그인 실패")

send_data(log_url,login_data)
check_login(main_url)

'''로그인 주소는 우클릭 > 검사 > Network > Doc > loginForm > Header 후 General에서 Request URL로 확인 가능함.
Status Code: 200 OK도 확인됨.'''