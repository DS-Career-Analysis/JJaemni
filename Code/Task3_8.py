import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:/VSC/JJaemni/CSV/Task3/'

df = pd.read_csv(path + 'wanted_dup.csv')

skl_list = []
for i in range(0, df.shape[0]):

    # 기술스택 ・ 툴 앞의 내용을 삭제
    text = df.Content[i]
    if '\n기술스택 ・ 툴' in text:
        skills_index = text.index('\n기술스택 ・ 툴')
        skills_text = text[skills_index:]
    else:
        skills_text = 'NaN'

    # 기술스택 ・ 툴 삭제
    text_replace = skills_text.replace('\n기술스택 ・ 툴', '')

    # 리스트에 요소 추가
    skl_list.append(text_replace)
    print(i, end=' ')
print(f'\nlen: {len(skl_list)}')

# 값 확인
for i in range(0, df.shape[0]):
    print(f'\n{i} -------------------------------------------------------------{skl_list[i]}\n-------------------------------------------------------------')

# 데이터프레임 생성
StackTool = pd.DataFrame({
    'StackTool': skl_list
})
StackTool.to_csv(path + 'wanted_5_StackTool.csv', index=False, encoding='utf-8-sig') 