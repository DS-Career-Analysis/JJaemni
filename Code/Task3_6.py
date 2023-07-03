import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:\\VSC\\JJaemni\\CSV\\Task3\\'

df = pd.read_csv(path + 'wanted.csv')

req_list = []
for i in range(0, df.shape[0]):
    
    # 자격요건 앞의 내용을 삭제
    text = df.Content[i]
    if '자격요건' in text:    
        requires_index = text.index('자격요건')
        requires_text = text[requires_index:]
    else:
        requires_text = 'NaN'

    # 자격요건 뒤의 내용을 삭제
    patterns = [
        '우대사항',
        '혜택 및 복지',
        '[필수 제출 서류]',
        '[기술스텍]',
        '■ 기술 스택 및 협업툴'
    ]
    for pattern in patterns:
        if pattern in requires_text:
            requires_index = requires_text.index(pattern)
            requires_text = requires_text[:requires_index]

    # 자격요건 삭제
    text_replace = requires_text.replace('자격요건', '')

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
Requirement.to_csv(path + 'wanted_3_Requirement.csv', index=False, encoding='utf-8-sig')