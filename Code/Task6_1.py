import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:/VSC/JJaemni/CSV/'
Task3_path = 'C:/VSC/JJaemni/CSV/Task3/'
Task4_path = 'C:/VSC/JJaemni/CSV/Task4/'

# 원티드 데이터
wanted = pd.read_csv(Task3_path + 'wanted_dup.csv')
ds_w = pd.read_csv(Task3_path + 'wanted_3_Requirement.csv')
da_w = pd.read_csv(Task3_path + 'wanted_4_Preference.csv')
de_w = pd.read_csv(Task3_path + 'wanted_5_StackTool.csv')

# 원티드 3가지 insert
wanted.insert(3, 'Requirement', ds_w)
wanted.insert(4, 'Preference', da_w)
wanted.insert(5, 'StackTool', de_w)

# 원티드 Location 전처리:  '· 한국' -> ''
L = []
for i in range(0, wanted.shape[0]):
    a = wanted.Location[i].replace(' · 한국', '')
    L.append(a)
loc_w = pd.DataFrame({'Location': L})
wanted.Location = loc_w

# 잡플래닛 데이터
jobplanet = pd.read_csv(Task4_path + 'jobplanet_dup.csv')
ds_j = pd.read_csv(Task4_path + 'jobplanet_3_Requirement.csv')
da_j = pd.read_csv(Task4_path + 'jobplanet_4_Preference.csv')
de_j = pd.read_csv(Task4_path + 'jobplanet_5_StackTool.csv')

# 잡플래닛 3가지 insert
jobplanet.insert(3, 'Requirement', ds_j)
jobplanet.insert(4, 'Preference', da_j)
jobplanet.insert(5, 'StackTool', de_j)

# 원티드 잡플래닛 merge
df = pd.concat([wanted, jobplanet])
df.reset_index(drop=True, inplace=True)
sorted_df = df.sort_values('label')
sorted_df.reset_index(drop=True, inplace=True)

sorted_df.to_csv('C:/VSC/JJaemni/CSV/wanted_jobplanet.csv', index=False, encoding='utf-8-sig')

# Null값 확인
sorted_df = pd.read_csv('C:/VSC/JJaemni/CSV/wanted_jobplanet.csv')
print(f'{sorted_df.shape = }')
print(f'## Null ##\n{sorted_df.isnull().sum()}')