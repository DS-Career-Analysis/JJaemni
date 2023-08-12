import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:/VSC/JJaemni/CSV/Task4/'

df = pd.read_csv(path + 'jobplanet_dup.csv')

prf_list = []
for i in range(0, df.shape[0]):

    # 우대사항 앞의 내용을 삭제
    text = df.Content[i]
    if '우대사항' in text:
        requires_index = text.index('우대사항')
        requires_text = text[requires_index:]
    else:
        requires_text = 'NaN'

    # 우대사항 뒤의 내용을 삭제
    patterns = [
        '채용 절차',
        '복리후생',
        '*전형절차',
        '#리텐틱스의 기술 스택'
    ]
    for pattern in patterns:
        if pattern in requires_text:
            requires_index = requires_text.index(pattern)
            requires_text = requires_text[:requires_index]

    # 우대사항 삭제
    text_replace = requires_text.replace('우대사항', '')

    # 리스트에 요소 추가
    prf_list.append(text_replace)
    print(i, end=' ')
print(f'\nlen: {len(prf_list)}')

# 값 확인
for i in range(0, df.shape[0]):
    print(f'\n{i} -------------------------------------------------------------{prf_list[i]}-------------------------------------------------------------')

# 데이터프레임 생성
Preference = pd.DataFrame({
    'Preference': prf_list
})
Preference.to_csv(path + 'jobplanet_4_Preference.csv', index=False, encoding='utf-8-sig')