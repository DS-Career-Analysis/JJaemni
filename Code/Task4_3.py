import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:/VSC/JJaemni/CSV/Task4/'

df = pd.read_csv(path + 'jobplanet_dup.csv')

req_list = []
for i in range(0, df.shape[0]):

    # 자격 요건 앞의 내용을 삭제
    text = df.Content[i]
    if '자격 요건' in text:
        requires_index = text.index('자격 요건')
        requires_text = text[requires_index:]
    else:
        requires_text = 'NaN'

    # 자격 요건 뒤의 내용을 삭제
    if '우대사항' in requires_text:
        requires_index = requires_text.index('우대사항')
        requires_text = requires_text[:requires_index]
    elif '채용 절차' in requires_text:
        requires_index = requires_text.index('채용 절차')
        requires_text = requires_text[:requires_index]       

    # 자격 요건 삭제
    text_replace = requires_text.replace('자격 요건', '')

    # 리스트에 요소 추가
    req_list.append(text_replace)
    print(i, end=' ')
print(f'\nlen: {len(req_list)}')

# 값 확인
for i in range(0, df.shape[0]):
    print(f'\n{i} -------------------------------------------------------------{req_list[i]}-------------------------------------------------------------')

# 데이터프레임 생성
Requirement = pd.DataFrame({
    'Requirement': req_list
})
Requirement.to_csv(path + 'jobplanet_3_Requirement.csv', index=False, encoding='utf-8-sig')