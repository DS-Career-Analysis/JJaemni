import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:\\VSC\\JJaemni\\CSV\\Task4\\'

df = pd.read_csv(path + 'jobplanet.csv')

skl_list = []
for i in range(0, df.shape[0]):

    # 스킬 뒤의 내용을 삭제
    text = df.Content[i]
    if '기업 이미지' in text:
        other_index = text.index('기업 이미지')
        other_text = text[:other_index]
    elif '기업 소개' in text:
        other_index = text.index('기업 소개')
        other_text = text[:other_index]

    # 스킬 앞의 내용을 삭제
    if '스킬' in other_text:
        skills_index = other_text.index('스킬')
        skills_text = other_text[skills_index:]
    else:
        skills_text = 'NaN'

    # 스킬 삭제
    text_replace = skills_text.replace('스킬', '')

    # 리스트에 요소 추가
    skl_list.append(text_replace)
    print(i, end=' ')
print(f'\nlen: {len(skl_list)}')

# 값 확인
for i in range(0, df.shape[0]):
    print(f'\n{i} -------------------------------------------------------------{skl_list[i]}-------------------------------------------------------------')

# 데이터프레임 생성
StackTool = pd.DataFrame({
    'StackTool': skl_list
})
StackTool.to_csv(path + 'jobplanet_5_StackTool.csv', index=False, encoding='utf-8-sig')