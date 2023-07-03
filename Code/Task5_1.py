import pandas as pd
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:\\VSC\\JJaemni\\CSV\\Task5\\'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}



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
def Incruit(link_key):

    # webdriver 실행
    driver = webdriver.Chrome()
    driver.get(f'https://search.incruit.com/list/search.asp?col=job&kw={link_key}&startno=0&psize=60')
    scroll(driver)
    


    # 데이터 수집 : 링크 타이틀 회사
    page = int(input(f'{link_key} final page = '))

    Lin = [] # 링크
    Tit = [] # 타이틀
    Com = [] # 회사
    for p in range(0, page): # 인크루트는 페이지 1이 0부터 시작함
        try:
            soup = requests.get(f'https://search.incruit.com/list/search.asp?col=job&kw={link_key}&startno={p * 60}&psize=60', 
                                headers=headers)   
            html = BeautifulSoup(soup.text, 'html.parser')

            cell_mid = html.select('div.cell_mid > div.cl_top')
            for elem in cell_mid:
                job_1 = elem.find('a')['href']
                job_2 = elem.find('a').text
                Lin.append(job_1)
                Tit.append(job_2)
            
            cell_first = html.select('div.cell_first > div.cl_top')
            for elem in cell_first:
                job_3 = elem.find('a').text
                Com.append(job_3)
        except Exception as e:
            print(e)
            break
    driver.close()



    # 데이터 출력
    elem_return1('링크', Lin)
    elem_return1('타이틀', Tit)
    elem_return1('회사', Com)
    


    # src에 들어갈 숫자 추출
    Lin2 = []
    for i in range(0, len(Lin)):
        lin_strip = Lin[i].strip('https://job.incruit.com/jobdb_info/jobpost.asp?job=').strip('&src=etc*se')
        Lin2.append(lin_strip)



    # 데이터 수집 : 공고내용
    Ctn = []

    for i in Lin2:
        try:
            soup = requests.get(f'https://job.incruit.com/s_common/jobpost/jobpostcont.asp?job={i}', 
                                headers=headers)   
            html = BeautifulSoup(soup.text, 'html.parser')
            
            content = html.select('html')
            for elem in content:
                job_4 = elem.text
                Ctn.append(job_4)
        except Exception as e:
            print(e)
            break



    # 데이터 출력
    elem_return2('공고내용', Ctn)



    # 데이터프레임 생성 및 데이터 저장   
    df = pd.DataFrame({
        'Title' : Tit,
        'Company' : Com,
        'Content' : Ctn,   
        'Link' : Lin,
        'Location' : 'None',
        'label' : f'{link_key}'         
    })
    df.to_csv(path + f'{link_key}.csv', index=False, encoding='utf-8-sig')
    df = pd.read_csv(path + f'{link_key}.csv')



## Incruit
KEY = ['데이터 사이언티스트', '데이터 애널리스트', '데이터 엔지니어']
for link_key in KEY:
    Incruit(link_key)

## 데이터 merge
DS = pd.read_csv(path + '데이터 사이언티스트.csv')
DA = pd.read_csv(path + '데이터 애널리스트.csv')
DE = pd.read_csv(path + '데이터 엔지니어.csv')
df = pd.concat([DS, DA, DE])
df.to_csv(path + 'incruit.csv', index=False, encoding='utf-8-sig')