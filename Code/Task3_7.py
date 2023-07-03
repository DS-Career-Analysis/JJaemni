import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:\\VSC\\JJaemni\\CSV\\Task3\\'

df = pd.read_csv(path + 'wanted.csv')

prf_list = []
for i in range(0, df.shape[0]):

    # 우대사항 앞의 내용을 삭제
    text = df.Content[i]
    if '우대사항' in text:
        prefers_index = text.index('우대사항')
        prefers_text = text[prefers_index:]
    else:
        prefers_text = 'NaN'

    # 우대사항 뒤의 내용을 삭제
    patterns = [
        '혜택 및 복지',
        '*전형절차',
        '참고해주세요',
        '[Tech Stack]',
        '#데이터 사이언티스트 기술 스택',
        ' 이런 문화로 일하고 있어요',
        '[레몬베이스 Data 팀에 합류해야 하는 이유]',
        '참고해 주세요',
        '【 기술스택 】',
        '[개발환경]',
        '【페이타랩의 근무 문화 및 환경】',
        '[합류 여정]',
        '[이런 기술을 사용하고 있어요]',
        '[핵클이 사용하는 기술]',
        '[근무 환경]',
        '[전형 프로세스]',
        '■ 채용 절차'
    ]
    for pattern in patterns:
        if pattern in prefers_text:
            prefers_index = prefers_text.index(pattern)
            prefers_text = prefers_text[:prefers_index]

    # 우대사항 삭제
    text_replace = prefers_text.replace('우대사항', '')

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
Preference.to_csv(path + 'wanted_4_Preference.csv', index=False, encoding='utf-8-sig')