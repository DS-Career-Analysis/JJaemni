import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:\\VSC\\JJaemni\\CSV\\Task4\\'

df = pd.read_csv(path + 'jobplanet.csv')

loc_list = []
for i in range(0, df.shape[0]):

    # 회사위치 앞의 내용을 삭제
    text = df.Content[i]
    if '회사위치' in text:
        lcts_index = text.index('회사위치')
        lcts_text = text[lcts_index:]
    else:
        lcts_text = 'NaN'  

    # 회사위치 뒤의 내용을 삭제
    if '문의처' in lcts_text:
        lcts_index = lcts_text.index('문의처')
        lcts_text = lcts_text[:lcts_index]

    # 회사위치 삭제
    text_replace = lcts_text.replace('회사위치', '')

    # 리스트에 요소 추가
    loc_list.append(text_replace)
    print(i, end=' ')
print(f'\nlen: {len(loc_list)}')

# 값 확인
for i in range(0, df.shape[0]):
    print(f'\n{i} -------------------------------------------------------------{loc_list[i]}-------------------------------------------------------------')

# 데이터프레임 생성
Location = pd.DataFrame({
    'Detailed_Locatio': loc_list
})
Location.to_csv(path + 'jobplanet_Detailed_Location.csv', index=False, encoding='utf-8-sig')