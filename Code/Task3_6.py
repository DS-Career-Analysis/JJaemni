import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:/VSC/JJaemni/CSV/Task3/'

df = pd.read_csv(path + 'wanted_dup.csv')

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
        '주요업무',
        '우대사항',
        '혜택 및 복지',
        '기술스택 ・ 툴',
        '[기술스텍]',
        '[기술 스택]',
        '【 이렇게 합류하게 돼요 】',
        '[채용 절차] ',
        '기술 스택',
        '*전형절차',
        '[필수 제출 서류]',
        '■ 기술 스택 및 협업툴',
        '[레몬베이스 Data 팀에 합류해야 하는 이유]',
        '사용하는 기술/Tool 은 아래와 같습니다.',
        '#리텐틱스의 기술 스택',
        '제출서류',
        '[Tech Stack]',
        '[전형절차]',
        '참고해 주세요',
        '[합류 여정]',
        '■ 정규직',
        '[핵클이 사용하는 기술]',
        '핀다 데이터 플랫폼팀에서 사용하고 있는 기술',
        '【페이타랩의 근무 문화 및 환경】',
        '[필요역량]',
        '[과제 및 테스트]',
        '[주요 기술 스택은 아래와 같아요]',
        '[개발환경]',
        '[이런 기술을 사용하고 있어요]',
        '[전형 프로세스]',
        '[근무 환경]',
        '기술 스택/툴'
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