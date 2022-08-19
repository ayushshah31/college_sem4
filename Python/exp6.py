# x = 11
# assert x<10 , "Wrong Input"
# print(" you have entered:",x)

import pandas as pd
import xlrd

# Open excel file
df = pd.read_excel(r'/Users/ayushshah/Downloads/student.xlsx')
# print(df)

#Q) Create own database
# data = {      'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
#  'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
#  'age': [41, 28, 33, 34, 38, 31, 37],
#  'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
#  }
# df2 = pd.DataFrame(data)
# print(df2)

# Open csl file
# df.to_csv(r'/Users/ayushshah/Downloads/student.csv')
# # print(df)
# # r,c = df.shape
# # print(r,c)
# # df.head()
# # print(df.head(3))
# # print(df.columns)
# # print(df[['name','mark']])
# # print(df['mark'].min())
# # print(df.describe())
# # print(df[df.marks>74])
# # print(df.mark>24)
# # print(df[df.mark==88])
# # print(df[df.mark==df.mark.max()])
# df3 = df.set_index('id')
# # print(df3)
# print(df.loc[34])
# # print(df)

# df4 = df.sort_values(by=['mark','name'],ascending=[True,False])
# print(df4)

# Q) max , min , sort , top3 , last3
data = {      'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}
df = pd.DataFrame(data)
print(df.max())
print(df.min())
df1 = df.sort_values(by=['py-score','name'],ascending=[True,False])
print(df1)
print(df1.head(3))
print(df1.tail(3))