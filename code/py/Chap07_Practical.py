#========#========#========#========#
# write 
# 	230411
# writer 
# 	sht
# content
# 	빅데이터 분석 강의 5주차
# 	- 7장 실습문제
#========#========#========#========#

import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols



print("[Magpie]>> Read CSV")
columnname = ["Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
# [Q-1]
wine_df = pd.read_csv('F:/Silla/4-1/bigdata/실습문제/winedata.txt', sep=',', header=0, engine='python')
wine_df.columns = columnname
# [Q-2]
wine_df.columns = wine_df.columns.str.replace(' ','_')
print("[Magpie]>> Generate CSV")
wine_df.to_csv('./winedata.csv', index=True)
print()
print()

wine = pd.read_csv('./winedata.csv', sep=',', header=0, engine='python')

print("[Magpie]>> Wine Information")
print(wine.info())
print()
print()
# [Q-4]
print("[Magpie]>> Wine Describe")
print(wine.describe())
print()
print()
# [Q-5]
print("[Magpie]>> Magnesium Mean")
print(wine['Magnesium'].mean())
print()
print()
# [Q-6]
print("[Magpie]>> Alcohol Max")
print(wine['Alcohol'].max())
print()
print()
# [Q-7]
print("[Magpie]>> Group Class Mean")
print(wine.groupby('Class').mean())

