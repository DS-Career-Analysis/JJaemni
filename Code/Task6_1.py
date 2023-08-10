import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)
path = 'C:\\VSC\\JJaemni\\CSV\\'

wanted = pd.read_csv(path + 'Task3\\wanted.csv')
jobplanet = pd.read_csv(path + 'Task4\\jobplanet.csv')

print(f'{wanted.shape = }\n{jobplanet.shape = }')
print(f'## wanted Null ##\n{wanted.isnull().sum()}\n\n## jobplanet Null ##\n{jobplanet.isnull().sum()}')