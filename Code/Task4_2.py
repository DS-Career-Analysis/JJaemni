import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:/VSC/JJaemni/CSV/Task4/'



## 중복 채용공고 제거
df = pd.read_csv(path + 'jobplanet.csv')
value_counts = df.Link.value_counts()
vc = df[df.Link.isin(value_counts[df.Link.value_counts() > 1].index)]
print('\n---------------------------------------------')
print(f'중복 채용공고 개수: {vc.shape[0]}')

df_copy = df.copy()
for i in vc.index:
    df_copy.drop(i, inplace=True)
print(f'중복 채용공고 제거 후, 채용공고 개수: {df_copy.shape}')
print('---------------------------------------------')

df_copy.reset_index(drop=True, inplace=True)
df_copy.to_csv(path + 'jobplanet_dup.csv', index=False, encoding='utf-8-sig')