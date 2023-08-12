import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:/VSC/JJaemni/CSV/Task4/'



## DevTools 메세지 안 뜨게
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--log-level=3")  # 로그 레벨을 최소화하여 메시지를 더 감춥니다
# driver = webdriver.Chrome(options=options)



## 스크롤
def scroll(driver):
    scroll_location = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        scroll_height = driver.execute_script('return document.body.scrollHeight')
        if scroll_location == scroll_height:
            break
        else:
            scroll_location = driver.execute_script('return document.body.scrollHeight')
    driver.implicitly_wait(5)



## 스크롤 한 번만
def scroll_one(driver):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
    driver.implicitly_wait(3)



## elem return 1
def elem_return1(Name, List):
    return print(f'\n{Name} *** {len(List)}\n{List[0]}')



## elem return 2
def elem_return2(Name, List):
    return print(f'\n{Name} *** {len(List)}')



## DS, DA, DE 수집
def Jobplanet(btn, link_key):

    # webdriver 실행
    driver = webdriver.Chrome()
    driver.get('https://www.jobplanet.co.kr/job')

    # # 직종 클릭
    # time.sleep(1)
    # elem = driver.find_element(By.CLASS_NAME, 'jply_btn_sm.inner_text.jf_b2')
    # elem.click()
    # # 전체 직종 중 '데이터' 클릭
    # time.sleep(1)
    # elem = driver.find_element(By.XPATH, '//*[@id="occupation_level1_filter"]/div/div[2]/div[1]/div[1]/ul/li[6]/button')
    # elem.click()
    # # '데이터'에서 데이터 사이언티스트, 데이터 분석가, 데이터 엔지니어를 차례대로 클릭
    # time.sleep(1)
    # elem = driver.find_element(By.XPATH, f'//*[@id="occupation_level1_filter"]/div/div[2]/div[1]/div[2]/ul/li[{btn}]')                                         
    # elem.click()
    # # '적용' 클릭
    # time.sleep(1)    
    # elem = driver.find_element(By.XPATH, '//*[@id="occupation_level1_filter"]/div/div[2]/div[2]/button[2]')
    # elem.click()
    time.sleep(10)
    scroll(driver)



    # 검색 키워드 출력
    print(f'\n\n########## {link_key} ##########')



    # 데이터 수집
    Lin = [] # 링크
    Tit = [] # 타이틀
    Com = [] # 회사

    first = driver.find_elements(By.CLASS_NAME, 'item-card')
    for elem in first:
        try:
            # 링크
            job_1 = elem.find_element(By.TAG_NAME, 'a').get_attribute('href')
            Lin.append(job_1)

            # 타이틀
            job_2 = elem.find_element(By.CLASS_NAME, 'item-card__title').text
            Tit.append(job_2)

            # 회사
            job_3 = elem.find_element(By.CLASS_NAME, 'item-card__name').text
            Com.append(job_3)
        except Exception as e:
            print(e)
            break



    # 데이터 출력
    elem_return1('링크', Lin)
    elem_return1('타이틀', Tit)
    elem_return1('회사', Com)



    # 데이터 수집
    Ctn = [] # 공고내용
    Loc = [] # 위치

    for i in Lin:
        driver.get(i)
        time.sleep(1)
        scroll_one(driver)
        time.sleep(1)

        try:
            # 위치
            job_4 = driver.find_element(By.CLASS_NAME, 'job_location').text
            Loc.append(job_4)

            # 공고내용
            job_5 = driver.find_element(By.CLASS_NAME, 'job_body').text                  
            Ctn.append(job_5)
        except Exception as e:
            print(e)
            break

        # # 위치
        # try:
        #     job_5 = driver.find_element(By.XPATH, '//*[@id="job_search_app"]/div/div[2]/section/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div/span[4]/span').text
        #     Loc.append(job_5)
        # except Exception as e:
        #     print(e)
        #     break

    driver.close()



    # 데이터 출력
    elem_return1('위치', Loc)
    elem_return2('공고내용', Ctn)



    # 데이터프레임 생성 및 데이터 저장
    df = pd.DataFrame({
        'Title' : Tit,
        'Company' : Com,
        'Content' : Ctn,   
        'Link' : Lin,
        'Location' : Loc,
        'label' : f'{link_key}'         
    })
    df.to_csv(path + f'{link_key}.csv', index=False, encoding='utf-8-sig')
    df = pd.read_csv(path + f'{link_key}.csv')



## Jobplanet
BUTTON = [4, 3, 5]
KEY = ['데이터 사이언티스트', '데이터 애널리스트', '데이터 엔지니어']
for btn, link_key in zip(BUTTON, KEY):
    Jobplanet(btn, link_key)

## 데이터 merge
DS = pd.read_csv(path + '데이터 사이언티스트.csv')
DA = pd.read_csv(path + '데이터 애널리스트.csv')
DE = pd.read_csv(path + '데이터 엔지니어.csv')
df = pd.concat([DS, DA, DE], axis=0)
df.to_csv(path + 'jobplanet.csv', index=False, encoding='utf-8-sig')