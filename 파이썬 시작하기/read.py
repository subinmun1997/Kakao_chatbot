import pandas as pd

user_list = pd.read_excel('sample.xlsx', sheet_name='Sheet1')
print(user_list)