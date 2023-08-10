import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:\\VSC\\JJaemni\\CSV\\Task3\\'



## DevTools 메세지 안 뜨게
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(executable_path='<C:\VSC\JaeminHong\Code\chromedriver.exe>', options=options)



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
    driver.implicitly_wait(3)



## 스크롤 한 번만
# def scroll_one(driver):
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(1)
#     driver.implicitly_wait(3)



## elem return 1
def elem_return1(Name, List):
    return print(f'\n{Name} *** {len(List)}\n{List[0]}')



## elem return 2
def elem_return2(Name, List):
    return print(f'\n{Name} *** {len(List)}')



## DS, DA, DE 수집
def Wanted(link_key):

    # webdriver 실행
    driver = webdriver.Chrome()
    driver.get(f'https://www.wanted.co.kr/search?query={link_key}')
    driver.implicitly_wait(2)
    
    # 포지션 선택
    elem = driver.find_element(By.XPATH, '//*[@id="search_tab_position"]')
    elem.click()
    driver.implicitly_wait(2)
    scroll(driver)



    # 검색 키워드 출력
    print(f'\n\n########## {link_key} ##########')



    # 데이터 수집
    Lin = [] # 링크
    Tit = [] # 타이틀
    Com = [] # 회사
    Loc = [] # 위치
    
    search = driver.find_element(By.XPATH, '//*[@id="search_tabpanel_position"]/div/div[1]/h2/span').text # 공고 개수
    for i in range(1, int(search)+1):
        try:
            # 링크
            job_1 = driver.find_element(By.XPATH, f'//*[@id="search_tabpanel_position"]/div/div[4]/div[{i}]/a').get_attribute('href')
            Lin.append(job_1)

            # 타이틀
            job_2 = driver.find_element(By.XPATH, f'//*[@id="search_tabpanel_position"]/div/div[4]/div[{i}]/a/div[2]/strong').text
            Tit.append(job_2)

            # 회사
            job_3 = driver.find_element(By.XPATH, f'//*[@id="search_tabpanel_position"]/div/div[4]/div[{i}]/a/div[2]/span[1]/span[1]').text
            Com.append(job_3)

            # 위치
            job_4 = driver.find_element(By.XPATH, f'//*[@id="search_tabpanel_position"]/div/div[4]/div[{i}]/a/div[2]/span[1]/span[2]').text
            Loc.append(job_4)
        except Exception as e:
            print(e)
            break



    # 데이터 출력
    elem_return1('링크', Lin)
    elem_return1('타이틀', Tit)
    elem_return1('회사', Com)
    elem_return1('위치', Loc)



    # 데이터 수집
    Ctn = [] # 공고내용

    for i in Lin:
        driver.get(i)
        driver.implicitly_wait(2)
        scroll(driver)

        # 공고내용
        try:
            job_5 = driver.find_element(By.CLASS_NAME, 'JobDescription_JobDescription__VWfcb').text
            Ctn.append(job_5)
        except Exception as e:
            print(e)
            break

        # # 위치
        # try:
        #     job_5 = driver.find_element(By.CLASS_NAME, 'JobWorkPlace_className__ra6rp').text
        #     time.sleep(1)
        #     Loc.append(job_5)
        # except Exception as e:
        #     Loc.append('None')
        #     pass

    driver.close()



    # 데이터 출력
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



## Wanted
KEY = ['데이터 사이언티스트', '데이터 애널리스트', '데이터 엔지니어']
for link_key in KEY:
    Wanted(link_key)

## 데이터 merge
DS = pd.read_csv(path + '데이터 사이언티스트.csv')
DA = pd.read_csv(path + '데이터 애널리스트.csv')
DE = pd.read_csv(path + '데이터 엔지니어.csv')
df = pd.concat([DS, DA, DE], axis=0)
df.to_csv(path + 'wanted.csv', index=False, encoding='utf-8-sig')