#========#========#========#========#
# write 
# 	230405~230411
# writer 
# 	sht
# content
# 	빅데이터 분석 강의 5주차
# 	- 데이터 분석 + 7장 연습문제
#========#========#========#========#

import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols, glm
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# colab
# print("[Magpie]>> Read CSV")
# red_df = pd.read_csv('/content/chap07_data/winequality-red.csv', sep=';', header=0, engine='python')
# white_df = pd.read_csv('/content/chap07_data/winequality-white.csv', sep=';', header=0, engine='python')

# print("[Magpie]>> Generate CSV")
# red_df.to_csv('/content/chap07_data/wine_quality_red_csv.csv', index=False)
# white_df.to_csv('/content/chap07_data/wine_quality_white_csv.csv', index=False)

# vs code
print("[Magpie]>> Read CSV")
print()
red_df = pd.read_csv('log/file/chap07_winequality-red.csv', sep=';', header=0, engine='python')
white_df = pd.read_csv('log/file/chap07_winequality-red.csv', sep=';', header=0, engine='python')

print("[Magpie]>> Generate :: wine_quality_red_csv")
print()
red_df.to_csv('./wine_quality_red_csv.csv', index=False)

print("[Magpie]>> Generate :: wine_quality_white_csv")
print()
white_df.to_csv('./wine_quality_white_csv.csv', index=False)




red_df.insert(0, column = 'type', value = 'red')
white_df.insert(0, column = 'type', value = 'white')

print("[Magpie]>> Combine wine")
print()
wine = pd.concat([red_df, white_df])
wine.shape

print("[Magpie]>> Generate :: wine_quality_csv")
print()
wine.to_csv('./wine_quality_csv.csv', index=False)
print(wine.info())
wine.columns = wine.columns.str.replace(' ','_')

wine.describe()
sorted(wine.quality.unique())
wine.quality.value_counts()



#========#========#========#========#
# statsmodels
#========#========#========#========#

red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']

stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var=False)

Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'
regression_result = ols(Rformula, data = wine).fit()
print()
print()
regression_result.summary()
print(regression_result.summary())
print()
print()

# 회귀 분석 모델로 새로운 샘플의 품질 등급 예측

sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]
sample1_predit = regression_result.predict(sample1)
sample1_predit

wine[0:5]['quality']

# data = {"fixed_acidity": [8.5, 8.1], "volatile_acidity": [0.8, 0.5], "citric_acid": [0.3, 0.4], "residual_sugar": [6.1, 5.8], "chlorides": [0.055, 0.04], "free_sulfur_dioxide": [30.0, 31.0], "total_sulfur_dioxide": [98.0, 99], "density": [0.996, 0.91], "pH": [3.25, 3.01], "sulphates": [0.4, 0.35], "alcohol": [9.0,0.8]}
data = {"fixed_acidity": [7.8], "volatile_acidity": [0.58], "citric_acid": [0.05], "residual_sugar": [2.0], "chlorides": [0.073], "free_sulfur_dioxide": [9.2], "total_sulfur_dioxide": [18.0], "density": [0.9968], "pH": [3.36], "sulphates": [0.57], "alcohol": [9.5]}
print()
print()
print()
print("[Magpie]>> data insert")
print(data)
print()
sample2 = pd.DataFrame(data, columns = sample1.columns)
sample2

sample2_predict = regression_result.predict(sample2)
print()
print("[Magpie]>> sample2_predict")
print(sample2_predict)
print()
print()
print()



sns.set_style('dark')
sns.distplot(red_wine_quality, kde= True, color = "red", label = 'red_wine')
sns.distplot(white_wine_quality, kde= True, color = "lightyellow", label = 'white_wine')

plt.title("Quality of Wine Type")
plt.legend()
plt.show()



# 부분 회귀 플롯으로 시각화

others = list(set(wine.columns).difference(set(["quality", "fixed_acidity"])))
p, resids = sm.graphics.plot_partregress("quality", "fixed_acidity", others, data = wine, ret_coords = True)

plt.show()



fig = plt.figure(figsize = (8, 13))
sm.graphics.plot_partregress_grid(regression_result, fig = fig)
plt.show()
