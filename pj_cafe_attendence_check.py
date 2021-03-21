import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#현재시간 출력
now=str(datetime.datetime.now()).replace('-',' ').replace(':',' ').split()
hour=now[3]; minute=now[4]
print(hour,minute)

id='네이버아이디'
pw='네이버비밀번호'


url=('https://www.naver.com/')
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

driver.find_element_by_xpath('//*[@id="account"]/a').click()

#로그인
driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(2)

#카페 검색
cafe='코뮤니티'
driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[2]/a').click()
driver.find_element_by_class_name("snb_search_text").send_keys(cafe)
time.sleep(1)

driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/form/fieldset/div/button/span[2]').click()

#카페 링크 크롤링


#출석체크 게시판 이동 및 출석
post='ㅊㅊ'
driver.get('https://cafe.naver.com/codeuniv')
driver.find_element_by_xpath('//*[@id="menuLink31"]').click()
driver.find_element_by_id('cmtinput').send_keys(post)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()